from django.contrib import admin
from . models import Project
from . models import Detail
# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'tech','image')
    list_filter = ('title', 'date_add')
    search_fields = ('title',)



@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'tech','image_detail')
    list_filter = ('title', 'date_add')
    search_fields = ('title',)