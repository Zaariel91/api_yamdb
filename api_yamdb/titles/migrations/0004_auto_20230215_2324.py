# Generated by Django 3.2 on 2023-02-15 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0003_alter_title_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]
