# instaclone 

## 01. 설치 및 일반
1) Frontend
2) Backend / Django

4) virtualenv 가상환경 세팅
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

5) 필요 패키지 설치
`pip install -r requirements.txt`

6) migrate
`python manage.py migrate`

7) 서버실행
`python manage.py runserver`
___
## 03. 장고 프로젝트 만들기
  1) pip 를 이용해 장고3.1버전 설치
  `pip3 install django--3.1`

  2) 설정파일이 들어 잇는 폴더 생성하면서 프로젝트 생성. (점)은 현재 폴더에 프로젝트를 생성 의미!
  3) `django-admin startproject config .`
___
## 04. PostgreSQL  
  1) 설치
  ```
  # apt-get 업댓
  apt-get update
  
  # 설치
  apt-get install postgresql
  
  #실행
  service postgresql start
  
  #작동확인
  ps -ef|grep postgres
  
  # 접속(슈퍼유저)
  su - postgres
  ```
  
  2) 데이터 베이스 생성
  `create database instaclone`
  
  
