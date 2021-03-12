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


  ## 3. 장고에 PostgreSQL 연결
  - 한번에 설치

  `pip install pillow pilkit psycopg2-binary django-imagekit`

  ```
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'instaclone',
        'USER': 'azimut',
        'PASSWORD': '1111',
        'HOST': 'localhost',
        'PORT': '',
  ```
___

## 005 accounts 앱 생성

```
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'config' / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media'
MEDIA_ROOT = BASE_DIR / 'media'
LOGIN_REDIRECT_URL = '/'
```

## 006 accoutns 앱 모델 생성
- 모델 작성 순서
  1) 패키지 설치
  2) 모델 작성
    (1) model.py 
    (2) Profile 모델 작성(모델 상속)
    (3) User, nickname, about, gender, picture 필드
  3) migrate

### 1) models.py
- import 여러개

### 2) Profile 모델 작성
- 사용자 정보 프로필 클래스 만든다. models.Model 을 상속 받아서 만듬! 이게 디비 태이블이 된다!

`class Profile(models.Model):`

### 3) user 필드
- 1:1 관계필드
- settings.AUTH_USER_MODEL 을 활용. 현재 인증으로 사용하는 유저모델이 설정
- 기본값으로 장고에서는 내장 auth 앱의 User 모델을 사용
- 유저 정보 삭제시 관련정보 함께 삭제. on_delete....

### 4) nickname 필드
- 최대 20자
- 각자 고유별명 가지도록 unique 속성 true 
- 그리고 프로필 객체들을 표현할때 닉네임을 사용하도록 설정
```
def __str__(self):
        return self.nickname
    
```

### 5) about 필드
- black 가능 

### 6) gender 필드
- GENDER_C = 성별 선택박스 Select Box 작성
```
GENDER_C = (
        ('선택암함', '선택안함'),
        ('여성', '여성'),
        ('남성', '남성'),
    )
```
- (A, B) 일때, 왼족 A는 디비에 저장되는 값, 오른쪽 B는 유저에게 보이는 값!
- gender 핖드 만들고, GENDER_C 를 choices 항목의 값을 넣어줍니다.
ㅡ choices 미리 정해진 이름, 틀리면 오류

### 7) picture 필드
- 이미지 처리 추가. 임포트 한 ProcessedImageField 사용
- upload_to 라는 항목은 저장 위치 처리. 포스트, 글 작성 구현 할떄도 똑같사용! 하면 활용 굳!!!!
- user_path 함수 : 사용자가 업로드 한 이미지 파일 경로를 생성하여 반환 하는 함수!
- instance는 Photo의 모델이고 filename은 사용자의 파일명. random선택을 한느 choice 기능과 string 기능 가져옴! 
```
# 대소문자 관계없이 8번 반복하여 문자를 불러 오게 한다
  arr = [choice(string.ascii_letters) for _ in range(8)]

# 이어 붙이기
    pid = ''.join(arr)
```