# Generated by Django 3.0 on 2019-12-11 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialieven', '0006_auto_20191211_1245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activiteit',
            options={'ordering': ['datum', 'starttijd']},
        ),
    ]