from django.contrib import admin
from .models import *


# Register your models here.
admin.site.site_title = '母婴后台系统'
admin.site.site_header = '母婴电商后台管理系统'
admin.site.index_title = '母婴管理平台'

@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    list_display = [x for x in list(Types._meta._forward_fields_map.keys())]
    search_fields = ['firsts', 'seconds']
    list_filter = ['firsts']


@admin.register(CommodityInfos)
class CommodityInfosAdmin(admin.ModelAdmin):
    list_display = [x for x in list(CommodityInfos._meta._forward_fields_map.keys())]
    list_display.append('colored_name')
    search_fields = ['name']
    date_hierarchy = 'created'
    save_as = True

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'types':
            db_field.choices = [(x['seconds'], x['seconds']) for x in Types.objects.values('seconds')]
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = []
        else:
            self.readonly_fields = ['types']

        return self.readonly_fields


