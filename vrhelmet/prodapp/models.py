from django.utils import timezone
from django.db import models
from django.utils.functional import cached_property

from usersapp.models import SiteUser

class ActiveManager(models.Manager):
    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_active=True)

class MainManager(models.Manager):
    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_main=True)

class IsActiveMixin(models.Model):
    objects = models.Manager()
    active_objects = ActiveManager()
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Category(models.Model):       #этот механизм включает функцию orm, т.е.данные сохраняются в бд
    #создаем поля. из models выбираем тип, в скобках парамерты поля
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name ='category'
        verbose_name_plural = 'categories'


class Helmets(IsActiveMixin):
    name = models.CharField(max_length=64, unique=True)
    #artikul = models.PositiveIntegerField(unique=True)
    text = models.CharField(max_length=84, default='Новое поколение игровых гарнитур')
    description = models.TextField(blank=True)
    #image = models.ImageField(upload_to='helmets/', null=True, blank=True)
    price = models.PositiveIntegerField(default=1)
    stock = models.CharField(max_length=16)   #срок поставки
    guarantee = models.CharField(max_length=16, blank=True)
    sale = models.CharField(max_length=3, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    #created = models.DateTimeField(auto_now_add=True, auto_now=False, default=timezone.now)
    #updated = models.DateTimeField(auto_now_add=False, auto_now=True, default=timezone.now)

    def __str__(self):
        return "%s, %s, %s" % (self.price, self.name, self.category)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class ProductImages(IsActiveMixin):
    objects = models.Manager()
    active_objects = ActiveManager()
    main_objects = MainManager()
    product = models.ForeignKey(Helmets, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='helmets/')
    #is_active = models.BooleanField(default=False)
    is_main = models.BooleanField(default=False)
    #created = models.DateTimeField(auto_now_add=True, auto_now=False, default=timezone.now)
    #updated = models.DateTimeField(auto_now_add=False, auto_now=True, default=timezone.now)

    def __str__(self):
        return "%s" % self.id

    # @cached_property
    # def get_product_pk(self, pk):
    #     pk = Helmets.objects.get(pk=pk)
    #     return pk

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'


class Carusel(models.Model):
    image1 = models.ImageField(upload_to='carusel', null=True, blank=True)
    image2 = models.ImageField(upload_to='carusel', null=True, blank=True)
    image3 = models.ImageField(upload_to='carusel', null=True, blank=True)
    image4 = models.ImageField( upload_to='carusel', null=True, blank=True )

    class Meta:
        verbose_name = 'carusel_image'
        verbose_name_plural = 'carusel_images'


# Заявка со страницы contactform
class Message(models.Model):
    name = models.CharField(max_length=128)
    #tel = models.CharField(max_length=16)
    email = models.EmailField(max_length=100)
    text = models.CharField(max_length=300)
    #user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)

    def __str__(self):
        return "%s, %s" % (self.id, self.email)

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'








