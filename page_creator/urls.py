from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_creator_page, name='page_creator_page'),
    path('<int:pk>/', views.page_creator, name='page_creator'),
    path('input_error', views.one_word_error_page, name='one_word_error_page')
    ]
