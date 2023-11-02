from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    # # trigger 500 error
    # pass
    # return HttpResponse('main index!')
    return render(request, 'main.html')


# 개발자 도구의 network page에서 status code가 404인 것을 확인 가능
# django는 404 error와 같은 error처리에 대해서, 별도의 커스텀을 하지 않아도 HttpResponseNotFound(404), HttpResponseBadRequest
# 와 같이, status code에 따라 클래스가 이미 구현되어 있다.

# 아래의 두 함수를 추가하지 않아도 자동으로 인식하지만, urls.py에서 함수를 불러왔으므로 추가함.
# README의 Template - Error templates - 1 참고
def error_404_view(request, exception):
    # return HttpResponseNotFound('This page is not found.')
    return render(request, '404.html')

def error_500_view(request):
    return render(request, '500.html')