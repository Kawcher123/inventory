# Generated by Django 3.1.2 on 2020-12-23 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20201223_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
