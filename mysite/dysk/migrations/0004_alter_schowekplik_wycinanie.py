# Generated by Django 3.2 on 2021-06-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dysk', '0003_alter_schowekplik_wycinanie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schowekplik',
            name='wycinanie',
            field=models.BooleanField(default=False),
        ),
    ]
