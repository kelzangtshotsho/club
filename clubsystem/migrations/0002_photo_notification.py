# Generated by Django 3.2.9 on 2021-11-12 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubsystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='notification',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
