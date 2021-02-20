from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models


def all_rooms(request):
    """
    - Django list nav
    - concept of exception
    - orphans
    - paginator.page()
    - handing Exceptions : use try, except - 무엇인가 하려 할때 exception이면 handing 가능.(15페이지에서 16페이지로 가려하면 자동으로 처음페이지로 이동(전체 페이지수가 15까지밖에 없으므로.))
    """
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")