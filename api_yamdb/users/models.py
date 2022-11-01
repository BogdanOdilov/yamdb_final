from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    CHOICES = (
        (USER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор')
    )

    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        null=True,
        unique=True
    )

    email = models.EmailField(
        'Адрес электронной почты',
        max_length=254,
        unique=True
    )

    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=True,
        default=''
    )

    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=True,
        default=''
    )

    bio = models.TextField(
        blank=True,
        default=''
    )

    role = models.CharField(
        'Роль',
        max_length=20,
        choices=CHOICES,
        default=USER
    )

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ('username',)
        constraints = (
            models.CheckConstraint(
                check=~models.Q(username__iexact='me'),
                name='username_is_not_me'
            ),
        )

    def __str__(self) -> str:
        return 'Пользовтель {} роль {}'.format(
            self.username,
            self.role
        )
