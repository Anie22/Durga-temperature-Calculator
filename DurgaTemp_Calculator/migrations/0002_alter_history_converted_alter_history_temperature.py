# Generated by Django 4.2.1 on 2023-09-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DurgaTemp_Calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='converted',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='history',
            name='temperature',
            field=models.FloatField(),
        ),
    ]
