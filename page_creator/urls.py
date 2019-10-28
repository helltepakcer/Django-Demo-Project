from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_creator_page, name='page-creator-page'),
    ]
