# Generated by Django 3.2 on 2021-05-08 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dysk', '0009_remove_katalog_id_katalogu_nadrzednego'),
    ]

    operations = [
        migrations.AddField(
            model_name='katalog',
            name='id_katalogu_nadrzednego',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dysk.katalog'),
            preserve_default=False,
        ),
    ]
