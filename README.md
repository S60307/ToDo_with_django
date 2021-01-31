## 개인 프로젝트
* Django를 이용한 MVC패턴의 웹 페이지 구축

  1)	1단계 : javascript를 이용하여 구현

  

  2)	2단계 : python을 이용하여 함수로 구현

  

  3)	3단계 : Django를 이용하여 MTV 패턴으로 구현

  

  4)	최종 : 위에 기술을 응용하여 운동경기 매칭 페이지 구축

  - 기능 : 로그인/회원가입, 일정 등록, 일정 신청

    - Model

      Todo(주소, 성별, 도시, 수준, 등록시간, 일정시간, 인원수, 등록 아이디)

    - Template

      main(base.html),

      Todo_app(create,detail,index,update.html), 

      Todo_customer(login,signup.html)

    - View

      Todo_app(index, detailTodo, createTodo, updateTodo, deleteTodo, applyTodo), Todo_customer(signup, login, logout)

​	

