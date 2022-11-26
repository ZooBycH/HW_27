from datetime import date

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from users.validators import check_birthdate


class Location(models.Model):
    name = models.CharField(max_length=150, unique=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class UserRole:
    MEMBER = 'member'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    choises = ((MEMBER, 'Пользователь'), (MODERATOR, 'Модератор'), (ADMIN, 'Администратор'))


class User(AbstractUser):
    age = models.PositiveSmallIntegerField(blank=True, null=True, editable=False)
    location = models.ManyToManyField(Location)
    role = models.CharField(choices=UserRole.choises, default=UserRole.MEMBER, max_length=10)
    birth_date = models.DateField(validators=[check_birthdate])
    email = models.EmailField(verbose_name="email address", blank=True,
                              validators=[RegexValidator(
                                  regex="@rambler.ru", inverse_match=True,
                                  message="Регистрация с домена rambler.ru запрещена!")])

    def save(self, *args, **kwargs):
        #self.set_password(self.password)
        self.age = relativedelta(date.today(), self.birth_date).years
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
