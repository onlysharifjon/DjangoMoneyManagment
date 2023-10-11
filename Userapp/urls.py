from django.urls import path

from .views import Monthly_money

urlpatterns = [
    path('oylik_pul/', Monthly_money.as_view()),
]
