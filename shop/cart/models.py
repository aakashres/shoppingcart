from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Timestampable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        super().save()


class Photo(Timestampable):
    photo = models.ImageField("Photo")
    title = models.CharField(
        "Photo Title", max_length=255, null=True, blank=True)

    def __str__(self):
        if self.title:
            return self.title
        return self.photo.url


class Category(Timestampable):
    title = models.CharField("Category Title", max_length=255)
    slug = models.SlugField("Category Slug", unique=True)
    description = models.TextField(
        "Category Description", null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Tag(Timestampable):
    title = models.CharField("Tag Title", max_length=255, unique=True)
    description = models.TextField(
        "Category Description", null=True, blank=True)

    def __str__(self):
        return self.title


class Product(Timestampable):
    name = models.CharField("Product Name", max_length=512)
    slug = models.SlugField("Product Slug", unique=True)
    photos = models.ManyToManyField(Photo, null=True, blank=True)
    description = models.TextField("Product Description")
    quantity = models.PositiveIntegerField("Produc Quantity", default=0)
    categories = models.ManyToManyField(Category, on_delete=models.CASCADE)
    # tags = models.ManyToManyField(Tag, on_delete=models.CASCADE)
    price = models.FloatField("Product Price", default=0)
    vat = models.FloatField("VAT", default=0)
    discount_percent = models.FloatField("Discount Percentage", default=0)

    def __str__(self):
        return self.name


class ProductInTransaction(Timestampable):
    products = models.OneToOneField(Product, null=True, blank=True)
    quantity = models.PositiveIntegerField("Product Quantity", default=0)

    def __str__(self):
        return self.product.name


class Cart(Timestampable):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ForeignKey(ProductInTransaction, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Wishlist(Timestampable):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ForeignKey(ProductInTransaction, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Coupon(Timestampable):
    title = models.CharField("Coupon Title", max_length=255)
    code = models.CharField("Coupon Code", max_length=255)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    validity_count = models.PositiveIntegerField("Validity Count", default=1)
    discount_percent = models.FloatField("Discount Percentage", default=0)

    def __str__(self):
        return self.title


class Point(Timestampable):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_point = models.PositiveIntegerField("Total Points", default=0)

    def __str__(self):
        return self.user.username


class Order(Timestampable):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ForeignKey(ProductInTransaction, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Featured(Timestampable):
    products = models.ForeignKey(Product, null=True, blank=True)

    def __str__(self):
        return self.products.title


class Slider(Timestampable):
    title = models.TextField("Slider Title")
    photos = models.ForeignKey(Photo, null=True, blank=True)

    def __str__(self):
        return self.title
