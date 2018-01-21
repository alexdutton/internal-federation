# Generated by Django 2.0.1 on 2018-01-20 11:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('infed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceprovider',
            name='changed',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='service_name',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
