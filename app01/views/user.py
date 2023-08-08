from django.shortcuts import redirect, render


def user(request):
    return render(request, "user.html")


def add(request):
    return render(request, "add.html")


def edit(request):
    return render(request, "edit.html")
