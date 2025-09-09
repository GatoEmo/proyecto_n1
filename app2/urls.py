from django.urls import path
from . import views

urlpatterns=[
    path("inicio2/", views.index_app2)
]