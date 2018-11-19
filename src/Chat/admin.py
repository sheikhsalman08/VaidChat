from django.contrib import admin

from .models import Msg,ChatRoom

# Register your models here.

admin.site.register([ChatRoom,Msg])