import hashlib
import random
import time

from django.shortcuts import render, redirect

# Create your views here.
from axf.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtype, Goods, User


def home(request):
    wheels=Wheel.objects.all()
    navs=Nav.objects.all()
    mustbuys=Mustbuy.objects.all()
    shops=Shop.objects.all()
    shophead=shops[0]
    shoptabs=shops[1:3]
    shopclass_list=shops[3:7]
    shopcommends=shops[7:11]
    mainshows=Mainshow.objects.all()
    data={
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shophead':shophead,
        'shoptabs':shoptabs,
        'shopclass_list':shopclass_list,
        'shopcommends':shopcommends,
        'mainshows':mainshows
    }


    return render(request,'home/home.html' ,context=data)


def market(request,childid='0',sortid='0'):
    foodtypes=Foodtype.objects.all()

    # goods_list=Goods.objects.all()[0:5]
    # goods_list = Goods.objects.filter(categoryid=categoryid)
    index=int(request.COOKIES.get('index','0'))
    categoryid=foodtypes[index].typeid

    if childid == '0':
        goods_list = Goods.objects.filter(categoryid=categoryid)
    else:
        goods_list = Goods.objects.filter(categoryid=categoryid).filter(childcid=childid)

    if sortid == '1':
        goods_list = goods_list.order_by('-productnum')
    elif sortid == '2':
        goods_list = goods_list.order_by('price')
    elif sortid == '3':
        goods_list = goods_list.order_by('-price')

    # if childid == '0':
    #     goods_list = Goods.objects.filter(categoryid=categoryid)
    # else:
    #     goods_list = Goods.objects.filter(categoryid=categoryid).filter(childcid=childid)

    # goods_list=Goods.objects.filter(categoryid=categoryid)


    childtypenames=foodtypes[index].childtypenames
    childtype_list=[]
    for item in childtypenames.split('#'):
        item_arr=item.split(':')
        temp_dir={
            'name':item_arr[0],
            'id':item_arr[1]
        }
        childtype_list.append(temp_dir)
    response_dir = {
        'foodtypes': foodtypes,
        'goods_list': goods_list,
        'childtype_list':childtype_list,
        'childid': childid
    }
    return render(request,'market/market.html',context=response_dir)


def mine(request):

    token=request.session.get('token')
    user=None
    if token:
        user=User.objects.get(token=token)



    return render(request,'mine/mine.html',context={'user':user})


def cart(request):
    return render(request,'cart/cart.html')


def generate_token():
    token = str(time.time()) + str(random.random())
    md5 = hashlib.md5()
    md5.update(token.encode('utf-8'))

    return md5.hexdigest()


def generate_password(param):
    md5 = hashlib.md5()
    md5.update(param.encode('utf-8'))
    return md5.hexdigest()


def register(request):
    if request.method == "GET":
        return render(request, 'mine/register.html')
    elif request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        name=request.POST.get('name')
        token=generate_token()
        try:
            user=User()
            user.email=email
            user.password=generate_password(password)
            user.name=name
            user.token=token
            user.save()
            response=redirect('axf:mine')
            request.session['token']=user.token

            return response
        except:
            return render(request,'mine/register.html')


def login(request):
    if request.method=='GET':
        return render(request,'mine/login.html')
    elif request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        users=User.objects.filter(name=name).filter(password=password)
        if users.exists():
            user=users.first()
            user.token=generate_token()

            user.save()
            request.session['token']=user.token

            return  redirect('axf:mine')
        else:
            return  render(request,'mine/login.html')

def logout(request):
    request.session.flush()
    return redirect('axf:mine')