from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from djangoProject.products.models import Products, ProductsLikes, ProductsCart


def product_detail(request, product_slug):
    """ product_detail returns single product detail page of the product the user chooses"""

    product = Products.objects.filter(slug=product_slug).get()

    products_in_cart = None
    total_price_of_cart = None
    number_of_products_in_cart = None

    if request.user.is_authenticated:
        user = request.user

        products_in_cart = ProductsCart.objects.filter(user=user)
        number_of_products_in_cart = ProductsCart.total_products_in_user_cart(user)
        total_price_of_cart = ProductsCart.total_price(user)

    if products_in_cart:
        for prod in products_in_cart:
            print(prod.product.product_name)



    context = {
        'user_is_auth': request.user.is_authenticated,
        'product': product,

        'products_in_cart': products_in_cart,
        'number_of_products_in_cart': number_of_products_in_cart,
        'total_cart_price': total_price_of_cart,
    }

    return render(request, 'product/product-single.html', context)


def product_page(request, category, sub_category, sorting):
    """ product_page returns list of products based on the above parameters which the user chooses"""

    products_in_cart = None
    total_price_of_cart = None
    number_of_products_in_cart = None

    if request.user.is_authenticated:
        user = request.user

        products_in_cart = ProductsCart.objects.filter(user=user)
        total_price_of_cart = ProductsCart.total_price(user)
        number_of_products_in_cart = ProductsCart.total_products_in_user_cart(user)

    product_category = product_page_category(category, sub_category)
    sort_choice = product_page_sorted(sorting, product_category)

    paginated_page = product_paginated_page(sort_choice[0])
    get_selected_product_page = request.GET.get('page')

    selected_product_page = paginated_page.page(get_selected_product_page)

    total_pages = selected_product_page.paginator.page_range

    if not selected_product_page.has_next():
        get_selected_product_page = 1

    context = {
        'products': selected_product_page,
        'total_pages': total_pages,
        'current_page': get_selected_product_page,

        'user_is_auth': request.user.is_authenticated,

        'products_in_cart': products_in_cart,
        'total_cart_price': total_price_of_cart,
        'number_of_products_in_cart': number_of_products_in_cart,

        'sorted_products_query': sort_choice[0],
        'sorting': sort_choice[1],
        'category': category,
        'sub_category': sub_category,
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
    """ product_add_to_cart takes the product's slug
    which the user selected and adds it to the current user cart"""

    user = request.user
    product = get_object_or_404(Products, slug=product_slug)

    cart_item = ProductsCart.objects.filter(user=user, product=product).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item = ProductsCart(user=user, product=product, quantity=1)
        cart_item.save()








    # if user_cart.product == product:
    #     user_cart.product.quantity += 1
    #     user_cart.
    #
    # elif not user_cart.product == product:
    #     user_cart.create(user=user, product=product, quantity=1)

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def product_paginated_page(final_query):
    """ product_paginated_page gets the final
    product query and paginate it by the number chosen below """

    paginated_page = Paginator(final_query, 5)
    return paginated_page


def product_page_category(category, sub_category):
    """ product_page_category takes
    the category and sub_category which the user chooses
    and returns a product query based on that """

    query = None

    if category == 'all' and sub_category == 'all':
        query = Products.objects.all()
    query = Products.objects.filter(category=category, secondary_category=sub_category).all()

    return query.all()


def product_page_sorted(sorting, products):
    """ product_page_sorted takes the sorting
    method the user chooses and the product
    query from 'product_page_category' and
    gives the final sorted product query """

    sort_dict = {
        'default': 'Default',
        'price_l2h': 'Price L to H',
        'price_h2l': 'Price H to L',
        'in_stock': 'In Stock',
        'out_of_stock': 'Out of Stock',
        'on_sale': 'On Sale',
        'None': 'Default',
    }

    sort_dict_as_list = list(sort_dict.items())

    query = products
    sort_choice = None

    if sorting in sort_dict.keys():
        if sorting == sort_dict_as_list[0][0]:
            query = query.all()
            sort_choice = sort_dict_as_list[0][1]

        elif sorting == sort_dict_as_list[1][0]:
            query = query.all().order_by('price')
            sort_choice = sort_dict_as_list[1][1]

        elif sorting == sort_dict_as_list[2][0]:
            query = query.all().order_by('-price')
            sort_choice = sort_dict_as_list[2][1]

        elif sorting == sort_dict_as_list[3][0]:
            query = query.filter(in_stock=True)
            sort_choice = sort_dict_as_list[3][1]

        elif sorting == sort_dict_as_list[4][0]:
            query = query.filter(in_stock=False)
            sort_choice = sort_dict_as_list[4][1]

        elif sorting == sort_dict_as_list[5][0]:
            query = query.filter(discount_percentage__gt=0)
            sort_choice = sort_dict_as_list[5][1]

        # edge cases !!
    elif sorting not in sort_dict.keys():
        query = query.all()
        sort_choice = sort_dict_as_list[6][1]
        # edge cases !!

    return query.all(), sort_choice
