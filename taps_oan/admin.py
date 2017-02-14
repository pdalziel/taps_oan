from django.contrib import admin
from taps_oan.models import Pub, Beer
from taps_oan.models import UserProfile

class PubAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
	
class BeerAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub', 'url')
	
admin.site.register(Pub, PubAdmin)
admin.site.register(Beer,BeerAdmin)
admin.site.register(UserProfile)