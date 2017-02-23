from django.contrib import admin
from taps_oan.models import Pub, Beer
from taps_oan.models import UserProfile

class PubAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_beers = ('beers')
    
class BeerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

	
admin.site.register(Pub, PubAdmin)
admin.site.register(Beer,BeerAdmin)
admin.site.register(UserProfile)
