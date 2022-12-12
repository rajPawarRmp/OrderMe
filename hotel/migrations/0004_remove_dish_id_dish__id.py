# Generated by Django 4.0.1 on 2022-11-09 22:43

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_alter_dish_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='id',
        ),
        migrations.AddField(
            model_name='dish',
            name='_id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
