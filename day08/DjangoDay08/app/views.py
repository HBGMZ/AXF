from django.shortcuts import render

# Create your views here.
from app.models import News, Book


def index(request):

    news_list = News.objects.all()

    books = Book.objects.all()

    return render(request, 'index.html', context={'news_list':news_list, 'books':books})


def newsdetail(request, news_id):
    news = News.objects.get(pk=news_id)

    return render(request, 'newsdetail.html', context={'news':news})


def bookdetail(request, book_id):
    book = Book.objects.get(pk=book_id)

    return render(request, 'bookdetail.html', context={'book':book})