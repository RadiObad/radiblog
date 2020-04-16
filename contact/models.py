from django.db import models
from blog.models import ModelBase
# Create your models here.

class Web(ModelBase):
    we = models.TextField('We')
    phone = models.CharField('Phone', max_length = 10)
    email = models.EmailField('Email', max_length = 200)
    address = models.CharField('Address', max_length = 200)

    class Meta:
        verbose_name = 'Web'
        verbose_name_plural = 'Webs'

    def __str__(self):
        return self.we

class Socialnetworks(ModelBase):
    facebook = models.URLField('Facebook')
    twitter = models.URLField('Twitter')
    instagram = models.URLField('Instagram')

    class Meta:
        verbose_name = 'Social Network'
        verbose_name_plural = 'Social Networks'

    def __str__(self):
        return self.facebook

class Contact(ModelBase):
    name = models.CharField('Name', max_length = 100)
    surnames = models.CharField('Surnames', max_length = 150)
    mail = models.EmailField('Email', max_length = 200)
    affair = models.CharField('Affair', max_length = 100)
    message = models.TextField('Message')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.affair

class Subscriber(ModelBase):
    mail = models.EmailField('Email', max_length = 200)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.mail



