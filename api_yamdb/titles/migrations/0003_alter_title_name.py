# Generated by Django 3.2 on 2023-02-15 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0002_auto_20230215_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.TextField(max_length=256),
        ),
    ]