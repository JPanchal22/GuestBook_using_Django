# Generated by Django 3.1.5 on 2021-01-24 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guestbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
