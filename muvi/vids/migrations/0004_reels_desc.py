# Generated by Django 4.0.6 on 2022-09-21 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vids', '0003_alter_reels_reel'),
    ]

    operations = [
        migrations.AddField(
            model_name='reels',
            name='desc',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
