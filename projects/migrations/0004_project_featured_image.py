# Generated by Django 3.2.6 on 2021-08-14 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210814_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default', null=True, upload_to=''),
        ),
    ]
