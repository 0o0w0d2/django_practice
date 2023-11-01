# django_practice

## venv (virtualenv)

### git bash 이용

1. 가상환경 활성화 `source .venv/Scripts/activate`
2. 비활성화 `deactivate`

### requirements.txt

-> 다른 가상환경에서도 package를 쓰고 싶을 때, express에서 package.json과 같은 역할을 함.

1. pip 정보 업데이트 `python -m pip freeze > requirements.txt`
2. requirements.txt에 있는 packages 다운로드 `python -m pip install -r requirements.txt`

## django

### 프로젝트 만들기

`django-admin startproject [디렉토리명]`

### 개발 서버 시작

`python manage.py runserver (포트 번호)`

### 앱 만들기

`python manage.py startapp [디렉토리명]`

## redirect

1. Fully qualified URL (e.g. 'https://www.naver.com/')
2. absolute path with no domain (e.g. '/search/')
3. relative path (e.g. 'search/')
