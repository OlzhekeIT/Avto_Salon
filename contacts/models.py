from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    state_choice = (
        ('ALA', 'Almaty'),
        ('AST', 'Astana'),
        ('SHY', 'Shymkent'),
        ('AKM', 'Akmola Region'),
        ('AKT', 'Aktobe Region'),
        ('ALM', 'Almaty Region'),
        ('ATY', 'Atyrau Region'),
        ('VKO', 'East Kazakhstan Region'),
        ('ZHA', 'Zhambyl Region'),
        ('JET', 'Jetisu Region'),
        ('ZKO', 'West Kazakhstan Region'),
        ('KAR', 'Karaganda Region'),
        ('KOS', 'Kostanay Region'),
        ('KYZ', 'Kyzylorda Region'),
        ('MAN', 'Mangystau Region'),
        ('ABA', 'Abai Region'),
        ('PAV', 'Pavlodar Region'),
        ('SKO', 'North Kazakhstan Region'),
        ('TUR', 'Turkistan Region'),
        ('ULY', 'Ulytau Region'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(choices=state_choice, max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
