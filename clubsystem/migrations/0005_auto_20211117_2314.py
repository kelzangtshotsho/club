# Generated by Django 3.2.9 on 2021-11-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubsystem', '0004_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Club', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='record',
            name='Sl_No',
        ),
        migrations.AddField(
            model_name='record',
            name='Name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]