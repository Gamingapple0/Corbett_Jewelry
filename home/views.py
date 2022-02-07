from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Product, Images, Beads
from django.core.mail import send_mail

# products = Product.objects.all()
# max_products_per_page = 9
# home_page = products[:max_products_per_page]
# divided_product_list = []
# first = max_products_per_page
# last = max_products_per_page + max_products_per_page
# curr_page = 1
# for i in range(max_products_per_page,len(products),max_products_per_page):
#     divided_product_list.append(products[first:last])
#     first = last
#     last += max_products_per_page


def home(request):
    return render(request, 'index.html')
    
# def home(request):
#     return render(request, 'index.html', {'products' : home_page,'nxt':1,'prev':len(divided_product_list)})

# def nxt_pg(request,num):
#     if num > len(divided_product_list) or num == 0:
#         return home(request)
#     elif num < 0:
#         num = len(divided_product_list)
#     return render(request, 'index.html', {'products': divided_product_list[num-1],'nxt':num+1,'prev':num-1})


# def detail_view(request,slug):
#     product = get_object_or_404(Product,slug=slug)
#     images = Images.objects.filter(product=product)
#     return render(request, 'details.html', {
#         'product': product,
#         'images': images
#     })

def purchased(request, slug):
    if request.method == 'POST':
        view = request.POST.get('productname',False)
        if view:
            product_name =  request.POST['productname']
            name = request.POST['name']
            number = request.POST['pnum']
            email = request.POST['email']
            quantity = request.POST['quantity']
            address = request.POST['add']
            extra = request.POST['einfo']
            send_mail(f'Order Recieved {name} {product_name}',
                      f"""
                        Name: {name}
                        Number: {number}
                        E-mail: {email}
                        Quantity: {quantity}
                        Address: {address}
                        Extra Info: {extra}
    """, email, ['corbettjewelry991@gmail.com'])
            return render(request, 'purchased.html', {'name': name})
        else:
            selected_beads = request.POST['selected_beads']
            name = request.POST['name']
            number = request.POST['pnum']
            email = request.POST['email']
            quantity = request.POST['quantity']
            address = request.POST['add']
            extra = request.POST['einfo']
            send_mail(f'Custom Order Recieved {name}',
                      f"""
Selected Beads: {selected_beads}
Name: {name}
Number: {number}
Quantity: {quantity}
Address: {address}
Extra Info: {extra}
            """, email, ['corbettjewelry991@gmail.com'])
            return render(request, 'purchased.html', {'name': name})
    else:
        return render(request,'purchased.html')


def custom(request):
    beads = Beads.objects.all()
    return render(request,'custom.html',{'beads':beads})
