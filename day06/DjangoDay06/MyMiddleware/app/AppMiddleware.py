from django.utils.deprecation import MiddlewareMixin
from DjangoDay06 import settings
from django.http import HttpResponse
import random
from app.models import User


class MyMiddle(MiddlewareMixin):
    # __init__ 服务器响应第一个请求时嗲用，检查中间是否生效
    # process_request() 在请求来的时候调用
    # process_view() 在视图函数之前调用
    # process_template_response() 模板渲染之前调用
    # process_response() 响应之前调用


    # def process_request(self, request):
    #   print(request.META['REMOTE_ADDR'])
    #    ip = request.META['REMOTE_ADDR']

    #    if ip in getattr(settings, 'BLOCKED_IPS', []):  # 阻拦
    #        return HttpResponse('<h1> 服务器繁忙，请稍后访问.... </h1>')

    def process_request(self, request):
        print(request.path)

        if request.path == '/lottery/':   # 是否为抽奖
            token = request.session.get('token')
            user = User.objects.get(token=token)

            if user.username == 'zyz':
                return HttpResponse('恭喜您 一等奖！ xxxxxxx')
            elif user.username == 'uu':
                return HttpResponse('恭喜您 二等奖！ xxxxxxx')

            temp = random.randrange(3,6)
            if temp == 3:
                return HttpResponse('恭喜您 三等奖！ xxxxxxx')
            elif temp == 4:
                return HttpResponse('恭喜您 鼓励奖！ xxxxxxx')
            elif temp == 5:
                return HttpResponse('谢谢参与(购买满100，可再获取抽奖机会)！ xxxxxxx')



