# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from re import match

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *

# Create your views here.
# 客户信息
def customer_list1(request):
    customerinfo = CustomerInfo.objects.all()
    return render(request, 'customer_list1.html', {'customerinfo': customerinfo})


 # 客户信息编辑
def customer_edit(request):
    jj = request.GET.get('jj', '')
    print jj
    jj = int(jj)
    customerinfo = CustomerInfo.objects.get(customer_id=jj)
    # user = request.POST.get('customerForUser')
    # user_name = UserInfo.objects.filter(user_id=jj).update(user_name=user)
    # qq = request.POST.get('customerQq')
    # customer_qq = UserInfo.objects.filter(customer_id=jj).update(customer_qq=qq)
    return render(request,'customer_edit.html')


# 客户详情
def customer_detail(request):
    customer_detail = request.GET.get('customer_detail', '')
    customer_detail = int(customer_detail)
    customerinfo = CustomerInfo.objects.get(customer_id=customer_detail)
    return render(request, 'customer_detail.html', {'customerinfo': customerinfo})
# 客户删除
def customer_dele(request):
    dele = request.GET.get('dele', '')
    dele = int(dele)
    delet = CustomerInfo.objects.get(customer_id=dele).delete()
    return HttpResponseRedirect('/client/customer_list1.html/')
# 查询客户信息
def index_customer(request):
    content = request.GET.get('customerInput')

    queryType = request.GET.get('queryType')
    # 按顾客信息查询
    if queryType == '1':
        customerinfo = CustomerInfo.objects.all()
        customerinfo = CustomerInfo.objects.filter(customer_name__contains=content)
        return render(request, 'customer_list1.html', {'customerinfo': customerinfo})
    elif queryType == '2':
        customerinfo = CustomerStatus.objects.get(status_name=content).customerinfo_set.all()
    #     # condition = CustomerCondition.objects.get(condition_name=content).condition_id
    #     # condition = int(condition)
    #     # cus = CustomerInfo.objects.filter(condition_id=condition)
        return render(request, 'customer_list1.html', {"customerinfo": customerinfo})
    elif queryType == '3':
        customerinfo = CustomerSource.objects.get(source_name=content).customerinfo_set.all()
        return render(request, 'customer_list1.html', {"customerinfo": customerinfo})
    elif queryType == '4':
        customerinfo = CustomerType.objects.get(type_name=content).customerinfo_set.all()
    #     cus = CustomerType.objects.get(type_name=content).type_id
    #     print cus
    #     cusi = int(cus)
    #     cus = CustomerInfo.objects.filter(type_id=cusi)
        return render(request, 'customer_list1.html', {"customerinfo": customerinfo})
    elif queryType == '5':
        customerinfo = UserInfo.objects.get(user_name=content).customerinfo_set.all()
        return render(request, 'customer_list1.html', {"customerinfo": customerinfo})
    elif queryType == '6':
        customerinfo = CustomerInfo.objects.filter(customer_company=content)
        return render(request, 'customer_list1.html', {"customerinfo": customerinfo})
    # return render(request,'c_c_information.html')
# 添加客户信息
def customer_add(request):
    if request.method == 'GET':
        return render(request, 'customer_add.html')
    else:

        customer_name = request.POST.get('customerName', '')
        customerJob = request.POST.get('customerJob', '')
        customer_sex = request.POST.get('customerSex', '')
        birth_day = request.POST.get('customerBirthday', '')
        customer_mobile = request.POST.get('customerMobile', '')
        customer_address = request.POST.get('customerAddress', '')
        customer_addman = request.POST.get('customerAddMan', '')
        customer_mobile = request.POST.get('customerTel', '')
        customer_company = request.POST.get('customerCompany', '')
        cust = request.POST.get('customerSource')
        source_name = CustomerSource.objects.get(source_name=cust)
        customerType = request.POST.get('customerType')
        type_name = CustomerType.objects.get(type_name=customerType)
        customer_email = request.POST.get('customerEmail')
        customerCondition = request.POST.get('customerCondition')
        condition = CustomerStatus.objects.get(status_name=customerCondition)
        customer_qq = request.POST.get('customerQq')
        change_man = request.POST.get('customerChangeMan')
        customer_blog = request.POST.get('customerBlog')
        customer_msn = request.POST.get('customerMsn')
        customer_remark = request.POST.get('customerRemark')
        try:
            ci = CustomerInfo.objects.get(customer_name=customer_name)
        except:
            ci = CustomerInfo.objects.create(customer_name=customer_name,
                                             customer_job=customerJob,
                                             customer_sex=customer_sex,
                                             customer_mobile=customer_mobile,
                                             customer_address=customer_address,
                                             type=type_name,
                                             customer_addman=customer_addman,
                                             customer_company=customer_company,
                                             source=source_name,
                                             birth_day=birth_day,
                                             customer_email=customer_email,
                                             status=condition,
                                             customer_qq=customer_qq,
                                             change_man=change_man,
                                             customer_blog=customer_blog,
                                             customer_msn=customer_msn,
                                             customer_remark=customer_remark
                                             )

            return HttpResponseRedirect('/client/customer_list1.html/')


