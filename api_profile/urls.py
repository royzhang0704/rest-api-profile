from django.urls import path,include

from rest_framework.routers import DefaultRouter

from . import views

router=DefaultRouter()

router.register('hello-viewset',views.HelloViewset,basename='hello-viewset')
router.register('profile',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)
urlpatterns = [
    path('hello-apiview/',views.HelloApiView.as_view()),
    path('login/',views.UserLoginAPIView.as_view()),
    path('',include(router.urls))
]
