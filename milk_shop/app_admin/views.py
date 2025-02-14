from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Customer, Order
from django.contrib import messages
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'app_admin/product_list.html', {'products': products})

def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Sản phẩm đã được thêm!")
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'app_admin/product_form.html', {'form': form})

def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request, "Sản phẩm đã bị xóa!")
    return redirect('product_list')

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'app_admin/order_list.html', {'orders': orders})