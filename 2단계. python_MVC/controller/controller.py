#입력데이터 valid 체크, service에 비즈니스 로직 호출, data 저장, view(template) 선택
from service.todo_service import TodoService
from view.view import message_display,list_display

class TodoController :

    def register(self, todo) :
        service = TodoService()
        message = service.register(todo)  #비즈니스 메서드 호출 
        message_display(message)   #View select

    def getAllTodo(self):
        service = TodoService() 
        todos = service.getAllTodo() #비즈니스 메서드 호출
        list_display(todos)   #데이터 저장해서 view select

    def update(self, num, title,content) :
        #num, content valid check
        if title==""or content=="" : 
            message_display("제목과 내용을 입력하세요.")
        service = TodoService()
        message = service.update(num,title ,content)
        message_display(message)        

    def remove(self, num) :
        if id == "" :
             message_display("삭제할 num을 입력하세요.")
        service = TodoService()
        message = service.remove(num)
        message_display(message)

    def file_read(self):
        service = TodoService()
        service.file_read()

    def file_write(self):
        service = TodoService()
        service.file_write()


