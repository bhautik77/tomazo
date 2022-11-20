from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import timedelta


class Order(models.Model):
    username = models.CharField(blank=False, max_length=120, null=False)
    items = models.TextField(blank=False, null=False)
    price = models.DecimalField(
        blank=False, decimal_places=2, max_digits=10000, null=False)
    instruction_restaurant = models.TextField(
        blank=False, null=True)
    instruction_delivery = models.TextField(
        blank=False, null=True)
    add_time = models.DateTimeField(
        default=timezone.now)
    prep_time = models.IntegerField(default=0)
    is_ready = models.BooleanField(default=False)
    accept_rest = models.BooleanField(default=False)
    accept_deli = models.BooleanField(default=False)
    rest_id = models.IntegerField(default=-1)
    deli_id = models.IntegerField(default=-1)

    def get_absolute_url(self):
        return reverse("orders:order-detail", kwargs={"id": self.id})

    def __str__(self):
        return str(self.id)

    def get_remaining_time(self):
        start_time = self.add_time
        end_time = start_time + timedelta(
            0, self.prep_time * 60
        )
        return end_time - timezone.now()

    def get_time_left(self):
        left = self.get_remaining_time()

        sec = int(left.total_seconds())
        if sec > 60:
            return "{} minutes".format(int(sec / 60))
        elif sec < 60 and sec > 0:
            return "{} seconds".format(sec)
        else:
            return 0
