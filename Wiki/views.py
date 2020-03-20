from Wiki.models import Page
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django import forms
import markdown
# import htmllib
from django.template import RequestContext, loader
# from django.core.context_processors import csrf
# Create your views here.

def view_page(request, page_name):
    c = {}
    try:
        page = Page.objects.get(pk=page_name)
        content = page.content
    except Page.DoesNotExist:
        return render(request,"create.html", {"page_name":page_name })
    content = page.content
    return render(request,"view.html", {"page_name":page_name, "content":content})

def edit_page(request, page_name):
    try:
        page = Page.objects.get(pk=page_name)
        content = page.content
    except Page.DoesNotExist:
        content = ""
    return render(request,"edit.html", {"page_name":page_name, "content":content})
    print()

def save_page(request, page_name):
    
    content = request.POST['content']
    try:
        page = Page.objects.get(pk=page_name)
        # content = request.GET['content']
        page.content = content
    except Page.DoesNotExist:
        page = Page(name=page_name, content=content)
    page.save()
#    return HttpResponseRedirect ("wikicamp/" + "{{page_name}}" + "/")
    return HttpResponseRedirect("/wiki/" + page_name + "/")