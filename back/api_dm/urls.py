from django.urls import path, include
from rest_framework.routers import DefaulRouter

app_name = 'dm'

router = DefaulRouter()

urlpatterns = [
    path('', include(router.urls))
]
