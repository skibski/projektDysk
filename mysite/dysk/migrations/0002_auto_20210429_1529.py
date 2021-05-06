# Generated by Django 3.2 on 2021-04-29 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dysk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dysk',
            name='id_uzytkownika',
        ),
        migrations.AddField(
            model_name='dysk',
            name='id_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
