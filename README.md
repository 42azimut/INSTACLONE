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
  ### 1) 리눅스로 설치
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

  ### 1-1) 맥에서 설치 (homebrew 잘 안되는데... 그냥 앱으로 설치 해야 할듯!)
  ```
  #설치
  brew install postgresql

  #실행
  brew services start postgresql

  brew services restart postgresql

  # 슈퍼유저 접속 <<< 여기서 에러 >>>
  su - postgres

  #성공#
  psql -d postgres -U azimut_mac

  #데이터 베이스 생성
  create database instaclone;

  #확인
  \l

  # 슈퍼유저로 접속 
  su - azimut_mac

  # 유저네임으로 인스타클론 디비에 접속 
  psql -U azimut -d instaclone

  ```
  
  ### 2) 데이터 베이스 생성
  `create database instaclone`
  
  ### 3) 유저 생성 및 설정
  `create user ______(username) with password '____';`
  `create user azimut with password '1111';`
  
  #### (1) 유저 인코딩 utf-8
  `alter role (username) set client_encoding to 'utf-8';`

  #### (2) 서울 기준 시간
  `alter role (username) set timezone to Asia/Seoul';`
  
  #### (3) instaclone 이라는 database의 권한을 username에게 부여
  `grant all privileges on databases instaclone to (username);`
  
  #### (4) 인스타클론 이라는 데이터 베이스의 오너를 유저네임(aizmut) 으로 변경 명려어
  `ALTER DATABASE instaclone OWNER TO azimut;`
