# Generated by Django 3.2.9 on 2021-11-13 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubsystem', '0003_alter_photo_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sl_No', models.IntegerField()),
                ('Date', models.DateField()),
                ('Time', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
                ('Activity', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Record',
            },
        ),
    ]
