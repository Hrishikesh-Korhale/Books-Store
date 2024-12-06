from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .models import Book, Order


def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "book_detail.html", {"book": book})


def about(request):
    return render(request, "about.html")

def thank_you(request):
    return render(request, "thank_you.html")


def contact(request):
    return render(request, "contact.html")


def book_purchase(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "purchase.html", {"book": book})

def purchase_book(request, id):
    # Get the book object
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

        # Validate that required fields are not empty
        if not all([name, email, mobile, address]):
            return render(request, 'purchase.html', {
                'book': book,
                'error_message': 'All fields are required.'
            })

        # Create the order
        Order.objects.create(
            book=book,
            name=name,
            email=email,
            mobile=mobile,
            address=address
        )

        # Redirect to a thank-you page
        return redirect('thank_you')

    # Render the purchase page if method is GET
    return render(request, 'purchase.html', {'book': book})


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
