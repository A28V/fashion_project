from django.db import models
from catalog_settings.models import products
from django.conf import settings
from django.utils import timezone

class Order(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(products, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


class payhistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rel_payment_paytm', on_delete=models.CASCADE)
    ORDERID = models.CharField('ORDER ID', max_length=30)
    TXNDATE = models.DateTimeField('TXN DATE', default=timezone.now)
    TXNID = models.CharField('TXN ID', max_length=300)
    BANKTXNID = models.IntegerField('BANK TXN ID', null=True, blank=True)
    BANKNAME = models.CharField('BANK NAME', max_length=50, null=True, blank=True)
    RESPCODE = models.IntegerField('RESP CODE')
    PAYMENTMODE = models.CharField('PAYMENT MODE', max_length=10, null=True, blank=True)
    CURRENCY = models.CharField('CURRENCY', max_length=4, null=True, blank=True)
    GATEWAYNAME = models.CharField("GATEWAY NAME", max_length=30, null=True, blank=True)
    MID = models.CharField(max_length=40)
    RESPMSG = models.TextField('RESP MSG', max_length=250)
    TXNAMOUNT = models.FloatField('TXN AMOUNT')
    STATUS = models.CharField('STATUS', max_length=12)


class paystatus(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='payment_paytm', on_delete=models.CASCADE)
    email = models.CharField('Email', max_length=30)
    ORDERID = models.CharField('ORDER ID', max_length=30)
    amount = models.CharField('AMOUNT', max_length=30)
    STATUS = models.CharField('STATUS', max_length=12,default='process')
    TXNDATE = models.DateTimeField('TXN DATE', default=timezone.now)

pay_status_change=(
    ('process','process'),
    ('complete','complete')
)

class pay_status(models.Model):
    userId = models.IntegerField("userId")
    email = models.CharField('Email', max_length=30)
    ORDERID = models.CharField('ORDER ID', max_length=30)
    amount = models.CharField('AMOUNT', max_length=30)
    orderSTATUS = models.CharField('STATUS', max_length=12,choices=pay_status_change)
    DATE = models.DateTimeField('DATE', default=timezone.now)


