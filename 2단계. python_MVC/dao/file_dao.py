import os.path
from entity.todo import Todo

#프로그램 종료시 list todos "todos.dat" 파일 저장
def save_list(todos) :
    save_file = open("todos.dat", "w")
    for index, todo in enumerate(todos) :
        save_file.write("{0}번째 | {1},{2},{3}\n".format(index,todo.num, todo.title, todo.content ))

    save_file.close()

#프로그램 시작시 "todos.dat" 파일이 존재하고 정보가 있는 경우  list todos초기화
def init_data_load() :
    todos=[]
    fileExist = os.path.isfile("todos.dat")
    if fileExist :
        read_file = open("todos.dat", "r")
        while True:
            data = read_file.readline()
            if len( data.split("|") )==2 :
                todo = data.split("|")[1].strip("\n").split(",")
                todos.append(Todo( todo[1].strip(), todo[2].strip() ))
            if not data:
                break
        read_file.close()
    return todos