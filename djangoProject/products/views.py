from django.shortcuts import render, redirect

from djangoProject.products.models import Products, ProductsLikes


def product_detail(request):

    return render(request, 'product/product-single.html')


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
    print(product_slug)
