from django.contrib import admin
from models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )

#    def preview(self, obj):
#        return '<img src="%s">' % (obj.icon.url)
#    preview.allow_tags = True

admin.site.register(Profile, ProfileAdmin)
