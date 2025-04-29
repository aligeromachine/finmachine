from django.db import models
from django.conf import settings as st

class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    state_id = models.BigIntegerField(default=0)
    user = models.ForeignKey(
        st.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

class AmountMixin(TimeStampedMixin):
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        verbose_name="Sum Value",
    )

    class Meta:
        # Этот параметр указывает Django, что этот класс не является представлением таблицы
        abstract = True

class Shop(TimeStampedMixin):
    address = models.CharField(max_length=250)

    class Meta:
        db_table = "content\".\"shop"
        verbose_name = "Shop"
        verbose_name_plural = "Shop"

class Source(TimeStampedMixin):
    class Meta:
        db_table = "content\".\"source"
        verbose_name = "Source"
        verbose_name_plural = "Source"

class Catalog(TimeStampedMixin):
    class Meta:
        db_table = "content\".\"catalog"
        verbose_name = "Catalog"
        verbose_name_plural = "Catalog"

class Cards(AmountMixin):
    number = models.CharField(max_length=250)

    class Meta:
        db_table = "content\".\"cards"
        verbose_name = "Cards"
        verbose_name_plural = "Cards"

class Products(TimeStampedMixin):
    catalog_id = models.BigIntegerField(default=0)

    class Meta:
        db_table = "content\".\"products"
        verbose_name = "Products"
        verbose_name_plural = "Products"

class Profit(AmountMixin):
    source_id = models.BigIntegerField(default=0)

    class Meta:
        db_table = "content\".\"profit"
        verbose_name = "Profit"
        verbose_name_plural = "Profit"

class Buy(AmountMixin):
    shop_id = models.BigIntegerField(default=0)
    products_id = models.BigIntegerField(default=0)

    class Meta:
        db_table = "content\".\"buy"
        verbose_name = "Buy"
        verbose_name_plural = "Buy"

class MoneyAggregation(models.Model):
    period = models.SmallIntegerField(default=0)
    total_profit = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00,
        verbose_name="Sum Profit",
    )
    total_transaction = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00,
        verbose_name="Sum Buy",
    )
    user = models.ForeignKey(
        st.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "content\".\"aggregations"
        verbose_name = "MoneyAggregation"
        verbose_name_plural = "MoneyAggregation"
