# Generated by Django 5.0.6 on 2024-07-05 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_alter_vacancy_options_alter_vacancy_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='namee'),
        ),
    ]
