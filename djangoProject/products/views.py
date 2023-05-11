from django.shortcuts import render, redirect

from djangoProject.products.models import Products, ProductsLikes, ProductsCart


def product_detail(request, product_slug):

    product = Products.objects.filter(slug=product_slug).get()

    products_in_cart = None
    total_price_of_cart = None

    if request.user.is_authenticated:
        products_in_cart = ProductsCart.objects.filter(user=request.user)

    if request.user.is_authenticated:
        total_price_of_cart = ProductsCart.total_price(current_user=request.user)

    context = {
        'user_is_auth': request.user.is_authenticated,
        'product': product,
        'products_in_cart': products_in_cart,
        'total_cart_price': total_price_of_cart,
    }

    return render(request, 'product/product-single.html', context)


def product_page(request, sorting):

    products_in_cart = None
    total_price_of_cart = None

    if request.user.is_authenticated:
        products_in_cart = ProductsCart.objects.filter(user=request.user)

    if request.user.is_authenticated:
        total_price_of_cart = ProductsCart.total_price(current_user=request.user)

    sort_choice = product_page_sorted(sorting)

    context = {
        'user_is_auth': request.user.is_authenticated,
        'products_in_cart': products_in_cart,
        'total_cart_price': total_price_of_cart,

        'sorted_products_query': sort_choice[0],
        'sorting': sort_choice[1],
    }
    return render(request, 'common/product.html', context)


# def product_like(request, pk):
#     product = Products.objects.filter(pk=pk).get()
#     user = request.user
#     product_liked_by_user = ProductsLikes.objects.filter(product=product, user=user)
#
#     if not product_liked_by_user:
#         like = ProductsLikes.objects.create(user=user, product=product)
#         like.save()
#
#     else:
#         ProductsLikes.objects.filter(user=user, product=product).delete()
#
#     return redirect(get_product_url(request, product_id=product.pk))
#
#
# def get_product_url(request, product_id):
#     return request.META['HTTP_REFERER'] + f'#photo-{product_id}'


def product_add_to_cart(request, product_slug):
    pass


def product_page_sorted(sorting):
    sort_dict = {
        'default': 'Default',
        'price_l2h': 'Price L to H',
        'price_h2l': 'Price H to L',
        'in_stock': 'In Stock',
        'out_of_stock': 'Out of Stock',
        'on_sale': 'On Sale'
    }
    sort_dict_as_list = list(sort_dict.items())

    query = None
    sort_choice = None

    if sorting in sort_dict.keys():
        if sorting == sort_dict_as_list[0][0]:
            query = Products.objects.all()
            sort_choice = sort_dict_as_list[0][1]

        elif sorting == sort_dict_as_list[1][0]:
            query = Products.objects.all().order_by('-price')
            sort_choice = sort_dict_as_list[1][1]

        elif sorting == sort_dict_as_list[2][0]:
            query = Products.objects.all().order_by('price')
            sort_choice = sort_dict_as_list[2][1]

        elif sorting == sort_dict_as_list[3][0]:
            query = Products.objects.filter(in_stock=True)
            sort_choice = sort_dict_as_list[3][1]

        elif sorting == sort_dict_as_list[4][0]:
            query = Products.objects.filter(in_stock=False)
            sort_choice = sort_dict_as_list[4][1]

        elif sorting == sort_dict_as_list[5][0]:
            query = Products.objects.filter(discount_percentage__gt=0)
            sort_choice = sort_dict_as_list[5][1]

    return query, sort_choice
