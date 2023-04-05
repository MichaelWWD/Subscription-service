from rest_framework import serializers
from . import models

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Content
        fields = ['id', 'text', 'created_at']


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubscriptionPlan
        fields = ['name', 'description', 'tier', 'fee', 'duration_days', 'created_at', 'updated_at']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubscriptionPlan
        fields = ['service', 'start_date', 'status', 'created_at', 'updated_at']