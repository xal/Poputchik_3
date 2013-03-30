from django.db import models
from stdimage import StdImageField
from orderable import OrderField
from django.template.defaultfilters import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize

class SiteElement(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    file = models.FileField(upload_to='uploads/user-files', max_length=255)


class Page(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=100)
    meta_keywords = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    position = OrderField()

    def __unicode__(self):
        return self.slug

    class Meta:
        ordering = ('position',)


class GalleryElement(models.Model):
    title = models.CharField(max_length=100, help_text='small title text')
    description = models.CharField(max_length=200, help_text='small description under image')
    long_description = models.TextField(blank=True, null=True, help_text='description after click on image')
    image = StdImageField(upload_to='uploads/gallery', thumbnail_size=(188, 145), help_text='Optimal size 800x600')
    image_pro = ImageSpecField([ResizeToFill(800, 600), ], image_field='image', format='JPEG', options={'quality': 80})


class FlatImage(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    image = StdImageField(upload_to='uploads/flat-image', thumbnail_size=(100, 100))

    class Meta:
        verbose_name = "Image for HTML Editor"
        verbose_name_plural = "Images for HTML Editor"


class Slider(models.Model):
    image = StdImageField(upload_to='uploads/slider', thumbnail_size=(188, 145), help_text='Optimal size 795x359')
    image_pro = ImageSpecField([SmartResize(795, 359), ], image_field='image', format='JPEG', options={'quality': 80})
    description = models.TextField(blank=True)
    enabled = models.BooleanField(default=True)


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    position = OrderField()

    def __unicode__(self):
        return 'Testimonial from %s' % self.name

    class Meta:
        ordering = ('position',)