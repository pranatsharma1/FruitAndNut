# Generated by Django 2.1.1 on 2019-01-27 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0062_auto_20190127_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='content',
            field=models.FileField(upload_to='files/download/%Y-%m-%d'),
        ),
        migrations.AlterField(
            model_name='download',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
