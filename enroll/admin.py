from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)   # equivalent to admin.site.register(User, UserAdmin)
class UserAdmin(admin.ModelAdmin):
 list_display = ('id', 'name', 'email', 'password')

#this is older method of writing code
 #class UserAdmin(admin.ModelAdmin):
  #  list_display = ('id', 'name', 'email', 'password')

#admin.site.register(User, UserAdmin)  # Explicitly registering the model"""