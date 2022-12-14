# Generated by Django 4.1.2 on 2022-10-31 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='status',
            field=models.CharField(blank=True, choices=[('interieur', 'interieur'), ('exterieur', 'exterieur')], default='interieur', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]
