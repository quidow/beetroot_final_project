from django.db import models
from django.contrib.auth import get_user_model


class Amenity(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    icon = models.ImageField(blank=True, null=True, verbose_name='Иконка')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Удобство"
        verbose_name_plural = "Удобства"


class Service(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    icon = models.ImageField(blank=True, null=True, verbose_name='Иконка')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Hotel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    services = models.ManyToManyField(Service, blank=True, verbose_name='Услуги')
    owners = models.ManyToManyField(to=get_user_model(), verbose_name='Администраторы')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Отель"
        verbose_name_plural = "Отели"


# class HotelAdminRelation(models.Model):
#     admin = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Администратор')
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Отель')
#
#     class Meta:
#         verbose_name = "Администратор отеля"
#         verbose_name_plural = "Администраторы отелей"
#         constraints = [
#             models.UniqueConstraint(fields=['admin', 'hotel'], name='unique admin and hotel')
#         ]


class HotelPhoto(models.Model):
    photo = models.ImageField(verbose_name='Фото')
    hotel = models.ForeignKey(Hotel, related_name='photos', on_delete=models.CASCADE, verbose_name='Отель')

    class Meta:
        ordering = ["pk"]
        verbose_name = "Фото отеля"
        verbose_name_plural = "Фото отелей"


class Room(models.Model):
    hotel = models.ForeignKey(to=Hotel, on_delete=models.CASCADE, verbose_name='Отель')
    amenities = models.ManyToManyField(Amenity, blank=True, verbose_name='Удобства')
    persons = models.PositiveSmallIntegerField(default=1, verbose_name='Количество человек')

    class Meta:
        ordering = ["pk"]
        verbose_name = "Номер"
        verbose_name_plural = "Номера"


class RoomPhoto(models.Model):
    photo = models.ImageField(verbose_name='Фото')
    room = models.ForeignKey(Room, related_name='photos', on_delete=models.CASCADE, verbose_name='Номер')

    class Meta:
        ordering = ["pk"]
        verbose_name = "Фото номера"
        verbose_name_plural = "Фото номеров"

# class Client(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#
#
# class Booking(models.Model):
#     room = models.ForeignKey(to=Room, on_delete=models.PROTECT)
#     check_in = models.DateField()
#     check_out = models.DateField()
#     clients = models.ManyToManyField(Client)
#     confirmed = models.BooleanField()
