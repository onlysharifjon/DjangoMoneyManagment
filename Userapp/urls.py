from django.urls import path


from .views import DescriptionMoney,KirimMoney,ChiqimMoney,KirimChiqimfarqi

urlpatterns = [
    path('hamma_pul/', DescriptionMoney.as_view()),
    path('kirim/', KirimMoney.as_view()),
    path('chiqim/', ChiqimMoney.as_view()),
    path('farq/',KirimChiqimfarqi.as_view())


