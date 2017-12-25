from django.contrib import admin
from .models import *
# Register your models here.


class MessageInline(admin.StackedInline):
    model = Message
    extra = 3

class UserAdmin(admin.ModelAdmin):
    messages = [MessageInline]


#admin.site.register(UserAdmin)
admin.site.register(Message)