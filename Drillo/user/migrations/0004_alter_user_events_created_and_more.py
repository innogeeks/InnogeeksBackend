# Generated by Django 4.2.2 on 2023-07-13 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_events_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='events_created',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='events_participated',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
