from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Timestampable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        super().save()


GENDER_CHOICES = (
    (1, "Male"),
    (2, "Female"),
    (3, "Others"))


class UserProfile(Timestampable):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.PositiveIntegerField("Gender", choices=GENDER_CHOICES)
    birthdate = models.DateField("Birthday", null=True, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


DISTRICT_CHOICES = (
    (1, "Achham"),
    (2, "Arghakhanchi"),
    (3, "Baglung"),
    (4, "Baitadi"),
    (5, "Bajhang"),
    (6, "Bajura"),
    (7, "Banke"),
    (8, "Bara"),
    (9, "Bardiya"),
    (10, "Bhaktapur"),
    (11, "Bhojpur"),
    (12, "Chitwan"),
    (13, "Dadeldhura"),
    (14, "Dailekh"),
    (15, "Dang"),
    (16, "Darchula"),
    (17, "Dhading"),
    (18, "Dhankuta"),
    (19, "Dhanusa"),
    (20, "Dholkha"),
    (21, "Dolpa"),
    (22, "Doti"),
    (23, "Gorkha"),
    (24, "Gulmi"),
    (25, "Humla"),
    (26, "Ilam"),
    (27, "Jajarkot"),
    (28, "Jhapa"),
    (29, "Jumla"),
    (30, "Kailali"),
    (31, "Kalikot"),
    (32, "Kanchanpur"),
    (33, "Kapilvastu"),
    (34, "Kaski"),
    (35, "Kathmandu"),
    (36, "Kavrepalanchok"),
    (37, "Khotang"),
    (38, "Lalitpur"),
    (39, "Lamjung"),
    (40, "Mahottari"),
    (41, "Makwanpur"),
    (42, "Manang"),
    (43, "Morang"),
    (44, "Mugu"),
    (45, "Mustang"),
    (46, "Myagdi"),
    (47, "Nawalparasi"),
    (48, "Nuwakot"),
    (49, "Okhaldhunga"),
    (50, "Palpa"),
    (51, "Panchthar"),
    (52, "Parbat"),
    (53, "Parsa"),
    (54, "Pyuthan"),
    (55, "Ramechhap"),
    (56, "Rasuwa"),
    (57, "Rautahat"),
    (58, "Rolpa"),
    (59, "Rukum"),
    (60, "Rupandehi"),
    (61, "Salyan"),
    (62, "Sankhuwasabha"),
    (63, "Saptari"),
    (64, "Sarlahi"),
    (65, "Sindhuli"),
    (66, "Sindhupalchok"),
    (67, "Siraha"),
    (68, "Solukhumbu"),
    (69, "Sunsari"),
    (70, "Surkhet"),
    (71, "Syangja"),
    (72, "Tanahu"),
    (73, "Taplejung"),
    (74, "Terhathum"),
    (75, "Udayapur"))


class Address(Timestampable):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line1 = models.CharField(
        "Address Line 1", max_length=255)
    address_line2 = models.CharField(
        "Address Line 2", max_length=255, null=True, blank=True)
    contact_line1 = models.CharField(
        "Contact Line 1", max_length=255)
    contact_line2 = models.CharField(
        "Contact Line 2", max_length=255, null=True, blank=True)
    landmark = models.CharField(
        "Nearest Landmark", max_length=255, null=True, blank=True)
    city = models.CharField("City", max_length=255)
    district = models.PositiveIntegerField(
        "District", choices=DISTRICT_CHOICES)
    billing_address = models.BooleanField("Billing Address", default=False)
    shipping_address = models.BooleanField("Shipping Address", default=False)

    def __str__(self):
        return self.user.username
