from django.shortcuts import redirect, render


def order(request):
    return render(request, "order.html")
