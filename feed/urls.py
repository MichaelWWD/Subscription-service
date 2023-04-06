from rest_framework import routers
from . import views
router = routers.SimpleRouter()


router.register('contents', views.ContentViewSet, basename='feed-contents')
router.register('plans', views.SubscriptionPlanViewSet, basename='subscription-plans')
router.register('subscriptions', views.SubscriptionViewSet, basename='subscriptions')

urlpatterns = router.urls