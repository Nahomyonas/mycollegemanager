# Generated by Django 3.0.7 on 2020-07-02 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_preferedlocations_userpreferences'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpreferences',
            name='minprice',
            field=models.IntegerField(default=5000),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='maxprice',
            field=models.IntegerField(default=10000),
        ),
    ]
