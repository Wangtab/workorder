from django.shortcuts import redirect, render, HttpResponse


def up(request):
    return render(request, "up.html")
