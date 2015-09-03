from django.db import models
from django.utils.deconstruct import deconstructible
from django_dropbox.storage import DropboxStorage

# If you are using django 1.8, you'll get a "Cannot Serialize" error.  A quick workaround is:
@deconstructible
class MyDropboxStorage(DropboxStorage):
    pass

STORAGE = MyDropboxStorage()

class Person(models.Model):
     photo = models.ImageField(upload_to='photos', storage=STORAGE, null=True, blank=True)
     resume = models.FileField(upload_to='resumes', storage=STORAGE, null=True, blank=True)
