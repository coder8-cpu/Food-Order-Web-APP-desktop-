# Generated by Django 4.0.5 on 2022-07-01 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_alter_review_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='img',
        ),
    ]