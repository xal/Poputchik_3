from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField(max_length=255, blank=True, default='')
    is_driver = models.BooleanField(default=False)
    coord_from = models.CharField(max_length=50)
    coord_to = models.CharField(max_length=50)

    def __unicode__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        self.user.delete()
        super(Profile, self).delete(*args, **kwargs)
