# Generated by Django 4.0.4 on 2022-04-27 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_restaurant_image_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='image_url',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
