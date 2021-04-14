# Generated by Django 3.2 on 2021-04-14 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dysk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_dysku', models.IntegerField(default=0)),
                ('rozmiar_calkowity', models.IntegerField(default=0)),
                ('rozmiar_zajety', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Katalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_katalogu', models.IntegerField(default=0)),
                ('nazwa', models.CharField(max_length=200)),
                ('sciezka_do_katalogu', models.CharField(max_length=200)),
                ('id_dysku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dysk.dysk')),
            ],
        ),
        migrations.CreateModel(
            name='Uzytkownik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_uzytkownika', models.IntegerField(default=0)),
                ('nazwa', models.CharField(max_length=200)),
                ('haslo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Plik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pliku', models.IntegerField(default=0)),
                ('nazwa', models.CharField(max_length=200)),
                ('typ_pliku', models.CharField(max_length=200)),
                ('sciezka_do_pliku', models.CharField(max_length=200)),
                ('id_katalogu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dysk.katalog')),
            ],
        ),
        migrations.AddField(
            model_name='dysk',
            name='id_uzytkownika',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dysk.uzytkownik'),
        ),
    ]
