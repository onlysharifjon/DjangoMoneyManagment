from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Money_monthly_serializer, Money_monthly_serializer_send
from .models import UserRegistration, MoneyManagment


# salomlar
#


class DescriptionMoney(APIView):
    serializer_class = Money_monthly_serializer
    queryset = UserRegistration.objects.all()

    def post(self, request):
        username = request.data.get('username')
        try:
            user = UserRegistration.objects.get(username=username)
            money = MoneyManagment.objects.all().filter(user=user)
            serializer_pulcha = Money_monthly_serializer_send(money, many=True)
            hammasi = 0
            for i in serializer_pulcha.data:
                hammasi += i['narx']
            return Response({"Sarflagan pul miqdori umumiy: ": hammasi})
        except:
            return Response("Tizimda qandaydir nosozlik")


class KirimMoney(APIView):
    serializer_class = Money_monthly_serializer
    queryset = UserRegistration.objects.all()

    def post(self, request):
        username = request.data.get('username')
        user = UserRegistration.objects.get(username=username)
        money = MoneyManagment.objects.all().filter(type_payment="Kirim", user=user)
        serializer_pulcha = Money_monthly_serializer_send(money, many=True)
        type_payment = 0
        for i in serializer_pulcha.data:
            type_payment += i['narx']
        return Response({"Kirim pul miqdori : ": type_payment})


class ChiqimMoney(APIView):
    serializer_class = Money_monthly_serializer
    queryset = UserRegistration.objects.all()

    def post(self, request):
        username = request.data.get('username')
        user = UserRegistration.objects.get(username=username)
        money = MoneyManagment.objects.all().filter(type_payment="Chiqim", user=user)
        serializer_pulcha = Money_monthly_serializer_send(money, many=True)
        total_payment = 1
        for i in serializer_pulcha.data:
            total_payment += i['narx']
        return Response({"Sarflagan pul miqdori : ": total_payment})


class KirimChiqimfarqi(APIView):
    serializer_class = Money_monthly_serializer
    queryset = UserRegistration.objects.all()

    def post(self, request):
        username = request.data.get('username')
        user = UserRegistration.objects.get(username=username)
        money_chiqim = MoneyManagment.objects.all().filter(type_payment="Chiqim", user=user)
        serializer_pulcha_chiqim = Money_monthly_serializer_send(money_chiqim, many=True)
        money_kirim = MoneyManagment.objects.all().filter(type_payment="Kirim", user=user)
        serializer_pulcha_kirim = Money_monthly_serializer_send(money_kirim, many=True)
        chqim = 0
        for g in serializer_pulcha_chiqim.data:
            chqim += g['narx']
        kirim = 0

        for i in serializer_pulcha_kirim.data:
            kirim += i['narx']

        summa = kirim - chqim
        return Response({"Xarajatlar natijasi : ": summa,
                         "Kirim": kirim,
                         "Chiqim:": chqim})
