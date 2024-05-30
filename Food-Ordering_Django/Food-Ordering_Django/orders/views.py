from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Category, RegularPizza, SicilianPizza, Toppings, Sub, Pasta, Salad, DinnerPlatters, UserOrder, SavedCarts
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout, authenticate, login
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, "orders/home.html", {"categories": Category.objects.all})
    else:
        return redirect("orders:login")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('orders:home')
    form = AuthenticationForm()
    return render(request, "orders/login.html", {"form": form})

def logout_request(request):
    logout(request)
    return redirect("orders:login")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("orders:index")
        return render(request, "orders/register.html", {"form": form})
    return render(request, "orders/register.html", {"form": UserCreationForm()})

def pizza(request):
    if request.user.is_authenticated:
        return render(request, "orders/pizza.html", {
            "regular_pizza": RegularPizza.objects.all,
            "sicillian_pizza": SicilianPizza.objects.all,
            "toppings": Toppings.objects.all,
            "number_of_toppings": [1, 2, 3]
        })
    else:
        return redirect("orders:login")

def pasta(request):
    if request.user.is_authenticated:
        return render(request, "orders/pasta.html", {"dishes": Pasta.objects.all})
    else:
        return redirect("orders:login")

def salad(request):
    if request.user.is_authenticated:
        return render(request, "orders/salad.html", {"dishes": Salad.objects.all})
    else:
        return redirect("orders:login")

def subs(request):
    if request.user.is_authenticated:
        return render(request, "orders/sub.html", {"dishes": Sub.objects.all})
    else:
        return redirect("orders:login")

def dinner_platters(request):
    if request.user.is_authenticated:
        return render(request, "orders/dinner_platters.html", {"dishes": DinnerPlatters.objects.all})
    else:
        return redirect("orders:login")

def directions(request):
    if request.user.is_authenticated:
        return render(request, "orders/directions.html")
    else:
        return redirect("orders:login")

def hours(request):
    if request.user.is_authenticated:
        return render(request, "orders/hours.html")
    else:
        return redirect("orders:login")

def contact(request):
        return render(request, "orders/contact.html")


def cart(request):
    if request.user.is_authenticated:
        return render(request, "orders/cart.html")
    else:
        return redirect("orders:login")

def checkout(request):
    if request.method == 'POST':
        cart = json.loads(request.POST.get('cart'))
        price = request.POST.get('price_of_cart')
        username = request.user.username
        response_data = {}
        list_of_items = [item["item_description"] for item in cart]
        order = UserOrder(username=username, order=list_of_items, price=float(price), delivered=False)
        order.save()
        response_data['result'] = 'Order Received!'
        return JsonResponse(response_data)
    else:
        return JsonResponse({"nothing to see": "this isn't happening"})

def view_orders(request):
    if request.user.is_superuser:
        rows = UserOrder.objects.all().order_by('-time_of_order')
        return render(request, "orders/orders.html", {"rows": rows})
    else:
        rows = UserOrder.objects.filter(username=request.user.username).order_by('-time_of_order')
        return render(request, "orders/orders.html", {"rows": rows})

def mark_order_as_delivered(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        UserOrder.objects.filter(pk=id).update(delivered=True)
        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"nothing to see": "this isn't happening"})

def save_cart(request):
    if request.method == 'POST':
        cart = request.POST.get('cart')
        saved_cart = SavedCarts(username=request.user.username, cart=cart)
        saved_cart.save()
        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"nothing to see": "this isn't happening"})

def retrieve_saved_cart(request):
    if request.user.is_authenticated:
        try:
            saved_cart = SavedCarts.objects.get(username=request.user.username)
            return HttpResponse(saved_cart.cart, content_type="application/json")
        except SavedCarts.DoesNotExist:
            return JsonResponse({"error": "No saved cart found for this user"}, status=404)
    else:
        return JsonResponse({"error": "User not authenticated"}, status=403)

def check_superuser(request):
    return JsonResponse({"is_superuser": request.user.is_superuser})

def makepayment(request):
    return render(request, 'orders/payment.html')


def review(request):
    return render(request, 'orders/review.html')

def user_details(request):
    return render(request, 'orders/user_details.html')

def restaurant_list(request):
    # Dummy data for demonstration purposes
    restaurants = [
        {
            'name': 'Restaurant A',
            'address': '123 Main St, City, Country',
            'menu': [
                {'name': 'Pizza', 'image_url': 'https://example.com/pizza.jpg'},
                {'name': 'Pasta', 'image_url': 'https://example.com/pasta.jpg'},
                {'name': 'Salad', 'image_url': 'https://example.com/salad.jpg'}
            ]
        },
        {
            'name': 'Restaurant B',
            'address': '456 Elm St, City, Country',
            'menu': [
                {'name': 'Burger', 'image_url': 'https://example.com/burger.jpg'},
                {'name': 'Sandwich', 'image_url': 'https://example.com/sandwich.jpg'},
                {'name': 'Fries', 'image_url': 'https://example.com/fries.jpg'}
            ]
        },
        {
            'name': 'Restaurant C',
            'address': '789 Oak St, City, Country',
            'menu': [
                {'name': 'Sushi', 'image_url': 'https://example.com/sushi.jpg'},
                {'name': 'Ramen', 'image_url': 'https://example.com/ramen.jpg'},
                {'name': 'Tempura', 'image_url': 'https://example.com/tempura.jpg'}
            ]
        }
    ]
    return render(request, 'orders/restaurant_list.html', {'restaurants': restaurants})

def term(request):
    return render(request, 'orders/termsandcondition.html')

def privacy(request):
    return render(request, 'orders/privacypolicy.html')

def landingpage(request):
    return render(request, 'orders/landingpage.html')

def work_with_us(request):
    return render(request, 'orders/work_with_us.html')
def about(request):
    return render(request, 'orders/about.html')
