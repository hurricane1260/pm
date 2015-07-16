#coding=utf-8

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .models import *

# Create your views here.

from pm.api import *

class AddError(Exception):
    pass

@require_login
def project_list(request):
    header_title, path1, path2 = '查看项目', '项目管理', '查看项目'

    projects = JProject.objects.all()
    contact_list = projects
    contact_list, p, contacts, page_range, current_page, show_first, show_end = pages(contact_list, request)
    return render_to_response('jproject/project_list.html', locals(), context_instance=RequestContext(request))


@require_admin
def project_add(request):
    header_title, path1, path2 = '添加项目', '项目管理', '添加项目'
    project_status = {0: 'Normal', 1: 'Delay'}
    if request.method == 'POST':
        name = request.POST.get('name', '')
        comment = request.POST.get('comment', '')
        date_start = request.POST.get('date_start', '')
        date_end = request.POST.get('date_end', '')

        try:
            if not name:
                raise AddError('项目名称不能为空')
            if JProject.objects.filter(name=name):
                raise AddError(u'项目名称 %s 已存在' % name)
        except AddError, e:
            error = e
        else:
            JProject(name=name, comment=comment, date_start=date_start, date_end=date_end).save()
            msg = u'添加项目 %s 成功' % name

    return render_to_response('jproject/project_add.html', locals(), context_instance=RequestContext(request))