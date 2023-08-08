from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django import forms
from app01 import models


# 这里用form
class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", required=True)
    password = forms.CharField(label="密码", required=True, widget=forms.PasswordInput(render_value=True))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"
            field.widget.attrs['placeholder'] = "请输入{}".format(field.label)


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    form = LoginForm(data=request.POST)
    if not form.is_valid():
        return render(request, "login.html", {"form": form, })  # "error": '您的输入有误'

        # models.UserInfo.objects.create()
    # user_object = models.UserInfo.objects.filter(username='', password='1').first()
    user_object = models.UserInfo.objects.filter(**form.cleaned_data).first()
    print(user_object)
    if not user_object:
        return render(request, "login.html", {"form": form, "error": '用户名或密码错误'})
    # 如果用户名密码正确  保存session
    request.session['user_info'] = {"id": user_object.id, 'username': user_object.username, "role": user_object.role}
    # if form.cleaned_data:
    #     return HttpResponse('ok')
    print("session success")
    return redirect("/home/")


def logout(request):
    request.session.clear()
    return redirect('/login/')


def home(request):
    # return HttpResponse("home success")
    return render(request, "home.html")
