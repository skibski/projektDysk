# Generated by Django 3.2 on 2021-05-09 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dysk', '0013_remove_katalog_id_katalogu_nadrzednego'),
    ]

    operations = [
        migrations.AddField(
            model_name='katalog',
            name='id_katalogu_nadrzednego',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dysk.katalog'),
        ),
    ]
