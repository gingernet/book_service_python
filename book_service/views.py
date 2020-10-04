#encoding=utf-8
import logging
import xlrd
import time
import random
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from book_service.models import BookUser
from common.helpers import ok_json, paged_items


LOGIN_URL = '/create_user/'


def random_email( emailType=None, rang=None):
    __emailtype = ["@qq.com", "@163.com", "@126.com", "@189.com"]
    if emailType == None:
        __randomEmail = random.choice(__emailtype)
    else:
        __randomEmail = emailType
    if rang == None:
        __rang = random.randint(4, 16)
    else:
        __rang = int(rang)
    __Number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
    __randomNumber = "".join(random.choice(__Number) for i in range(__rang))
    _email = __randomNumber + __randomEmail
    return _email


def gen_datetime():
    sart_time = (1990, 1, 1, 0, 0, 0, 0, 0, 0)
    end_time = (2020, 10, 9, 23, 59, 59, 0, 0, 0)
    start = time.mktime(sart_time)
    end = time.mktime(end_time)
    date = None
    for i in range(10):
        t = random.randint(start, end)
        date_touple = time.localtime(t)
        date = time.strftime("%Y-%m-%d %H:%M:%S", date_touple)
    return date

def create_user(request):
    if request.method == "GET":
        return render(request, 'backoffice/user/create_user.html', locals())
    elif request.method == "POST":
        file = request.FILES.get('fileContent')
        data = xlrd.open_workbook(
            filename=None, file_contents=file.read())
        table = data.sheets()[0]
        row = table.nrows
        for i in range(1, row):
            col = table.row_values(i)
            BookUser.objects.create(
                name=random_email(),
                phone=int(col[0]),
                created_time=gen_datetime()
            )
    return render(request, 'backoffice/user/create_user.html', locals())


@login_required
def backend_logout(request):
    logout(request)
    return redirect('/admin/')


@login_required
def user_list(request):
    user_lists = BookUser.objects.all()
    user_lists = user_lists.order_by('-created_time')
    user_lists = paged_items(request, user_lists)
    return render(request, 'backoffice/user/user_list.html', locals())


