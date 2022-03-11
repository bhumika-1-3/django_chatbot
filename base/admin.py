from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.models import Group
[Greeting]
"Hi, how are you?", "Is anyone there?", "Hello", "What's up?!", "hey there!"

["Goodbye"]
"Bye", "See you later", "Goodbye", "I need to go now."
# Register your models here.
admin.site.unregister(Group)
admin.site.register(CustomUser)

