# Generated by Django 3.0 on 2019-12-05 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_straat'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='Huisnummer',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='Postcode',
            field=models.CharField(default='1234ab', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='Woonplaats',
            field=models.CharField(default='amsterdam', max_length=64),
            preserve_default=False,
        ),
    ]
