# Generated by Django 4.2.2 on 2023-07-01 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formatapp', '0008_amphitheatre_user_seminarhall_user_sportsground_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditorium',
            name='describe',
            field=models.TextField(max_length=10),
        ),
    ]
