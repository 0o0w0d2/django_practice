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

## Template

### variables

- {{ <variable> }}

### filters

- {{ <variable>|<filter> }}
- lower, upper
- length
- date: "D d M Y"
- escape
- https://docs.djangoproject.com/ko/4.2/ref/templates/builtins/#ref-templates-builtins-filters
- https://www.djangotemplatetagsandfilters.com/

### tags

- {% <Command> %}
- for .. in .. endfor
- if .. elif .. else .. endif
  - ==, !=, >=, <=, >, <
  - and, or, in, not in, is, is not
- block & extends

### Error Templates

1. django의 경우 urls.py에 handler404, handler500 등 error function을 추가하지 않더라도(별도의 코드를 추가하지 않더라도), project의 templates 디렉토리에 있는 404.html, 500.html 등을 자동으로 사용함.

- 코드를 추가하면 views.py에서 exception에 대한 정보를 얻을 수 있음

2. settings.py의 `DEBUG = True`인 상태에서는 오류의 세부 정보가 표시되는데, 이는 오류를 디버그하고 해결하는데 도움이 되지만(개발 단계), 운영을 할 경우에 사용자에게 세부 정보를 노출시키지 않기 위해서 `DEBUG = False`로 변경하고, 오류 페이지를 사용자 정의해야 함.

## Model

1. models.py 작성
2. `python manage.py makemigrations` -> 테이블을 어떤식으로 만들건지에 대한 파일 생성?
3. `python manage.py migrate` => table 만들기

### shell

$ python manage.py shell

> > > from polls.models import Choice, Question # Choice, Question table 불러오기

> > > Question.objects.all() # Question table 안의 내용 보여줘
> > > <QuerySet []> # 아직 아무 자료도 X
> > > from django.utils import timezone # import timezone modules
> > > q = Question(question_text="What's new?", pub_date=timezone.now())
> > > q.save() # 저장해야 저장이 됨
> > > Question.objects.all()
> > > <QuerySet [<Question: Question object (1)>]>
> > > q.question_text
> > > "What's new?"
> > > q.pub_date
> > > datetime.datetime(2023, 11, 7, 18, 24, 4, 222615, tzinfo=datetime.timezone.utc)
> > > q.question_text = "What's up?"
> > > q.save()
> > > q.question_text
> > > "What's up?"
