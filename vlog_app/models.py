
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=70,
        verbose_name='Заголовок'
    )
    img = models.ImageField(
        verbose_name="Пост",
        upload_to="media/%Y/%m/%d"
    )
    description = models.TextField(
        verbose_name="chernovik"
    )
    is_delete = models.BooleanField(
        verbose_name="udalen",
        default=False
    )
    create_data = models.DateTimeField(
        verbose_name="data sozdaniya",
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        verbose_name="data sozdaiya",
        auto_now=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )