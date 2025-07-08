from django.contrib import admin
from .models import AboutImage, AboutGalleryImage, Speaker, Schedule, Blog, Contact, Event, TicketBook,User
# Register your models here.
admin.site.register(AboutImage)
admin.site.register(Speaker)
admin.site.register(Schedule)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(AboutGalleryImage)
admin.site.register(Event)
admin.site.register(TicketBook)
admin.site.register(User)




