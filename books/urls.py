from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list, name="book_list"),  # Home page (Book list)
    path("about/", views.about, name="about"),  # About page
    path("contact/", views.contact, name="contact"),  # Contact page
    path("book/<int:id>/", views.book_detail, name="book_detail"),  # Book detail page
    path('book/<int:id>/purchase/', views.purchase_book, name='purchase_book'),  # Add this route
    path("login/", views.login, name="login"),
    path('signup/', views.signup, name='signup'),
    path('thank-you/', views.thank_you, name='thank_you'),  # Thank-you page
    
]
