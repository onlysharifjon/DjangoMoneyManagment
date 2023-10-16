from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Money_monthly_serializer, Money_monthly_serializer_send
from .models import UserRegistration, MoneyManagment


# salomlar
class Monthly_money(APIView):
    serializer_class = Money_monthly_serializer
    queryset = UserRegistration.objects.all()

    def post(self, request):
        username = request.data.get('username')
        print(f"Serializer: {username}")

        try:
            user = UserRegistration.objects.get(username=username)
            print(f"User: {user}")
            money = MoneyManagment.objects.all().filter(user=user)

            import datetime
            now = datetime.datetime.now()
            now_month = now.month
            money = money.filter(date__month=now_month)
            # Handle the money data and return a response
            if money:
                # Process the money data here
                # ...
                serializer_pulcha = Money_monthly_serializer_send(money, many=True)
                return Response({"message": serializer_pulcha.data})
            else:
                return Response({"message": "No money data found for this user"})
        except UserRegistration.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


class DescriptionMoney(APIView):
    serializer_class = Money_monthly_serializer
    queryset = UserRegistration.objects.all()

    def post(self, request):
        username = request.data.get('username')
        user = UserRegistration.objects.get(username=username)
        money = MoneyManagment.objects.all().filter(user=user)
        serializer_pulcha = Money_monthly_serializer_send(money, many=True)
        hammasi = 0
        for i in serializer_pulcha.data:
            hammasi += i['narx']
        return Response({"Sarflangan pul miqdori umumiy: ": hammasi})
