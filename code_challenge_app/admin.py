from django.contrib import admin
from .models import Email_template, Email

class Email_templateAdmin(admin.ModelAdmin):
    search_fields = ('template_name',)
    list_filter = ('template_name',)
    list_display = ('id','template_name','subject','content')
    ordering = ('id',)
    list_display_links = ('template_name',)
admin.site.register(Email_template, Email_templateAdmin)

class EmailAdmin(admin.ModelAdmin):
    
    raw_id_fields = ('user','template')
    readonly_fields = ('subject','content')
    exclude = ('from_email',)
    search_fields = ('user__username','template__template_name','from_email')
    list_filter = ('template','from_email','creation_date')
    list_display = ('id','template','user','subject','content','from_email','creation_date')
    ordering = ('id',)
    list_display_links = ('id','template')
admin.site.register(Email, EmailAdmin)

