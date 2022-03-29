# Generated by Django 4.0.3 on 2022-03-25 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restuarant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='city',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant', to='restuarant.city'),
        ),
    ]
