# Generated by Django 3.1 on 2020-08-25 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
