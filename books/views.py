from django.shortcuts import render, get_object_or_404
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "book_detail.html", {"book": book})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def book_purchase(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "purchase.html", {"book": book})


def login(request):
    return render(request, "login.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
