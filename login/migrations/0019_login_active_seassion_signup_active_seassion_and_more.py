# Generated by Django 4.0.5 on 2022-07-07 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_cart_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='active_seassion',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='active_seassion',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='c_k',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
    ]
