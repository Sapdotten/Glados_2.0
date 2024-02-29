import json

from models import User


def console_add_user():
    User.create(
        user_login=input('Enter user login: '),
        user_password=input('Enter hashed password: '),
        user_Last_name=input('Enter last name: '),
        user_first_name=input('Enter first name: '),
        user_patronymic=input('Enter patronymic: '),
        user_group_number=input('Enter group number: '),
        user_phone=input('Enter phone number: '),
        user_vk=input('Enter VK username: '),
        user_telegram=input('Enter Telegram username: '),
        user_email=input('Enter email: '),
        user_is_active=True
)

def console_get_all_user():
    return_user_query = []
    all_objects = User.select()
    for obj in all_objects:
        return_user_query.append(obj.__dict__['__data__'])
    ouput_data(return_user_query)
    return return_user_query 

def console_del_user():
    user_del_id = int(input('user ID to delete: '))
    query = User.delete().where(User.id == user_del_id)
    deleted_rows = query.execute()
    if deleted_rows:
        print(f"The record with ID {user_del_id} has been successfully deleted")
    else:
        print(f"The record with ID {user_del_id} was not found")


def console_get_user():
    user_get_id = int(input("Enter the user ID to get from the database: "))
    user = User.get_or_none(User.id == user_get_id)
    if user:
        ouput_data(user.__dict__)
    else:
        print(f"User with ID {user_get_id} not found")

def console_update_user():
    user_update_id = int(input('Введите ID пользователя для обновления: '))

    # Получение пользователя из базы данных по ID
    user = User.get_or_none(User.id == user_update_id)

    if user:
        user.user_login=input('Enter user login: '),
        user.user_password=input('Enter hashed password: '),
        user.user_Last_name=input('Enter last name: '),
        user.user_first_name=input('Enter first name: '),
        user.user_patronymic=input('Enter patronymic: '),
        user.user_group_number=input('Enter group number: '),
        user.user_phone=input('Enter phone number: '),
        user.user_vk=input('Enter VK username: '),
        user.user_telegram=input('Enter Telegram username: '),
        user.user_email=input('Enter email: '),
        user.user_is_active=True
        
        user.save()

        print(f"Данные пользователя с ID {user_update_id} успешно обновлены")
    else:
        print(f"Пользователь с ID {user_update_id} не найден")


def ouput_data(data):
    for el in data:
        print(json.dumps(el, indent=4, ensure_ascii=False))


