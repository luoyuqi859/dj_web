from django.shortcuts import render
from .models import TopMenu,Artical


# Create your views here.
def index(request):
    topMenu = TopMenu.objects.all()
    artical = Artical.objects.all()

    context = {
        "topMenu": topMenu,
        "artical": artical,
    }
    return render(request, 'myblog/index.html', context)
