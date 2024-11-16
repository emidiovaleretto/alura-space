# Generated by Django 5.1.3 on 2024-11-14 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='category',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('GALAXIA', 'Galaxia'), ('PLANETA', 'Planeta'), ('ESTRELLA', 'Estrela')], default='', max_length=100),
        ),
    ]