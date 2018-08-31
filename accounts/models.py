from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from lessons.models import Question, Answer


CORRECTNESS_CHOICES = (
    (1, True),
    (0, False),
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given username, email, and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email='balgabekov9@gmail.com', password=None):
        """
        Creates and saves a superuser with the given username, email, and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=45, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=45)
    second_name = models.CharField(max_length=45)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Progress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    correct = models.IntegerField(default=0, choices=CORRECTNESS_CHOICES)
    time_started = models.DateTimeField()
    time_finished = models.DateTimeField(auto_now_add=True)
    time_spent = models.FloatField()