from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Import custom models
from .models import *

#-------------------------------------------------------------------------------
# HOW-TO NOTES

#To make a field read only
#    readonly_fields = ('isActive', )

#To define the fields on the table list display
#    list_display = ('name', 'description', 'isActive')

#To define fields that are EDITABLE on the table list display direcly
#    list_editable = ('description', 'isActive')

#To define filters
#    list_filter = ('isActive', )
#    with FK us '__' eg. ('vendor__user', ) NOTE: Relationship defined in model

#-------------------------------------------------------------------------------


#Define the User admin site (extends builtin User)
class userprofileInline(admin.StackedInline):
	model = userprofile
	can_delete = False
	verbose_name_plural = 'userprofile'		
class UserAdmin(BaseUserAdmin):
	inlines = (userprofileInline, )
	list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')
	
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


#Define the Vendor admin site
class VendorFilter(admin.SimpleListFilter):
	title = ('Active')
	parameter_name = 'isActive'
	
	def lookups(self, request, model_admin):
		return (
		  (None, ('Active')),
		  ('NotActive', ('Not Active')),
		  
		)
	def choices(self, cl):
		for lookup, title in self.lookup_choices:
			yield {
			  'selected': self.value() == lookup,
			  'query_string': cl.get_query_string({
			    self.parameter_name: lookup,
			  }, []),
			  'display': title,
			}
	def queryset(self, request, queryset):
		if self.value() == None:
			return queryset.filter(isActive = True)
		if self.value() == 'NotActive':
			return queryset.filter(isActive = False)
		
	
class VendorAdmin(admin.ModelAdmin):
	fields = ('name', 'description', 'isActive')
	list_display = ('name', 'description', 'isActive')
	list_editable = ('description', 'isActive')
	list_filter = (VendorFilter, )

admin.site.register(vendor, VendorAdmin)


#Define the Service admin site
class ServiceAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'suppliername')
	
	def suppliername(self, obj):
		return obj.supplier

admin.site.register(service, ServiceAdmin)


#Define the remaining models that do not require special attribution
admin.site.register(appointment)
admin.site.register(schedule)
