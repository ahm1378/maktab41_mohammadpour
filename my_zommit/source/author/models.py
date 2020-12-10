from django.db import models

# Create your models here.
from  django.contrib.auth import get_user_model
from lib.models import BaseModel

User=get_user_model()
class Author(BaseModel):
    avatar=models.ImageField(verbose_name="avatar",upload_to="author/avatars/")
    user =models.OneToOneField(User,related_name="author",on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name="Author"
        verbose_name_plural="Authors"
        db_table = "author"