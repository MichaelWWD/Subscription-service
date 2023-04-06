from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from . import serializers, models

class ContentViewSet(ModelViewSet):
    queryset = models.Content.objects.all()
    serializer_class = serializers.ContentSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'user_id': self.request.user}


class SubscriptionPlanViewSet(ModelViewSet):
    queryset = models.SubscriptionPlan.objects.all()
    serializer_class = serializers.SubscriptionPlanSerializer
    permission_classes = [IsAuthenticated]


class SubscriptionViewSet(ModelViewSet):
    queryset = models.Subscription.objects.all()
    serializer_class = serializers.SubscriptionSerializer
    permission_classes = [IsAuthenticated]
