# Generated by Django 5.0.6 on 2024-07-06 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest_book', '0002_rename_guestbook_guestbookposts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GuestBookPosts',
            new_name='Post',
        ),
    ]
