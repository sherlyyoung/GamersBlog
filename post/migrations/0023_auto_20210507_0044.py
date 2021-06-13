# Generated by Django 3.0.7 on 2021-05-06 23:44

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0022_auto_20210507_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postimage',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=85, size=[300, 300], upload_to='post_images'),
        ),
    ]
