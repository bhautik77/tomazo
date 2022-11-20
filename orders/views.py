from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrderForm
from .models import Order


def order_create_view(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = OrderForm()
    context = {
        'form': form
    }
    return render(request, "orders/order_create.html", context)


def order_update_view(request, id):
    obj = get_object_or_404(Order, id=id)
    form = OrderForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "orders/order_create.html", context)


def order_list_view(request):
    if request.method == 'POST':
        obj = get_object_or_404(Order, id=request.POST['accept-id'])
        obj.accept_rest = True
        obj.save()

    queryset = Order.objects.filter(accept_rest=False)
    context = {
        "object_list": queryset
    }
    return render(request, "orders/order_list.html", context)


def order_accepted_list_view(request):
    if request.method == 'POST':
        obj = get_object_or_404(Order, id=request.POST['ready-id'])
        obj.is_ready = True
        obj.save()

    queryset = Order.objects.filter(accept_rest=True)
    context = {
        "object_list": queryset
    }
    return render(request, "orders/order_accepted_list.html", context)
