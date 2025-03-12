from django.contrib import admin
#first Import the models
from .models import Messages, Players, Teams, Responses
# Register your models here.
admin.site.register(Messages)
admin.site.register(Responses)
admin.site.register(Players)
admin.site.register(Teams)