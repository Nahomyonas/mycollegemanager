# Generated by Django 2.2.12 on 2020-07-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200702_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercolleges',
            name='deadline',
            field=models.DateField(default='0000-00-00', null=True),
        ),
        migrations.AlterField(
            model_name='usercolleges',
            name='location',
            field=models.CharField(default='', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='usercolleges',
            name='myrating',
            field=models.IntegerField(default=5, null=True),
        ),
        migrations.AlterField(
            model_name='usercolleges',
            name='price',
            field=models.BigIntegerField(default=0, null=True),
        ),
    ]
