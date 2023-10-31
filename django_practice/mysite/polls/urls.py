from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # '<>' <<-- dynamic variable // 여기서는 question_id가 해당
    # /polls/integer/ 로 접근할 경우
    path('<int:question_id>/', views.detail, name='detail'),
    # /polls/integer/results/ 로 접근할 경우
    path('<int:question_id>/results/', views.results, name='results'),
    # /polls/integer/vote/ 로 접근할 경우
    path('<int:question_id>/vote/', views.vote, name='vote')
]
