# Generated by Django 5.1.3 on 2024-11-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0002_photo_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]