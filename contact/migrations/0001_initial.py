# Generated by Django 2.2.6 on 2020-04-14 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modification_date', models.DateField(auto_now=True, verbose_name='Modification date')),
                ('removal_date', models.DateField(auto_now=True, verbose_name='Elimination Date')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('surnames', models.CharField(max_length=150, verbose_name='Surnames')),
                ('mail', models.EmailField(max_length=200, verbose_name='Email')),
                ('affair', models.CharField(max_length=100, verbose_name='Affair')),
                ('message', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Socialnetworks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modification_date', models.DateField(auto_now=True, verbose_name='Modification date')),
                ('removal_date', models.DateField(auto_now=True, verbose_name='Elimination Date')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('twitter', models.URLField(verbose_name='Twitter')),
                ('instagram', models.URLField(verbose_name='Instagram')),
            ],
            options={
                'verbose_name': 'Social Network',
                'verbose_name_plural': 'Social Networks',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modification_date', models.DateField(auto_now=True, verbose_name='Modification date')),
                ('removal_date', models.DateField(auto_now=True, verbose_name='Elimination Date')),
                ('mail', models.EmailField(max_length=200, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscribers',
            },
        ),
        migrations.CreateModel(
            name='Web',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modification_date', models.DateField(auto_now=True, verbose_name='Modification date')),
                ('removal_date', models.DateField(auto_now=True, verbose_name='Elimination Date')),
                ('we', models.TextField(verbose_name='We')),
                ('phone', models.CharField(max_length=10, verbose_name='Phone')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
            ],
            options={
                'verbose_name': 'Web',
                'verbose_name_plural': 'Webs',
            },
        ),
    ]