from django.shortcuts import render,get_object_or_404, redirect
from .forms import BookingForm,OrderForm, CustomLoginForm
from .models import MenuItem,Order, OrderItem
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            messages.success(request, f'Reservation confirmed for {booking.first_name} {booking.last_name}! We look forward to serving you.')
            return redirect('book')
        else:
            messages.error(request, 'Please correct the errors below.')
    context = {'form': form}
    return render(request, 'book.html', context)


def display_menu_item(request, pk=None): 
    menu_item = None
    if pk: 
        try:
            menu_item = MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            menu_item = None
    return render(request, 'menu_item.html', {"menu_item": menu_item})


def menu(request):
    menu_items = MenuItem.objects.all()
    for item in menu_items:
        print(f"DEBUG — title: '{item.name}', price: {item.price}")
    return render(request, 'menu.html', {"menu_items": menu_items})



def combined_view(request):
    home_text = "Welcome to our restaurant!"
    about_text = "We serve delicious food made with love."

    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()

    menu_items = MenuItem.objects.all()
    featured_item = MenuItem.objects.first() if menu_items else None

    context = {
        'home_text': home_text,
        'about_text': about_text,
        'form': form,
        'menu_items': menu_items,
        'featured_item': featured_item,
    }

    return render(request, 'index.html', context)

def order_item(request, item_id):
    menu_item = get_object_or_404(MenuItem, id=item_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        quantity = int(request.POST.get('quantity', 1))
        if form.is_valid():
            order = Order.objects.create(customer_name=form.cleaned_data['customer_name'])
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)
            return render(request, 'order_confirmation.html', {'item': menu_item, 'qty': quantity})
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form, 'item': menu_item})

def view_orders(request):
    orders = Order.objects.all().prefetch_related('items')
    return render(request, 'orders.html', {'orders': orders})


def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomLoginForm()
    
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')