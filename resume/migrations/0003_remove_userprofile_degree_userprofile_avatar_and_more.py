# Generated by Django 4.2 on 2023-04-19 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_remove_skill_intro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='degree',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='background',
            field=models.ImageField(blank=True, null=True, upload_to='background'),
        ),
    ]