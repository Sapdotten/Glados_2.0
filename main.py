from modules.UserLogicApp import(
                                    console_add_user, 
                                    console_get_all_user, 
                                    console_del_user, 
                                    console_get_user, 
                                    console_update_user
                                )
from models import files


def show_menu():
    menu =  """
        Console API
        ::User API::
        1.1) add User
        1.2) del User
        1.3) get User
        1.4) list User
        1.5) update User
          ::DOC API::
        2.1) add doc
        2.5) add doc with parametrs  
        2.2) del doc
        2.2) get doc id 
        2.3) get doc all
        2.4) get doc with filter

        
        *) Update table
        **) Drop table 
        ***) Create table

        
        exit - exit || quit - exit
        """
    print(menu)



def user_choose():
    choose = input("--> ")
    match choose:
        case "1.1": console_add_user()
        case "1.2": console_del_user()
        case "1.3": console_get_user()
        case "1.4": console_get_all_user()
        case "1.5": console_update_user()

        case "*": ...
        case "**": ...
        case "***": ...

        case "exit": return quit()
        case "quit": return quit()

def console_thread_commands():
    while True:
        show_menu()
        user_choose()

def main():
    console_thread_commands()


if __name__ == '__main__':
    main()


