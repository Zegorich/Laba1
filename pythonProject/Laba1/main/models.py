from django.contrib.auth.models import AbstractUser
from django.db import models

from django.urls import reverse

class Product(models.Model):
    name = models.CharField('Имя товара', max_length = 100)
    price = models.FloatField('Стоимость товара')
    img = models.ImageField('Изображение товара', upload_to='img/')
    extra_info = models.TextField('Дополнительная информация', max_length = 1000)
    amount = models.FloatField('Количество товара')
    rest = models.FloatField('Осталось товаров')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class User(AbstractUser):
    name = models.CharField(verbose_name='ФИО', blank=True, null=True, max_length = 100)
    balance = models.FloatField(verbose_name='Баланс', blank=True, null=True)
    credit_limit = models.FloatField(verbose_name='Кредит', blank=True, null=True)
    debt = models.FloatField(verbose_name='Долг долг клиента', blank=True, null=True)
    credit_remain = models.FloatField(verbose_name='Остаток по кредиту', blank=True, null=True)
    extra_info = models.TextField(verbose_name='Дополнительная информация', max_length = 1000, blank=True, null=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    price = models.FloatField('Стоимость товара', default=1)
    QP = models.FloatField('Сумма стоимости товаров 1-го вида', default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product}"

    def get_absolute_url(self):
        return reverse("main:cart_detail")


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    summ = models.FloatField(verbose_name='Сумма всех покупок', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'