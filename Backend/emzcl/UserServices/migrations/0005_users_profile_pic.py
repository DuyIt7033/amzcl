# Generated by Django 5.1.5 on 2025-02-06 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserServices', '0004_remove_users_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/'),
        ),
    ]
