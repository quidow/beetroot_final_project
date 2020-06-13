from django.db import models


class Amenity(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Service(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    services = models.ManyToManyField(Service)


class Room(models.Model):
    hotel = models.ForeignKey(to=Hotel, on_delete=models.CASCADE)
    amenities = models.ManyToManyField(Amenity)
    persons = models.SmallIntegerField(default=1)


class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Booking(models.Model):
    room = models.ForeignKey(to=Room, on_delete=models.PROTECT)
    check_in = models.DateField()
    check_out = models.DateField()
    clients = models.ManyToManyField(Client)
    confirmed = models.BooleanField()
