from controller.controller import TodoController
from view.view import menu_dispay, menu_select, message_display
from view.view import input_display, update_display,delete_display


controller = TodoController()


controller.file_read()
while True:
    menu_dispay()

    menu = menu_select()
    if menu =="1" :
        todo = input_display()
        controller.register(todo)
       
    elif menu =="2" :
        controller.getAllTodo()

    elif menu =="3" :
        num, title ,content = update_display()
        controller.update(num,title ,content)
                   
    elif menu=="4" :
        num = delete_display()
        controller.remove(num)
      
    elif menu=="0" :
        message_display("일정 관리 프로그램을 종료합니다.")
        controller.file_write()
        break
    else :
        print()
        message_display("1,2,3,4,0 번 중 선택하세요" )
