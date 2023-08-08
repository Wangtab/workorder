from django.shortcuts import redirect, render


def work(request):
    return render(request, "work.html")
