from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # Main book listing
    path('book/<int:id>/', views.book_detail, name='book_detail'),  # Book detail page
]
