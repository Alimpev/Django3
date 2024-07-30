from django.urls import path

from .views import *

urlpatterns = [

    path('list/', ListPost.as_view()),
    path('<int:pk>/', OnePost.as_view())

]