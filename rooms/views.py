from django.views.generic import ListView
from django.shortcuts import render
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    """ 
        concept of listview
        : reference - http://ccbv.co.uk
        : 문제점 - method는 보여주나 property(속성)는 안보여줌
    """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


def room_detail(request, pk):
    print(pk)
    return render(request, "rooms/detail.html")