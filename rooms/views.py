from django.views.generic import ListView
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