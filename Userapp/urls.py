from django.urls import path

from .views import Monthly_money, DescriptionMoney

urlpatterns = [
    path('oylik_pul/', Monthly_money.as_view()),
    path('hamma_pul/', DescriptionMoney.as_view()),
]
