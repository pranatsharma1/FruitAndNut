# Generated by Django 2.1.5 on 2020-01-24 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admissionprocess',
            options={'verbose_name': 'Admission Process', 'verbose_name_plural': 'Admission Process'},
        ),
        migrations.AlterField(
            model_name='collegeawards',
            name='session',
            field=models.CharField(choices=[('2011-2012', '2011-2012'), ('2012-2013', '2012-2013'), ('2013-2014', '2013-2014'), ('2014-2015', '2014-2015'), ('2015-2016', '2015-2016'), ('2016-2017', '2016-2017'), ('2017-2018', '2017-2018'), ('2018-2019', '2018-2019'), ('2019-2020', '2019-2020'), ('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024'), ('2024-2025', '2024-2025')], default=2020, max_length=10, verbose_name='year'),
        ),
        migrations.AlterField(
            model_name='universityawards',
            name='session',
            field=models.CharField(choices=[('2011-2012', '2011-2012'), ('2012-2013', '2012-2013'), ('2013-2014', '2013-2014'), ('2014-2015', '2014-2015'), ('2015-2016', '2015-2016'), ('2016-2017', '2016-2017'), ('2017-2018', '2017-2018'), ('2018-2019', '2018-2019'), ('2019-2020', '2019-2020'), ('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024'), ('2024-2025', '2024-2025')], default=2020, max_length=10, verbose_name='year'),
        ),
    ]