# 客户分配信息目录
def customer_distribute_list(request):
    cust_dist_list = CustomerLinkreord.objects.all()
    return render(request, 'customer_distribute_list.html',{'cust_dist_list':cust_dist_list})

# 分配所选客户信息
def customer_distribute(request):
    return render(request, 'customer_distribute.html')


# 客户关怀信息目录
def customer_care_list(request):
    cust_care_list = CustomerCare.objects.all()
    return render(request, 'customer_care_list.html', {'cust_care_list':cust_care_list})


def customer_care_edit(request):
    return render(request, 'customer_edit.html')
# 客户类型信息目录
def customer_type_list(request):
    cust_type_list = CustomerType.objects.all()
    return render(request, 'customer_type_list.html',{'cust_type_list':cust_type_list})

# 客户状态信息目录
def customer_state_list(request):
    cust_stat_list = CustomerStatus.objects.all()
    return render(request, 'customer_state_list.html',{'cust_stat_list': cust_stat_list})

# 客户来源信息目录
def customer_source_list(request):
    cust_source_list = CustomerSource.objects.all()
    cust_source_list_del = CustomerSource .objects.filter()
    return render(request, 'customer_source_list.html', {'cust_source_list':cust_source_list},{'cust_source_list_del':cust_source_list_del})



# 客户来源信息添加
def customer_source_add(request):
    if request.method == 'GET':
        return render(request, "customer_source_add.html")
    else:
        source_name = request.POST.get('sourceName', None)

        try:
            source1 = CustomerSource.objects.get(source_name=source_name)
        except CustomerSource.DoesNotExist:
            source2 = CustomerSource.objects.create(source_name=source_name)

    return HttpResponseRedirect('/client/customer_source_list')

# 客户来源信息删除
def customer_source_list_dele(request):
    sourc_id = request.GET.get('sourceId', None)
    sourc_id = int(sourc_id)
    CustomerSource.objects.filter(source_id=sourc_id).delete()
    return HttpResponseRedirect('/client/customer_source_list.html')

# 客户查询
def customer_source_list_find(request):
    if request.method == 'GET':
        cust_source_list = CustomerSource.objects.all()
        return render(request, 'customer_source_list.html', {'cust_source_list': cust_source_list})
    else:
        source_name = request.POST.get('SourceName', None)
        source_name = CustomerSource.objects.filter(source_name=source_name)
        if source_name:
            return render(request, "customer_source_list.html", {'cust_source_list': source_name})
        else:
            return HttpResponseRedirect('/client/customer_source_list')

# 分页展示
def customer_source_list_tab(request, num=1):
    # 获取当前页吗
    num = int(num)
    # 查询所有帖子
    cust_posts = CustomerSource.objects.order_by('-created')
    # 创建分页器对象
    cust_sourc_tab = Paginator(cust_posts, per_page=1)
    # 获取当前页的数据
    cust_list_post = cust_sourc_tab.page(num)
    # 每页显示的页码范围
    cust_tab_begin = (num-int(match.ceil(10.0/2)))
    if cust_tab_begin < 1:
        cust_tab_begin = 1
    # 每页结束码
    cust__tab_end = cust_tab_begin + 9
    if cust__tab_end > cust_sourc_tab.num_pages:
        cust__tab_end = cust_sourc_tab.num_pages
    if cust__tab_end <= 10:
        cust_tab_begin = 1
    else: cust_tab_begin = cust__tab_end - 9

    cust_paglist = range(cust_tab_begin,cust__tab_end+1)

    return render(request,'customer_source_list.html',{'cust_list_post':cust_list_post,'cust_paglist':cust_paglist,'num':num,'cust_posts':cust_posts})

