from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse("main index.")


# 개발자 도구의 network page에서 status code가 404인 것을 확인 가능
def error_404_view(request, exception):
    return HttpResponseNotFound('This page is not found.')

# django는 404 error와 같은 error처리에 대해서, 별도의 커스텀을 하지 않아도 HttpResponseNotFound(404), HttpResponseBadRequest
# 와 같이, status code에 따라 클래스가 이미 구현되어 있다.
