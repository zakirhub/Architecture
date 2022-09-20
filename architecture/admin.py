from django.contrib import admin
from architecture.models import Contact, Project, AboutMe, AboutUs, SliderImage

# Register your models here.
@admin.register(Contact)
class AdimnContact(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message']

@admin.register(Project)
class AdimnProject(admin.ModelAdmin):
    list_display = ['title', 'description', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6','date']

@admin.register(AboutMe)
class AdimnContact(admin.ModelAdmin):
    list_display = ['my_description', 'my_image']

@admin.register(AboutUs)
class AdimnContact(admin.ModelAdmin):
    list_display = ['company_description', 'company_image']

@admin.register(SliderImage)
class AdimnContact(admin.ModelAdmin):
    list_display = ['slider_image1', 'slider_image2', 'slider_image3']

