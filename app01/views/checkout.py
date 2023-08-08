from django.shortcuts import redirect, render, HttpResponse
from app01 import models
from utils.pagination import Pagination

def checkout(request):
    # 查询当前待审批的数量
    count = models.Order.objects.filter(status=1, leader=request.unicom_userid).count()
    # 查询自己待审批的工单
    queryset = models.Order.objects.filter(leader=request.unicom_userid).order_by('status',"-id")
    page_object = Pagination(request, queryset)
    # print("page_object",page_object.html())
    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "pager_string": page_object.html(),  # 生成页码
        # "form": form
        'count': count
    }
    return render(request, "checkout.html", context)


def checkout_action(request, action, oid):
    if action not in [1, 2]:
        return HttpResponse("请求错误")
    import datetime
    ctime = datetime.datetime.now()
    if action == 1:
        models.Order.objects.filter(id=oid, status=1, leader_id=request.unicom_userid).update(status=2,update_datetime=ctime)
        return redirect('/checkout/')
    else:
        models.Order.objects.filter(id=oid, status=1, leader_id=request.unicom_userid).update(status=3,update_datetime=ctime)
        return redirect('/checkout/')
