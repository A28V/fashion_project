from django.contrib import admin
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from catalog_settings.models import *
# Register your models here.


class CatalogAdmin(admin.ModelAdmin):
	def validate_url(value):
		url_validator = URLValidator()
		try:
			url_validator(value)
		except:
			raise ValidationError("Invalid URL")
	def formfield_for_dbfield(self, db_field, **kwargs):
		if db_field.name == 'url':
			kwargs['validators'] = [validate_url]
		return super().formfield_for_dbfield(db_field, **kwargs)


admin.site.register(Category)
admin.site.register(products)