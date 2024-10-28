from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def top(request):
    return HttpResponse(b"Hello World")


def catche_new(request):
    return HttpResponse('釣果の登録')


def catche_edit(request, catche_id):
    return HttpResponse('釣果の編集')


def catche_detail(request, catche_id):
    return HttpResponse('釣果の詳細閲覧')