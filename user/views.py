from lib2to3.pgen2 import driver
from ssl import AlertDescription
from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')

    elif request.method == 'POST':
        #읽어야할 데이터를 불러온다.
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        password2 = request.POST.get('password2',None)
        bio = request.POST.get('bio',None)

        
        
        if password != password2:
            return render(request, 'user/signup.html')

        else:
            exist_user = get_user_model().objects.filter(username = username)
            if exist_user:
                return render(request, "user/signup.html")
            else:
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in')
    


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        me = auth.authenticate(request, username=username, password=password)
            
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return redirect('/sign-in')

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def user_view(request):
    if request.method == 'GET':
        # 사용자를 불러오기, exclude와 request.user.username 를 사용해서 '로그인 한 사용자'를 제외하기
        user_list = UserModel.objects.all().exclude(username=request.user.username)
        #exclude = 해당하는 데이터에서 어떤 데이터를 빼겠다. 즉 나를 제외한 사용자 리스트
        return render(request, 'user/user_list.html', {'user_list': user_list})


@login_required
def user_follow(request, id):
    me = request.user
    click_user = UserModel.objects.get(id=id)
    #click_user = 내가 방금 누른 사람

    if me in click_user.followee.all():
        #그 사람을 팔로우 하는 모두 내가 팔로우를 했는지 안했는지

        click_user.followee.remove(request.user)
        #팔로우에 있다면 팔로우에서 지우기

    else:

        click_user.followee.add(request.user)
        #팔로우에 추가
    return redirect('/user')