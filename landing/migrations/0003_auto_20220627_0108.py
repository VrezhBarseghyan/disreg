# Generated by Django 3.2.5 on 2022-06-26 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20220627_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fullquestion',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='fullquestion',
            name='question',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
