from django.db import models
from django.conf import settings


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext as _
import datetime


class User(AbstractBaseUser):

    username = None
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    manner = models.IntegerField(default=50, auto_created=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['address', 'manner', 'name']

    def __str__(self):
        return self.email


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, name, address, manner, password=None):
        user = self.model(
            email=self.normalize_email(email),
            address=address,
            manner=manner,
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, name, address, manner, password):
        user = self.create_user(
            email,
            password=password,
            address=address,
            manner=manner,
            name=name,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, address, manner, password):
        user = self.create_user(
            email,
            password=password,
            address=address,
            manner=manner,
            name="True",
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class Post(models.Model):
    CATEGORY_CHOICES = {('디지털/가전', '디지털/가전'), ('가구/인테리어', '가구/인테리어'), ('유아동/유아도서', '유아동/유아도서'), ('생활/가공식품', '생활/가공식품'), ('스포츠/레저', '스포츠/레저'), ('여성잡화', '여성잡화'),
                        ('여성의류', '여성의류'), ('남성패션/잡화', '남성패션/잡화'), ('게임/취미', '게임/취미'), ('뷰티/미용', '뷰티/미용'), ('반려동물용품', '반려동물용품'), ('도서/티켓/음반', '도서/티켓/음반'), ('식물', '식물'), ('기타 중고물품', '기타 중고물품'), ('삽니다', '삽니다')}

    author = models.ForeignKey('daangns.User', on_delete=models.CASCADE)
    image = models.URLField(null=False)
    title = models.CharField(max_length=30, null=False)
    category = models.CharField(
        choices=CATEGORY_CHOICES, max_length=10, blank=True, null=False)
    price = models.IntegerField(null=False)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated_at',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        'daangns.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('daangns.User', on_delete=models.CASCADE)

    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.text
