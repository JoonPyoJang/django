from django.http import HttpResponse
from django.shortcuts import render


def base_response(request):
    return HttpResponse("안녕하세요! 장고의 시작입니다!")

# HttpResponse()는 괄호 안에 있는 내용을 인터넷 창 화면에 보여주는 역할을 합니다! 

def fisrt_view(request):
    return render(request, 'test.html')

def test(request):
    return render(request, 'base.html')