from django.template import Library
from django.conf import settings
import copy

register = Library()


@register.inclusion_tag("menu.html")
def unicom_menu(request):
    # 当前是什么角色
    role = request.unicom_role
    # 去setting中获取所有的菜单信息
    user_menu_list = copy.deepcopy(settings.UNICOM_MENU[role])
    for row in user_menu_list:
        # if row['url'] == request.path_info:
        if request.path_info.startswith(row['url']):
            row['class'] = 'active'
    return {"menu_list": user_menu_list}
