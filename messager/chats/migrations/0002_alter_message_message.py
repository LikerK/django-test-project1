# Generated by Django 4.0.5 on 2022-07-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(max_length=100, verbose_name='Сообщение'),
        ),
    ]
