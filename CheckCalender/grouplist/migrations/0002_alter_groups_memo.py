# Generated by Django 4.0.4 on 2022-05-14 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grouplist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='memo',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]