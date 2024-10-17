from django.shortcuts import render , redirect , get_object_or_404
from .models import banner , clothes_product , digital_product , base_product , Favorite 
from django.db.models import Q

def test_store(request):
    context = {
        'banner_images' : banner.objects.get(title ='home-main').images,
        'banner_images2' : banner.objects.get(title ='home-main2').images,
        'clothes_products' : clothes_product.objects.all(),
        'digital_products' : digital_product.objects.all(),
        'suggested_products' : clothes_product.objects.filter(is_suggested = True),
    }
    return render(request , "index.html" , context)

def product_detail(request , id):
    product = clothes_product.objects.all()
    return render(request , 'single-product.html' , {'product' : product} )

def add_remove_favorite(request, product_id):
    product = get_object_or_404(base_product, id=product_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)

    if not created:
        favorite.delete()
    
    return redirect(clothesproduct_page, id=product_id)


# def product_page(request , id):
#     context = {}
#     product = get_object_or_404(base_product, id=id)
#     product_detail = get_object_or_404(product_detail, product=product)
#     if request.user.is_authenticated:
#         is_favorite = Favorite.objects.filter(user=request.user, product=product).exists()
#     else:
#         is_favorite = False
#     context['product'] = product
#     context['product_detail']= product_detail
#     context['without_discount' ]= f"{round(product.price/(1-(product.discount/100))):,}"
#     context['discount_price' ]= f"{round((product.price/(1 - (product.discount/100))) - product.price):,}"
#     context['is_favorite']= is_favorite

#     if product.count > 0:
#         return render(request , 'single-product.html' , context)
#     else:
#         return render(request , 'single-product-not-available.html' , context)

def clothesproduct_page(request, id):
    context = {}
    product = get_object_or_404(clothes_product, id=id)

    context['product'] = product


    if product.count > 0:
        return render(request , 'single-product.html' , context)
    else:
        return render(request , 'single-product-not-available.html' , context)
    
def digitalproduct_page(request, id):
    context = {}
    product = get_object_or_404(digital_product, id=id)

    context['product'] = product
    print('mage inja nisti kalak? : ',product)

    if product.count > 0:
        return render(request , 'single-product.html' , context)
    else:
        return render(request , 'single-product-not-available.html' , context)
    
def product_search(request):
    query = request.GET.get('q') 
    products = clothes_product.objects.all() 
    digital_products = digital_product.objects.all() 

    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(brand__name__icontains=query) | 
            Q(category__name__icontains=query)
        ).distinct()
        digital_products = digital_products.filter(
            Q(name__icontains=query) | 
            Q(brand__name__icontains=query) | 
            Q(category__name__icontains=query)
        ).distinct()
    from itertools import chain
    combined_products = list(chain(products, digital_products))

    return render(request, 'search.html', {'products': combined_products})