# Generated by Django 5.0.2 on 2024-09-15 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_commentuser_comment_commentuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dateCreation',
            field=models.DateTimeField(auto_now=True),
        ),
    ]