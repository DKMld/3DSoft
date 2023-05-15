from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models import Max, Min


CATEGORY_CHOICES = [
    ('airsoft', 'airsoft'),
    ('mountain_bike', 'mountain_bike'),
    ('other', 'other'),
]


SECONDARY_CATEGORY_CHOICES = [
    ('weapon_attachments', 'weapon_attachments'),
    ('gear_accessories', 'gear_accessories'),
    ('other', 'other'),
]


class Products(models.Model):

    product_name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, max_length=1000)
    price = models.FloatField(null=True, max_length=10)

    in_stock = models.BooleanField(null=True)
    discount_percentage = models.FloatField(null=True, max_length=100, default=0)
    quantity = models.FloatField(null=True, max_length=100, default=1)

    image = models.ImageField(null=True, upload_to='product_images', blank=True)

    category = models.CharField(null=True, max_length=50, choices=CATEGORY_CHOICES)
    secondary_category = models.CharField(null=True, max_length=50, choices=SECONDARY_CATEGORY_CHOICES)

    slug = models.SlugField(null=True, unique=True, blank=True, max_length=200)

    def __str__(self):
        return f"{self.product_name} - {self.slug}"

    def save(self, *args, **kwargs):
        super(Products, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.category + '-' + self.secondary_category + '-' + self.product_name + '-' + str(self.id))
            self.save()

    def discounted_price(self):
        discounted_price = (self.price * self.discount_percentage) / 100
        price = self.price - discounted_price
        return price


class ProductsLikes(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.product_name} liked by {self.user.username}"


class ProductsCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.FloatField(max_length=50, null=False, blank=False, default=1)

    @staticmethod
    def total_price(current_user):
        current_user_products_price = ProductsCart.objects.filter(user=current_user)
        total_price_of_cart = 0

        for product in current_user_products_price:

            if product.product.discount_percentage != 0:
                total_price_of_cart += product.product.discounted_price() * product.quantity

            elif product.product.discount_percentage == 0:
                total_price_of_cart += product.quantity * product.product.price

        return total_price_of_cart

    @staticmethod
    def total_products_in_user_cart(current_user):
        current_user_products_num = ProductsCart.objects.filter(user=current_user).count()

        if current_user_products_num == 0:
            return 0
        else:
            return current_user_products_num

