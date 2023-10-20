from django.urls import path

from .views import DescriptionMoney, KirimMoney, ChiqimMoney, KirimChiqimfarqi, Top3, TopUsers3

urlpatterns = [
    path('hamma_pul/', DescriptionMoney.as_view()),
    path('kirim/', KirimMoney.as_view()),
    path('chiqim/', ChiqimMoney.as_view()),
    path('farq/', KirimChiqimfarqi.as_view()),
    path('top3/', Top3.as_view()),
    path('topuser/', TopUsers3.as_view()),
]
#biz tugatdik