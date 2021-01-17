from entity.todo import Todo

#menu display
def menu_dispay():
    print("====== 일정 관리 시스템 ======")
    print("1.일정 추가")
    print("2.일정 조회")
    print("3.일정 수정")
    print("4.일정 삭제")
    print("0.종료")

#menu select display
def menu_select():
    menu = input("메뉴를 선택하세요 : ")
    return menu

#message display
def message_display(message):
    print(message)


#list display
def list_display(todos) :
    print("==== 일정 목록 ====")
    for todo in todos :
        print(todo)      #Todo 재정의한 __str__

#Todo input display
def input_display():
    title = input("제목 : ")
    content = input("내용 :" )

    return Todo(title,content)

#update input display
def update_display():
    num = int(input("수정할 번호 : "))
    title=input("수정할 제목 :" )
    content = input("수정할 내용 :" )

    return num,title,content


#delete input dispaly
def delete_display():
    num = int(input("삭제할 일정 번호 : "))
    return num