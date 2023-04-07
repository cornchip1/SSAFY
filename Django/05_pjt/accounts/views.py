from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from .forms import CustomUserCreationForm, CustomUserChangeForm

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if not request.user.is_authenticated:
        return redirect('movies:index')
    
    auth_logout(request)
    return redirect('movies:index')


# 문제 1. 회원 가입시 비밀번호가 일치하지 않을 때 발생하는 에러를 수정하시오.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    
    # 만약 비밀번호가 일치하지 않으면 기존 정보를 포함한 signup 페이지를 반환해야 한다
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

# 문제 3. 회원 탈퇴가 되지 않고 발생하는 에러를 해결하시오.
@require_POST
def delete(request):
    if not request.user.is_authenticated:
        return redirect('movies:index')
    
    # 로그아웃 후에는 verification 이 불가능해 delete이 안된다: 두 행의 순서 변경 필요
    request.user.delete()
    auth_logout(request)
    return redirect('movies:index')


@require_http_methods(['GET', 'POST'])
def update(request):
    if not request.user.is_authenticated:
        return redirect('movies:index')
    
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@require_http_methods(['GET', 'POST'])
def change_password(request):
    if not request.user.is_authenticated:
        return redirect('movies:index')
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)