from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
from .models import *
from .domain.Response import R
from datetime import datetime
# Create your views here.
def delContact(request):
    if request.method == 'POST':
        body = request.body
        obj = json.loads(body)
        list = obj['data']
        for item in list:
            Contact.objects.filter(name=item).delete()
        return HttpResponse(R(200, "删除用户成功", {}))
    else:
        return HttpResponse(R(500, "服务器内部错误", {}))
def upadteContact(request):
    if request.method == 'POST':
        body = request.body
        obj = json.loads(body)
        Contact.objects.filter(name=obj['name']).update(sex=obj['sex'], tel=obj['tel'],birth=obj['birth'],address=obj['address'],specialize_id=obj['specialize_id'])
        return HttpResponse(R(200, "修改用户成功", {}))
    else: return HttpResponse(R(500, "服务器内部错误", {}))
def addContact(request):
    if request.method == 'POST':
        body = request.body
        obj = json.loads(body)
        Contact.objects.create(name=obj['name'], sex=obj['sex'], tel=obj['tel'],birth=obj['birth'],address=obj['address'],specialize_id=obj['specialize_id'])
        return HttpResponse(R(200, "增加用户成功", {}))
    else: return HttpResponse(R(500, "服务器内部错误", {}))

def getSpecialize(request):
    if request.method == 'GET':
        specialize = request.GET.get('specialize')
        print(specialize)
        obj = Specialize.objects.filter(specialize_name=specialize).values().first()
        return HttpResponse(R(200, "查询学院成功", { "academy": obj['academy_name'], "specialize_id": obj['specialize_id']}))
    else: HttpResponse(R(500, "服务器内部错误", {}))
def selectSpecialize(request):
    if request.method == 'GET':
        keyword = request.GET.get('keywords')
        contact_list = Specialize.objects.filter(specialize_name__contains=keyword).values()
        dict_contact = []
        for contact in contact_list:
            specialize_id = contact['specialize_id']
            x = Contact.objects.filter(specialize_id=specialize_id).values()
            for item in x:
                item['specialize'] = contact['specialize_name']
                item['academy'] = contact['academy_name']
                item['birth'] = item['birth'].strftime('%Y.%m.%d')
                dict_contact.append(item)
        return HttpResponse(R(200, "查询成功", dict_contact))
    else:
        return HttpResponse(R(500, "服务器内部错误", {}))
def selectAddress(request):
    if request.method == 'GET':
        keyword = request.GET.get('keywords')
        contact_list = Contact.objects.filter(address__contains=keyword).values()
        dict_contact = [precessHanle(x) for x in contact_list]
        return HttpResponse(R(200, "查询成功", dict_contact))
    else:
        return HttpResponse(R(500, "服务器内部错误", {}))
def selectName(request):
    if request.method == 'GET':
        keyword = request.GET.get('keywords')
        contact_list = Contact.objects.filter(name__contains=keyword).values()
        dict_contact = [precessHanle(x) for x in contact_list]
        return HttpResponse(R(200, "查询成功", dict_contact))
    else:
        return HttpResponse(R(500, "服务器内部错误", {}))
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(name=username)
        if user:
            pwd = user.values().first().get('password')
            if password == pwd:
                identity = user.values().first().get("identity")
                dict_data = {
                    "username" : username,
                    "identity" : identity
                }
                return HttpResponse(R(200, "登录成功", dict_data))
            else:
                return HttpResponse(R(404, "登录失败, 密码错误", {}))
        else:
            return HttpResponse(R(404, "登录失败, 未找到用户", {}))
    else:
        return HttpResponse(R(500, "服务器内部错误", {}))
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        tel = request.POST.get('tel')
        try:
            User.objects.create(name=username, password=password, tel=tel,identity="0")
            return HttpResponse(R(200, "注册成功", {}))
        except:
            return HttpResponse(R(500, "注册失败, 服务器内部错误",{}))
    else:
        return HttpResponse(R(500, "服务器内部错误", {}))
def getPermisson(request):
    if request.method == 'GET':
        username = request.GET.get("username")
        print(username)
        if username != None:
            identity = User.objects.filter(name=username).values().first().get("identity")
            return HttpResponse(R(200, "权限查询成功", {"identity": identity}))
        else :
            return HttpResponse(R(404, "用户名未找到", {}))
    else :
        return HttpResponse(R(500, "服务器内部错误", {}))
def main(request):
    if request.method == 'GET':
        contact_list = Contact.objects.all()[:15]
        dict_contact_list = [handle(i.to_json()) for i in contact_list]
        return HttpResponse(R(200, "响应成功", dict_contact_list))
    else:
        return HttpResponse(R(500, "服务器内部错误", {}))
def handle(x):
    specialize_id = x.get('specialize')
    qw = Specialize.objects.filter(specialize_id=specialize_id).values().first()
    x['birth'] = datehandle(x['birth'])
    x['specialize'] = qw['specialize_name']
    x['academy'] = qw['academy_name']
    return x
def datehandle(x):
    x = datetime.strptime(x, '%Y-%m-%d')
    return x.strftime('%Y.%m.%d')
def precessHanle(x):
    specialize_id = x['specialize_id']
    qw = Specialize.objects.filter(specialize_id=specialize_id).values().first()
    x['birth'] = x['birth'].strftime('%Y.%m.%d')
    x['specialize'] = qw['specialize_name']
    x['academy'] = qw['academy_name']
    return x
