#비즈니스 로직 처리
from exception.duplicate_exception import DuplicateException
from exception.numnotfound_exception import NUMNotFoundException
from dao.file_dao import save_list, init_data_load

class TodoService:
    todos=[]  #클래스 변수  : 프로그램시작시 파일에서 todo객체 읽어서 한번 초기화
    
    #일정 등록 : list todos에 id중복체크하고 존재하지 않는 경우 정보 저장하고 message 리턴, 존재하는 경우 DuplicateException 발생
    def register(self,todo):
        todo.num+=1
        index = self.is_exist(todo.num)
        if index < 0 :
            TodoService.todos.append(todo)
            return "{0}(이)가 등록되었습니다.".format(todo.num)
        else :
            try:
                raise DuplicateException(str(todo.num))
            except DuplicateException as inputError:
                return str(inputError)

    #일정 목록 : list todos 목록 리턴
    def getAllTodo(self):
        return TodoService.todos

    #일정 수정 : num를 검색해서 내용을 수정하고 message 리턴, 존재하지 않는 경우 NUMNotFoundException 발생
    def update(self,num,title,content):
        index = self.is_exist(num)
        if index > -1 :
            TodoService.todos[index].title= title
            TodoService.todos[index].content= content
            return "{0} 내용으로 수정되었습니다.".format(content)
        else :
            try:
                raise NUMNotFoundException(str(num))
            except NUMNotFoundException as updateError:
                return str(updateError)

    #일정 삭제 :num를 검색해서 일정 삭제 message 리턴 존재하지 않는 경우 NUMNotFoundException 발생
    def remove(self,num) :
        index = self.is_exist(num)
        if index > -1 :
            TodoService.todos.pop(index)
            return "{0} 일정을 삭제했습니다.".format(num)
        else :
            try:
               raise NUMNotFoundException(num) 
            except NUMNotFoundException as removeError:
               return removeError

    #번호 존재여부 : num 검색해서 list todos의 index 값 리턴
    def is_exist(self,num):     
        for index, todo in enumerate(TodoService.todos):
            if todo.num == (num) :
                return index
        return -1

    #file read
    def file_read(self) :
        TodoService.todos = init_data_load()

    #file write
    def file_write(self) :
        save_list(TodoService.todos)
