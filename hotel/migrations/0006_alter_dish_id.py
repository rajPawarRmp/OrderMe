# Generated by Django 4.0.1 on 2022-11-09 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_rename__id_dish_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
