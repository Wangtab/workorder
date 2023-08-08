from django.shortcuts import render, redirect
from app01 import models
from utils.pagination import Pagination
from utils.bootstrap import BootStrapModelForm


class TplModelForm(BootStrapModelForm):
    class Meta:
        model = models.Template
        fields = ['title', 'leader']


def tpl(request):
    if request.method == 'GET':
        # 创建form
        form = TplModelForm()
    else:
        # print(request.POST)
        form = TplModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            form = TplModelForm()  # 重新置零
    # 获取数据 + 分析
    queryset = models.Template.objects.all().order_by("-id")
    # 2.实例化分页对象
    page_object = Pagination(request, queryset)
    # print("page_object",page_object.html())
    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "pager_string": page_object.html(),  # 生成页码
        "form": form
    }
    print(page_object.page, page_object.html())
    return render(request, 'tpl.html', context)


def tpl_edit(request, pk):
    queryset = models.Template.objects.filter(id=pk).first()
    if request.method == "GET":
        form = TplModelForm(instance=queryset)
    else:
        form = TplModelForm(instance=queryset, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tpl/')

    # 获取数据 + 分析
    queryset = models.Template.objects.all().order_by("-id")
    # 2.实例化分页对象
    page_object = Pagination(request, queryset)
    # print("page_object",page_object.html())
    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "pager_string": page_object.html(),  # 生成页码
        "form": form
    }
    print(page_object.page, page_object.html())
    return render(request, 'tpl.html', context)


from django.http import JsonResponse


def tpl_delete(request, pk):
    try:
        models.Template.objects.filter(id=pk).delete()
        return JsonResponse({"status": True})
    except Exception as e:
        return JsonResponse({"status": False})
