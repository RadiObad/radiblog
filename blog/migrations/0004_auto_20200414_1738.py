# Generated by Django 2.2.6 on 2020-04-14 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_delete_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Socialnetworks',
        ),
        migrations.DeleteModel(
            name='Subscriber',
        ),
        migrations.DeleteModel(
            name='Web',
        ),
    ]