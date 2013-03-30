from django import forms
from django.contrib import admin
from models import SiteElement, Page, Document, GalleryElement, FlatImage, Slider, Testimonial
from orderable import OrderableAdmin


class SiteElementAdmin(admin.ModelAdmin):
    class Media:
        js = ['js/jquery.js', 'js/jquery.tinymce.js', 'js/admin_tinymce.js']

admin.site.register(SiteElement, SiteElementAdmin)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ['file', 'name', 'pick']

    def pick(self, obj):
        return '<a class="file-picker" href="%s">pick</a>' % obj.file.url
    pick.allow_tags = True

    class Media:
        js = ['js/jquery.js', 'js/jquery.tinymce.js', 'tiny_mce/tiny_mce_popup.js', 'js/admin_tinymce_popup.js']

admin.site.register(Document, DocumentAdmin)


class FlatImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'name', 'thumbnail_image']

    def thumbnail_image(self, obj):
        return '<a class="image-picker" href="%s"><img src="%s">Pick</a>' % (obj.image.url, obj.image.thumbnail.url())
    thumbnail_image.allow_tags = True

    class Media:
        js = ['js/jquery.js', 'js/jquery.tinymce.js', 'tiny_mce/tiny_mce_popup.js', 'js/admin_tinymce_popup.js']

admin.site.register(FlatImage, FlatImageAdmin)


class PageAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PageAdminForm, self).__init__(*args, **kwargs)
        self.fields['meta_keywords'].widget.attrs['class'] = 'plain'
        self.fields['meta_description'].widget.attrs['class'] = 'plain'

    class Meta:
        model = Page


class PageAdmin(OrderableAdmin):
    form = PageAdminForm
    list_display = ('slug', 'title')

    class Media:
        js = ['js/jquery.js', 'js/jquery.tinymce.js', 'js/admin_tinymce.js']

admin.site.register(Page, PageAdmin)


class GalleryElementAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')

admin.site.register(GalleryElement, GalleryElementAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', )

    def thumbnail(self, obj):
        return '<img src="%s">' % obj.image.thumbnail.url()
    thumbnail.allow_tags = True

admin.site.register(Slider, SliderAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', )

    class Media:
        js = ['js/jquery.js', 'js/jquery.tinymce.js', 'js/admin_tinymce.js']

admin.site.register(Testimonial, TestimonialAdmin)