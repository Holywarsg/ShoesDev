from django.db import models


class Shoes(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug_Shoes")
    description = models.TextField(blank=True)
    color = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True)
    shoe_size = models.ForeignKey('ShoeSize', on_delete=models.SET_NULL, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='shoes/')  # Путь, куда будут загружаться фото
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    sex = models.ForeignKey('Sex', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    season = models.ForeignKey('Season', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)  # Например, "Красный", "Синий" и т.д.

    def __str__(self):
        return self.name


class ShoeSize(models.Model):
    size = models.DecimalField(max_digits=4, decimal_places=2)  # Например, 39.5, 40 и т.д.

    def __str__(self):
        return str(self.size)


class Brand(models.Model):
    name = models.CharField(max_length=100)  # Например, "Nike", "Adidas" и т.д.
    slug = models.SlugField(max_length=120, unique=True, verbose_name="Slug_Brand", default="default-slug")

    def __str__(self):
        return self.name


class Sex(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



