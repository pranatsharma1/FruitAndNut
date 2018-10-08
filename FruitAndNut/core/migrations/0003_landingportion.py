# Generated by Django 2.1.1 on 2018-09-27 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180927_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPortion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider', models.ImageField(unique=True, upload_to='images/landing_slider/')),
                ('active', models.BooleanField(default=True)),
                ('heading', models.CharField(blank=True, max_length=200, null=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]