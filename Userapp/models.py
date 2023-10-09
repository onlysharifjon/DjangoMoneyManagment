from django.db import models


# Create your models here.


class UserRegistration(models.Model):
    username = models.TextField(unique=True, null=False)
    email = models.EmailField(unique=True, null=False)
    phone = models.TextField(unique=True, max_length=18)
    password = models.CharField(max_length=33)

    def __str__(self):
        return self.username


class MoneyManagment(models.Model):
    user = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    narx = models.IntegerField()
    # create choise model
    CHOICES = (
        ('Kirim', 'Kirim'),
        ('Chiqim', 'Chiqim'),
    )

    # create choise field
    type_payment = models.CharField(max_length=30, choices=CHOICES)

    CHOICES1 = (
        ('Oziq ovqat', 'Oziq ovqat'),
        ('Transport', 'Transport'),
        ('Internet', 'Internet'),
        ('Telefon', 'Telefon'),
        ('kiyimlar', 'kiyimlar'),
        ('Qarzlar', 'Qarzlar'),
        ('Komunal', 'Komunal'),
        ('Boshqa', 'Boshqa'),
    )
    type_expense = models.CharField(max_length=30, choices=CHOICES1)
    commentary = models.TextField()

    def __str__(self):
        return self.user.username
