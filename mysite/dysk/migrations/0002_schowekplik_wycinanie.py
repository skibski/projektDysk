# Generated by Django 3.2 on 2021-05-31 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dysk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schowekplik',
            name='wycinanie',
            field=models.BooleanField(default=False),
        ),
    ]
