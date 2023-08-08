from django.shortcuts import redirect, render
from django.http import JsonResponse
from app01 import models
from utils.pagination import Pagination
from utils.bootstrap import BootStrapModelForm
from datetime import datetime


class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        fields = ['tpl']


def my(request):
    form = OrderModelForm()
    queryset = models.Order.objects.filter(user=request.unicom_userid).order_by("-id")
    page_object = Pagination(request, queryset)
    # print("page_object",page_object.html())
    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "pager_string": page_object.html(),  # 生成页码
        "form": form
    }
    return render(request, "my.html", context)


def my_add(request):
    """创建工单"""
    if request.method == "GET":
        form = OrderModelForm()
        return render(request, "my_add.html", {"form": form})
    form = OrderModelForm(data=request.POST)
    if not form.is_valid():
        return render(request, "my_add.html", {"form": form})

    tpl_object = form.cleaned_data['tpl']
    form.instance.user_id = request.unicom_userid
    form.instance.leader_id = tpl_object.leader_id
    form.instance.create_datetime = datetime.now()
    form.save()
    return redirect("/my/")


def my_add_plus(request):
    """ajax提交并创建"""
    form = OrderModelForm(data=request.POST)
    if not form.is_valid():
        return JsonResponse({"status": False, "error": form.errors})

    tpl_object = form.cleaned_data['tpl']
    form.instance.user_id = request.unicom_userid
    form.instance.leader_id = tpl_object.leader_id
    form.instance.create_datetime = datetime.now()
    form.save()
    # return redirect("/my/")
    return JsonResponse({"status": True})
