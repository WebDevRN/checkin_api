# Generated by Django 2.1.3 on 2018-11-29 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20181128_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='closed_registration',
            field=models.BooleanField(default=False, verbose_name='closed registration'),
        ),
        migrations.AlterField(
            model_name='subeventcheck',
            name='entrance_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='entrance date/time'),
        ),
        migrations.AlterField(
            model_name='subeventcheck',
            name='exit_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='exit date/time'),
        ),
    ]
