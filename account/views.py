from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect("youareright: main")
        else:
            return redirect(request, "login")
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})


def logout(request):
    auth.logout(request)
    return redirect("youareright: main")


# 회원가입 함수
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect("youareright: main")
        else:
            return redirect(request, "signup")
    else:
        form = UserCreationForm()
        return render(request, "signup.html", {"form": form})
