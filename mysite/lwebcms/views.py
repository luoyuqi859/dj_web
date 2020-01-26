from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from lwebcms.models import Userinfo
from myblog.models import Artical
from myblog.forms import ArticalForm

# Create your views here.

def index(request):
    if not isinstance(request.user, User):
        return redirect(to="myblog_index")
    
    userid = request.user
    userinfo = Userinfo.objects.get(belong=userid)
    context = {
        "userinfo":userinfo
    }
    return render(request,"lwebcms/index.html",context)

# 文章列表
def list(request):
    if not isinstance(request.user, User):
        return redirect(to="myblog_index")

    userid = request.user
    userinfo = Userinfo.objects.get(belong=userid)
    artical = Artical.objects.all()
    context = {
        "userinfo":userinfo,
        "artical":artical,
    }
    return render(request,"lwebcms/list.html", context)

# 发布文章
def fabu(request):
    if not isinstance(request.user, User):
        return redirect(to="myblog_index")
    userid = request.user
    userinfo = Userinfo.objects.get(belong=userid)
    if request.method == "GET":
        form = ArticalForm
    if request.method == "POST":
        form = ArticalForm
        title = request.POST["title"]
        content = request.POST['content']
        img = request.FILES['suolvetu']
        new_artical = Artical(title=title, content=content, img=img)
        new_artical.save()
        return redirect('/lwebadmin/list')
    context = {
        "userinfo":userinfo,
        "form":form,
    }
    return render(request, "lwebcms/fabu.html", context)

# 删除文章
def delete_artical(request,id):
    artical = Artical.objects.get(id=id)
    print(artical)
    artical.delete()
    return redirect('/lwebadmin/list')

# 文章内容
def artical(request,id):
    if not isinstance(request.user, User):
        return redirect(to="myblog_index")
    
    # 获取文章
    artical = Artical.objects.get(id=id)


    userid = request.user
    userinfo = Userinfo.objects.get(belong=userid)
    # if request.method == "GET":
    #     form = ArticalForm
    # if request.method == "POST":
    #     form = ArticalForm
    #     title = request.POST["title"]
    #     content = request.POST['content']
    #     new_artical = Artical(title=title, content=content)
    #     new_artical.save()

    if request.method == 'POST':
        title = request.POST['title']
        try:
            img = request.FILES['suolvetu']
        except:
            img = artical.img
        content = request.POST['content']
        artical.title = title
        artical.img = img
        artical.content = content
        artical.save()
    context = {
        "userinfo":userinfo,
        # "form":form,
        "artical":artical,
    }
    return render(request,"lwebcms/artical.html", context)