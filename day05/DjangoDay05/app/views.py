from datetime import timedelta

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# HttpRequest
# request对象，是Django在客户端发起请求后，根据请求信息创建 request
from django.views.decorators.csrf import csrf_exempt

from app.models import User


# def index(request):
#     # 请求方法
#     print(request.method)
#
#     # 请求路径
#     print(request.path)
#
#     # print(request.META)
#
#     # get请求参数
#     print(request.GET)
#
#     # post请求参数
#     print(request.POST)
#
#     # 文件参数
#     print(request.FILES)
#
#     # cookie
#     print(request.COOKIES)
#
#     # session
#     print(request.session)
#
#     return render(request, 'index.html')


# 路径参数
# 127.0.0.1:8000/goods/4/
# 视图函数中，第一个参数必须是request，后续即路径参数(一一对应)
def goods(request, haha=1):
    temp = '第{}页 商品'.format(haha)

    return HttpResponse(temp)

def sum(request, a, b, c):
    temp = ' a:{} ,b:{} , c:{}'.format(a,b,c)
    return HttpResponse(temp)

def detail(request, name):
    temp = '{} 详情信息'.format(name)
    return HttpResponse(temp)


# get请求参数
def gettest(request):
    # QueryDict 类 字典
    # 使用这种方式，假如书写的key不存在，会抛出异常 【不建议使用】
    # name = request.GET['name']
    # age = request.GET['age']

    # 通过get方法获取 【推荐】
    name = request.GET.get('name')
    age = request.GET.get('age')
    score = request.GET.get('score')

    temp = '名字:{}, 年龄:{}, 成绩:{}'.format(name, age, score)

    return HttpResponse(temp)


# post请求参数
def postview(request):
    return render(request, 'postview.html')


@csrf_exempt
def posttet(request):
    username = request.POST.get('username')
    temp = '用户名:{}'.format(username)

    return HttpResponse(temp)



# 重定向
# 2xx 成功
# 3xx 重定向
# 4xx 客户端错误
# 5xx 服务端错误
def urltest(request):
    # return redirect('/')
    # return redirect('app:index')
    # return redirect('app:goodslist', 3)

    return HttpResponseRedirect('/')




####### 响应
# HttpResponse()
# render()
# HttpResponseRedirect()
# redirect()
# JsonResponse()

def jsontest(request):

    student = {
        'name': '张三',
        'age': 20
    }

    return JsonResponse(student)



###########################################

def index(request):
    # 获取cookies
    username = request.COOKIES.get('username')

    return render(request, 'index.html', context={'username':username})

def register(request):
    if request.method == 'GET': # 获取页面页面
        return render(request, 'register.html')
    elif request.method == 'POST':  # 注册操作
        # 注意1: 第一步先检查客户端是否能将 用户信息 传到 服务器

        # 注意2: 获取数据的字段，要保持一致
        # 获取参数
        username = request.POST.get('username')
        password = request.POST.get('password')
        tel = request.POST.get('tel')
        sex = request.POST.get('sex')
        # print(username, password, tel, sex)

        # 注意3: 检查确保数据 可以存入 到数据库
        # 存储到数据库
        try:
            user = User()
            user.username = username
            user.password = password
            user.tel = tel
            user.sex = sex
            user.save()

            # 传递 参数给 客户端 【response】
            # 要求: 回到首页
            response = redirect('app:index')

            #设置cookie
            response.set_cookie('username', user.username)

            # return HttpResponse('注册成功')
            return response
        except:
            return HttpResponse('注册失败(该用户已注册)')


def logout(request):

    # 重定向 首页
    response = redirect('app:index')

    # 删除cookie
    response.delete_cookie('username')

    return response


def login(request):
    if request.method == 'GET': # 获取登录页面
        return render(request, 'login.html')
    elif request.method == 'POST':  # 登录操作
        # 获取数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)

        # 验证
        users = User.objects.filter(username=username)
        if users.exists():  # 用户存在
            user = users.first()
            if user.password == password:   # 验证通过
                # 重定向 首页
                response = redirect('app:index')

                # 设置cookie
                # max_age=数值: 指定多少秒后过期
                # max_age=None: 浏览器关闭失效
                # expires过期时间: 指定过期时间
                # temp = timedelta(seconds=5)
                response.set_cookie('username', user.username,max_age=None)

                return response
            else:   # 密码错误
                return render(request, 'login.html', context={'p_err': '密码错误'})

        else:   # 用户不存在
            return render(request, 'login.html', context={'u_err': '用户不存在'})
