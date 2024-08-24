from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models import UserModel, PhoneModel, EmailModel, SocialAccountModel, Base
from schemas import UserCreate, UserInDB, PhoneCreate, EmailCreate, SocialAccountCreate
from authentication import create_access_token, get_password_hash, verify_password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

user_router_v0 = APIRouter()


@app.post("/get-token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    user = await db.query(UserModel).filter(UserModel.user_login == form_data.username).first()
    if not user or not verify_password(form_data.password, user.user_hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.user_login}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/logup/", response_model=UserInDB)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = UserModel(
        user_login=user.user_login,
        user_hashed_password=get_password_hash(user.user_hashed_password),
        user_Last_name=user.user_Last_name,
        user_first_name=user.user_first_name,
        user_patronymic=user.user_patronymic,
        user_group_number=user.user_group_number
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

    for phone in user.phones:
        db_phone = PhoneModel(user_id=db_user.id, phone=phone.phone)
        db.add(db_phone)
    
    for email in user.emails:
        db_email = EmailModel(user_id=db_user.id, email=email.email)
        db.add(db_email)
    
    for account in user.social_accounts:
        db_account = SocialAccountModel(user_id=db_user.id, account_type=account.account_type, account_id=account.account_id)
        db.add(db_account)
    
    await db.commit()
    return db_user

@app.get("/u/me", response_model=UserInDB)
async def read_users_me(current_user: UserModel = Depends(get_current_user)):
    return current_user

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await db.query(UserModel).filter(UserModel.user_login == username).first()
    if user is None:
        raise credentials_exception
    return user

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)