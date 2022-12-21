from django.contrib import admin

from application.pets.models import Pet


# Register your models here.

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    model = Pet
    fields = ('name', 'created_at', 'updated_at', 'status')
    readonly_fields = ('id', 'created_at', 'updated_at')
    search_fields = ('name', 'status')
