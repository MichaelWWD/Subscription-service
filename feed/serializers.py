from rest_framework import serializers
from . import models

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Content
        fields = ['id', 'user', 'text', 'created_at']

    def create(self, validated_data):
        user = self.context['user_id']
        return models.Content.objects.create(user_id=user.id, **validated_data)




class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubscriptionPlan
        fields = ['name', 'description', 'tier', 'fee', 'duration_days', 'created_at', 'updated_at']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subscription
        fields = ['service', 'start_date', 'status', 'created_at', 'updated_at']