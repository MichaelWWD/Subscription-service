from datetime import timedelta, timezone
from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_trainer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user.username}'

    def username(self) -> str:
        return str(self.user.username)
    

class Content(models.Model):
    #  Entities : Images, Text , 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text  = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SubscriptionPlan(models.Model):
    BASIC_TIER = 'basic'
    PREMIUM_TIER = 'premium'
    TIER_OPTIONS = [
        (BASIC_TIER, 'Basic'),
        (PREMIUM_TIER, 'Premium'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    tier = models.CharField(max_length=15, choices=TIER_OPTIONS, default=BASIC_TIER)
    fee = models.DecimalField(max_digits=6, decimal_places=2)
    duration_days = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('canceled', 'Canceled'),
    )
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trainer_subscriptions')
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriber_subscriptions')
    service = models.ForeignKey(SubscriptionPlan, on_delete=models.PROTECT)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=None)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            # If this is a new subscription, set the end date based on the plan
            self.end_date = timezone.now() + timedelta(days=self.service.duration_days)
        super().save(*args, **kwargs)

    def is_active(self):
        return self.status == 'active' and self.end_date > timezone.now()

    def cancel(self):
        self.status = 'canceled'
        self.save()

    def renew(self):
        if self.is_active():
            self.end_date += timedelta(days=self.service.duration_days)
        else:
            self.status = 'active'
            self.end_date = timezone.now() + timedelta(days=self.service.duration_days)
        self.save()


# class Payment(models.Model):
#     subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f'{self.subscription} - {self.amount}'

# class SubscriptionManager:
#     def __init__(self, subscription):
#         self.subscription = subscription

#     def charge(self, amount):
#         # Implement payment gateway integration logic here
#         payment = Payment(subscription=self.subscription, amount=amount)
#         payment.save()

#     def cancel(self):
#         self.subscription.cancel()

#     def renew(self):
#         self.subscription.renew()
#         self.charge(self.subscription.plan.price)


