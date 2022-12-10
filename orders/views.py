from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrderForm
from .models import Order, Item, Item_detail, User_details
from django.contrib.auth.models import User
from django.utils import timezone


def item_view(request):
    name = request.user.username
    user_id = User.objects.filter(
        username=name).values_list('id', flat=True)[0]

    order_list = Order.objects.filter(
        accept_rest=True, rest_id=user_id, is_ready=False)

    item_detail = []
    for order in order_list:
        item_list = Item.objects.filter(order_id=order.id)

        for item in item_list:
            temp_item = Item_detail.objects.filter(
                id=item.item_id)
            temp_item.item_name = temp_item.values_list(
                'item_name', flat=True)[0]
            temp_item.no_item = item.no_item
            temp_item.order_id = item.order_id
            temp_item.prep_time = order.get_time_left
            item_detail.append(temp_item)

    context = {
        "item_detail": item_detail
    }
    return render(request, "orders/item_view.html", context)


def order_detail_view(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Order, id=request.POST['order-id'])
        if 'accept' in request.POST.keys():
            obj.prep_time = request.POST['prep-time']
            obj.acc_time = timezone.now()
            obj.accept_rest = True
        elif 'reject' in request.POST.keys():
            obj.accept_rest = False
        else:
            obj.is_ready = True
        obj.save()
        queryset = Order.objects.filter(accept_rest=True)
        context = {
            "object_list": queryset
        }
        return redirect('/orders/accepted/')

    name = request.user.username

    order_details = get_object_or_404(Order, id=id)
    customer_user_details = get_object_or_404(User_details, username=name)
    customer_care_user_details = get_object_or_404(
        User_details, username='Customer_care')
    try:
        deli_details = User_details.objects.filter(id=order_details.deli_id)[0]
    except:
        deli_details = None

    item_list = Item.objects.filter(order_id=id)

    item_detail = []
    for item in item_list:
        temp_item = Item_detail.objects.filter(
            id=item.item_id)
        temp_item.item_name = temp_item.values_list('item_name', flat=True)[0]
        temp_item.price = temp_item.values_list('price', flat=True)[0]
        temp_item.no_item = item.no_item
        item_detail.append(temp_item)

    context = {
        "order_details": order_details,
        "item_detail": item_detail,
        "customer_user_details": customer_user_details,
        "customer_care_user_details": customer_care_user_details,
        "deli_details": deli_details
    }
    return render(request, "orders/order_detail.html", context)


def order_create_view(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = OrderForm()
    context = {
        'form': form
    }
    return render(request, "orders/order_create.html", context)


def order_list_view(request):
    if request.method == 'POST':
        obj = get_object_or_404(Order, id=request.POST['accept-id'])
        obj.accept_rest = True
        obj.save()

    name = request.user.username
    if name == "":
        return redirect('/admin/')
    user_id = User.objects.filter(
        username=name).values_list('id', flat=True)[0]
    queryset = Order.objects.filter(accept_rest=False, rest_id=user_id)
    context = {
        "object_list": queryset
    }
    return render(request, "orders/order_list.html", context)


def order_accepted_list_view(request):
    if request.method == 'POST':
        obj = get_object_or_404(Order, id=request.POST['ready-id'])
        obj.is_ready = True
        obj.save()

    name = request.user.username
    user_id = User.objects.filter(
        username=name).values_list('id', flat=True)[0]

    queryset = Order.objects.filter(accept_rest=True, rest_id=user_id)
    context = {
        "object_list": queryset
    }
    return render(request, "orders/order_accepted_list.html", context)
