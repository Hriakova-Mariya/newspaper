# Generated by Django 4.2.9 on 2024-01-22 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='CommentUser',
            new_name='commentUser',
        ),
    ]