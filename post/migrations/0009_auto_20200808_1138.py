# Generated by Django 3.0.7 on 2020-08-08 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20200807_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='replied_commentid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='post.Comment'),
        ),
    ]
