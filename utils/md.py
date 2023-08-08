from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, HttpResponse
from django.conf import settings


# from django.contrib.auth.middleware.AuthenticationMiddleware


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 对于无需登录的网页放行
        path = request.path_info
        # if path == '/login/':
        #     return
        if request.path_info in ['/login/', '/logout/']:
            return
        info = request.session.get('user_info')
        if info:
            request.unicom_userid = info['id']
            request.unicom_username = info['username']
            request.unicom_role = info['role']
            return

        return redirect('/login/')

    def process_view(self, request, view_func, args, kwargs):
        if request.path_info in ['/login/', '/logout/']:
            return
        # 当前用户的角色
        role = request.unicom_role

        # 自己具备的权限
        user_permission_list = settings.UNICOM_PERMISSION[role]
        # 自己是否具有权限
        print("*****request.resolver_match.url_name：", request.resolver_match)
        if request.resolver_match.url_name in user_permission_list:
            return
        # 无权限
        return HttpResponse("无权限")
