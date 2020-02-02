from django.contrib import admin

# Register your models here. models.pyのクラスの定義
from .models import Post

admin.site.register(Post)