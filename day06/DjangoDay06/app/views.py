import hashlib
import os
import random
import time
import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from DjangoDay06 import settings
from app.models import User


def index(request):
    # 状态保持 cookie
    # username = request.COOKIES.get('username')

    # 状态保持 session
    # username = request.session.get('username')

    # 状态保持 token
    token = request.session.get('token')
    print(token)
    user = None
    if token:
        user = User.objects.get(token=token)

    return render(request, 'index.html', context={'user':user})


def errtest(request):

    print(a)

    return HttpResponse('错误测试')


# token生成
# token 唯一标识
def generate_token():
    # 时间戳
    # 时间戳 + 随机数
    # 时间戳 + 随机数 + IP
    # 时间戳 + 随机数 +公司域名

    token = str(time.time()) + str(random.random())
    md5 = hashlib.md5()
    md5.update(token.encode('utf-8'))

    return md5.hexdigest()


def generate_password(param):
    md5 = hashlib.md5()
    md5.update(param.encode('utf-8'))
    return md5.hexdigest()


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        user = User()
        user.username = request.POST.get('username')
        user.password = generate_password(request.POST.get('password'))
        user.tel = request.POST.get('tel')

        # hex 为了生成纯数字、字母长串 (否则是都有 '-')
        user.token = generate_token()

        # UUID 通用唯一标识符
        # uuid.uuid1()  基于时间戳、Mac地址、随机数　[不建议使用]
        # uuid.uuid2()  基于分布 [Ｐｙｔｈｏｎ中没有]
        # uuid.uuid3(namespace, name)  基于名字MD5离散值 [推荐]
        # uuid.uuid4()  基于随机数 [不建议使用]
        # uuid.uuid5()  基于sha-1离散值 [推荐]

        user.save()

        response = redirect('app:index')

        # 状态保持 cookie
        # response.set_cookie('username', user.username)

        # 状态保持 session
        # BASE64编码解码     https://base64.supfree.net/
        #  session_data >>>>>  df60e3492035dc09255ba8d4c2e8a0661ca28a20:{"username":"zyz"}
        # request.session['username'] = user.username

        # session 设置过期时间
        # request.session.set_expiry(10)


        # 状态保持 token
        request.session['token'] = user.token

        return response


def logout(request):
    response = redirect('app:index')

    # 方式一
    # del request.session['username']

    # 方式二 [session依赖于cookie]
    # response.delete_cookie('sessionid')

    # 方式三 同时清除cookie和session
    request.session.flush()

    return response


def login(request):
    if request.method == 'GET':
        return render(request , 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = generate_password(request.POST.get('password'))

        users = User.objects.filter(username=username).filter(password=password)
        if users.exists():
            # 状态保持
            user = users.first()
            user.token = generate_token()   # 更新token
            user.save()

            request.session['token'] = user.token
            return redirect('app:index')
        else:
            return redirect('app:login')

def lottery(request):

    return HttpResponse('抽奖')



def upfile(request):
    if request.method == 'GET':
        return render(request, 'upfile.html')
    elif request.method == 'POST':
        # 获取图片
        headimg = request.FILES.get('headimg')

        # 图片名字(避免图片名冲突)
        filename = str(int(time.time())) + '-' + headimg.name

        # 文件路径
        filepath = os.path.join(settings.MEDIA_ROOT, filename)

        #文件读写
        with open(filepath, 'wb') as fp:
            for item in headimg.chunks():
                fp.write(item)

        # 更新数据库信息
        token = request.session.get('token')
        user = User.objects.get(token=token)
        user.icon = filename
        user.save()

        return redirect('app:index')