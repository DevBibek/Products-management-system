from django.shortcuts import render,redirect
from .models import Product
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):
    return render(request,'index.html')

@login_required
def addproduct(request):
    if request.method == 'POST':
       
        pn = request.POST.get('name')
        pp = request.POST.get('price')
        pc = request.POST.get('category')
        ps = request.POST.get('stock')
        if not all([pn, pp, pc, ps]):
            messages.error(request,'All fields are required',extra_tags="add_product")
            return redirect('addproduct')

        else:
            Product.objects.create(user = request.user ,name = pn ,price = pp,  category = pc ,stock = ps)
            messages.success(request,'Add product successfuly', extra_tags="add_product")
            return redirect('productlist')
        
    return render(request,'addproduct.html')

@login_required
def product_list(request):
    product = Product.objects.filter(user = request.user)
    if request.method =='POST':
        data = request.POST
        searched = data['search']
        
        # === FOR EMTPY CHEACK ====
        if not  searched.strip():
            messages.warning(request,'Please Enter Somthing',extra_tags="search")
            

        else:
            product = Product.objects.filter(Q(name__icontains = searched)
        |Q(price__icontains =  searched)|Q(stock__icontains = searched)|Q(category__icontains = searched))
            
            # ==== FOR DATA CHEACK ===
            if not product:
                messages.error(request,'NO Data Found',extra_tags='search')

    return render(request,'productlist.html',{'product': product})


@login_required
def update_product(request,id):
    prod = get_object_or_404(Product, pk = id ,user = request.user)
    if request.method == 'POST':
        data = request.POST
        prod.name = data['name']
        prod.price = data['price']
        prod.category = data['category']
        prod.stock = data['stock']
        prod.save()
        messages.success(request,"Product Updated Successfully",extra_tags="update_product")
        return redirect('productlist')
    return render(request,'updateproduct.html',{'product': prod})


def delete_product(request,id):
    prod = get_object_or_404(Product,pk = id , user = request.user)
    prod.delete()
    messages.success(request,'Delete product successfuly',extra_tags="delete_product")
    return redirect('productlist')

@login_required
def dashboard(request):
    products = Product.objects.filter(user = request.user)
    total_products = products.count()
    

    return render(request, 'dashboard.html', {
        'total_products': total_products,
        'products':products
      
    })

