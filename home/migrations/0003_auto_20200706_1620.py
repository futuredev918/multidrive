# Generated by Django 3.0.8 on 2020-07-06 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200706_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='dropbox',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='setting',
            name='google_projectid',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='setting',
            name='google_token',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='setting',
            name='one_client',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='setting',
            name='one_security',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='setting',
            name='one_tenant',
            field=models.CharField(max_length=255),
        ),
    ]