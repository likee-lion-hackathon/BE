# Generated by Django 5.0.7 on 2024-07-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='photo',
            field=models.ImageField(upload_to='pet_photos/'),
        ),
    ]