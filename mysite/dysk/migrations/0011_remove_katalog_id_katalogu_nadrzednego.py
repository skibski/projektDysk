# Generated by Django 3.2 on 2021-05-08 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dysk', '0010_katalog_id_katalogu_nadrzednego'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='katalog',
            name='id_katalogu_nadrzednego',
        ),
    ]