# Generated by Django 3.0.6 on 2020-06-15 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memopolis', '0011_meme_accepted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='author_id',
        ),
    ]
