#encoding=utf-8

from urllib.parse import urljoin
import pytz
import json
import time

from django.conf import settings
from django import template
from django.contrib.contenttypes.models import ContentType
from decimal import Decimal

register = template.Library()


@register.filter(name='hdatetime')
def repr_datetime(value) -> str:
    if not value:
        return ''
    tz = pytz.timezone(settings.TIME_ZONE)
    return value.astimezone(tz).strftime('%Y-%m-%d %H:%M:%S')


@register.filter(name='hdate')
def repr_date(value):
    if not value:
        return ''
    tz = pytz.timezone(settings.TIME_ZONE)
    return value.astimezone(tz).strftime("%Y-%m-%d")


@register.filter(name='hdatemin')
def repr_datemin(value):
    if not value:
        return ''
    else:
        loc_time = time.localtime(int(value))
        return time.strftime("%Y-%m-%d %H:%M", loc_time)


@register.filter(name='keep_two_decimal_places')
def ktd_places(value):
    if not value:
        return "0"
    dec_value = Decimal(value).quantize(Decimal("0.00"))
    return dec_value.to_integral() if dec_value == dec_value.to_integral() else dec_value.normalize()


@register.filter(name='decimal_remove_zero')
def remove_zero(value):
    if not value:
        return "0"
    return value.to_integral() if value == value.to_integral() else value.normalize()


@register.filter(name='mem_type')
def mem_type(type):
    return {
        'CoreMember': '核心成员',
        'CommonMember': '普通成员',
        'PartTimeMember': '线下推广员',
    }.get(type, '')


@register.filter(name='mem_status')
def mem_status(status):
    return {
        'YES': '无效成员',
        'NO': '有效成员',
    }.get(status, '')


@register.filter(name='approve_status')
def approve_status(approve):
    return {
        'UnApproved': '未申请',
        'Approving': '申请中',
        'Approved': '审批通过',
        'Payment':'已支付',
        'Rejected': '已拒绝'
    }.get(approve, '')


@register.filter(name='sex_choice')
def sex_choice(sex):
    return {
        'Male': '女',
        'Female': '男',
    }.get(sex, '')