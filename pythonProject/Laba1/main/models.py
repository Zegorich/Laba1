from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

# Модель для товара.
class Product(models.Model):
    name = models.CharField('Имя товара', max_length=100)
    price = models.FloatField('Стоимость товара')
    img = models.ImageField('Изображение товара', upload_to='img/')
    extra_info = models.TextField('Дополнительная информация', max_length=1000)
    amount = models.FloatField('Количество товара', default=1)
    rest = models.FloatField('Осталось товаров', default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


# Модель для пользователя.
class User(AbstractUser):
    name = models.CharField(verbose_name='ФИО', blank=True, null=True, max_length=100)
    balance = models.FloatField(verbose_name='Баланс', blank=True, null=True, default=0)
    credit_limit = models.FloatField(verbose_name='Кредит', blank=True, null=True)
    debt = models.FloatField(verbose_name='Долг клиента', blank=True, null=True)
    credit_remain = models.FloatField(verbose_name='Остаток по кредиту', blank=True, null=True)
    extra_info = models.TextField(verbose_name='Дополнительная информация', max_length=1000, blank=True, null=True)
    registration_code = models.IntegerField(verbose_name='Код учёта', blank=True, null=True)
    registration_code_flag = models.BooleanField(verbose_name='без имени', blank=True, null=True, default=0)


# Модель для корзины.
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


# Модель для заказа.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    price = models.FloatField('Стоимость товара', default=1)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


# Дополнительная модель для заказа (Order2).
class Order2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spent_money = models.IntegerField(default=0)
    account_money = models.IntegerField(default=0)
    credit_limit = models.IntegerField(default=1)
    current_debt = models.IntegerField(default=1)
    credit_remains = models.IntegerField(default=1)
