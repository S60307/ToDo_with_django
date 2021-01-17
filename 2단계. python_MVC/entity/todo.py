class Todo:
    num=-1


    def __init__(self,title,content):
        Todo.num+=1
        self.title=title
        self.content=content

     #객체의 num가 같은 경우 True
    def __eq__(self, num) :
        if self.num == num :
            return True
        else : 
            return False

    #객체를 대표하는 문자열
    def __str__(self) :
        return "num:{0} 제목:{1} 내용:{2}".format(self.num,self.title,self.content)
    
