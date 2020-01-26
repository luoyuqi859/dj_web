from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
# 用户管理
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

from myblog.models import TopMenu,Banner


class TopMenuSerialization(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = TopMenu
        fields = '__all__'


class BannerSerialization(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Banner
        fields = '__all__'



@api_view(['GET','POST'])
def indexData(request):
    # 首页的导航栏
    topmenu = TopMenu.objects.all()
    topmenuData = TopMenuSerialization(topmenu, many=True)
    # 首页的banner
    banner = Banner.objects.all()
    bannerData = BannerSerialization(banner, many=True)

    userid = request.user.id
    loginType = "NO"
    if userid != None:
        loginType = "OK"

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user != None:
            login(request,user)
            return Response({"loginType":"OK"})
    return Response({"topmenu":topmenuData.data, "banner":bannerData.data, "loginType":loginType})