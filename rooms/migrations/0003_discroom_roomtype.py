# Generated by Django 3.0.7 on 2020-07-01 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_discroom_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='discroom',
            name='roomtype',
            field=models.CharField(default='private', max_length=10),
        ),
    ]
