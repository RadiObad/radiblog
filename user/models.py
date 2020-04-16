from django.db import models
from blog.models import ModelBase
# Create your models here.
class Author(ModelBase):
    name = models.CharField('Names',max_length = 100)
    surnames = models.CharField('Surnames',max_length = 120)
    email = models.EmailField('Email', max_length = 200)
    description = models.TextField('Description')
    referential_image = models.ImageField('Referential image', null = True, blank = True,upload_to = 'authors/')
    web = models.URLField('Web', null = True, blank = True)
    facebook = models.URLField('Facebook', null = True, blank = True)
    twitter = models.URLField('Twitter', null = True, blank = True)
    instagram = models.URLField('Instagram', null = True, blank = True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return '{0},{1}'.format(self.surnames,self.name)
