from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # Home page (Book list)
    path('about/', views.about, name='about'),    # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('book/<int:id>/', views.book_detail, name='book_detail'),  # Book detail page
]
