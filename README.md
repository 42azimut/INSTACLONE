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

# 파일 확장자명을 분리해서 저장
  extenstion = filename.split('.')[-1]  
```
- 결과적으로 accoutns/username/random.확장자명 같은 파일 경로 문자열을 반환

## 007 accounts admin 
  1) admin. py 모델 등록
  2) admin 페이지 접속
  3) admin 유저 생성
  4) admin 페이지에서 객체 생성하기

### 1) admin.py 모델 등록
- 데코레이터를 이용해서 클래스 만듬
`@admin.register(Profile)`
- admin 관련해서 미리 정해진 옵션들이 저장된 것을 사용!
- 어떤 리스트 보여줄지 적는다!
- 닉네임을 통해 유저를 검색 할수 있는 검색창 만듬
`search_fields = 'nickname'`

### 2) admin 페이지 접속

### 3) admin 유저 생성
`python manage.py createsuperuser`
- run server again

### 4) admin 페이지에서 객체 생성하기
-클래스 이름은 Profile 단수형인데, 어드민 페이지에서는 "자동으로" 복수형 이다.

# 008 프론트엔드 협업

# 009 static: 프론트 엔드 예제파일업로드

# 010 template : 기본 layout

# 011  회원가입 | 로그인 | 로그아웃  **** 문서 오류 주의 특히 로그인 주소, 회원가입 주소 {% url 'accounts:login' %} ****
- url 짚고 넘어가기
- 만약 아래와 같이 패스 adm 라고 바꾸면 어떻게 될까?
```
urlpatterns = [
    path('adm/', admin.site.urls),
]
```
- 주소:8000/adm 으로 접속 된다! 설정을 여기서 달리 할수 있다!

### 1) config/urls.py

### 2) accounts/urls.py
- signup. login_checkout, logout 기능은 views.py 에서 정의! 함수명!
- accounts/signup 등 연결된다! 

### 3) accounts/views.py 
- views.py는 사용자가 url을 통해 접근했을때 구체적으로 어떤 일을 수행 하는지 명령하는 곳!
- authenticate 인증기능
- redirect 로그인 했을시 어떤 페이지로 보낼때
- render  template을 랜더링 하는 기능
- form을 정의해서 사용하기 때문에 따로 파일을 만들어서 불러온다!

### 4) 회원가입 함수, 로그인, 로그아웃 
```
# 함수형 뷰 : 회원가입
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:login')
    else:
        form = SignupForm()
    
    return render(request, 'accounts/signup.html', {
        'form':form,
        })
```
- 처음에 요청이 포스트 방식인지 확인! 
- 포스트 방식이면 forms.py에서 정의한 SignupForm을 가져오고, form 갑이 제대로 채워지면 저장! 
- 저장후 로그인 페이지로 리다이렉트(이동시킴)
- 포스트방식이 아니면, 회원가입 페이지를 다시 렌더링!

```
def login_check(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form':form}) 
```
- POST 요청으로 받은 계정과 비번을 가지고 유저인지 확인. 유저이면 로그인하고 루트url (/) 이동 >> redirect 아무것도 안쓰면 됨!
- 유저 아니면 로그인 페이지 다시 랜더링! 이때 폼 에러 메시지 담겨 있기 때문에 같이 렌더링!
- 만약 포스트 요청이 아니면 로그인 페이지를 렌더링!

- 로그아웃은 django_logout 시키면 끝! 그리고 루트로 이동!

### 5) forms 
- username 될수 있는 조건설정! 
- meta 클래스 추가. Meta는 SignupForm의 내부 클래스.
- fields 변수에 회원가입폼에서 보여줄 필드를 설정! 
- Meta 클래스를 이용하면 정렬옵션, 데이터베이스 테이블 이름등의 모델 단위의 옵션을 정할수 있다. 


# 012 메인 화면
```
1. post app 만들기
2. 포스트 모델 작성
3. 어드민 포스트 모델 등록
4. 디비에 모델 등록 확인
5. urls.py 수정
6. views.py
7. Template 작성
  1) layout.html 수정
8. post_list.html 작성
  1) layout 설정
```

## 1. post app 만들기
`python manage.py startapp post`

```
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = ProcessImageField(upload_to=photo_path, processors=[ResizeToFill(600, 600)],
                                formawt='JPEG',
                                options={'quality': 90})
    content = models.CharField(max_length=140, help_text="최대 140자 입력 가능")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
    
```
- 유저 모델 불러와서 author에 저장
- ProcessedImageField 기능 활용, 사진 저장 경로==photo_path 함수 사용
- 리사이즈, 콘텐츠 140 길이 제한, 등등
- Meta 생성 시간 기준으로 정렬

```
# post/models.py
def photo_path(instance, filename):
...
...

# post/admin.py

```


## 5 urls.py 수정
`path('post/', include('post.urls', namespace='post'))`
`path('', lambda r:redirect('post:post_list', name='root'))`
- 'post/' url 과 post 폴더의 ulrs.py 를 연결
- 그리고 루트 url로 접근할때도 post로 연결
- post 폴더에 urls.py 를 생성 및 작성

## 6. views.py




### 5. 이미지 미리 보기
- 자바스크립트로 구현
- cnavas 활용하여 미리 보기 구현
- html element 하나 가져온다. id_photo 라고 하는 id 값을 가진 요소를 가지고 온다. form.as_p 로 렌더링된 이미지 필드의 input 태그이다.
  - 장고 Form을 HTML에 렌더링 시 , 각  필드의 id값은 ##id_필드명## 형식으로 자동으로 추가 된다. 
  - 그래서 PostForm의 photo필드는 id_photo 라는 id 값을 가진 input 태그가 된다. 


# 013 좋아요

# 014 북마크

# 015 댓글
- 오타 p.256 post/templates/post/post_list.html 

# 016 팔로우 **주의**
- 프로필 모델은 accounts/models.py 애서 작업!!!
- Profile 모델에 ManyToManyField 사용!
- 오타 p261 : accounts/models.py 에서 작업 해야 함! 

# 017 히든메뉴_사이드 박스
- 오타 p272 : post/view.py 에서 리턴 'comment_form': comment_form 빠짐!


# 018 무한 스크롤
- p.281 : post_list를 posts 로 변경!!

# 019 태그 검색
