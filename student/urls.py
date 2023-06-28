from django.urls import path
from rest_framework.routers import DefaultRouter


from .views import StudentViewSet, SpamAPIView


router = DefaultRouter()

router.register('', StudentViewSet)

urlpatterns = [
    path('spam/', SpamAPIView.as_view())
]
    
urlpatterns.extend(router.urls)