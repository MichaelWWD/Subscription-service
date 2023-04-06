from rest_framework import serializers
from . import models

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Content
        fields = ['id', 'user', 'text', 'created_at']


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubscriptionPlan
        fields = ['user', 'name', 'description', 'tier', 'fee', 'duration_days', 'created_at', 'updated_at']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subscription
        fields = ['trainer', 'subscriber', 'service', 'start_date', 'status', 'created_at', 'updated_at']