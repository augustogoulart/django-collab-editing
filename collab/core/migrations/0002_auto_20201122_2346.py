# Generated by Django 3.1.3 on 2020-11-22 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selection',
            name='selection',
            field=models.TextField(null=True),
        ),
    ]