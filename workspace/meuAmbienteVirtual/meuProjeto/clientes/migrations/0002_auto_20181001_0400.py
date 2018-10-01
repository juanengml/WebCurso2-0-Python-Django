# Generated by Django 2.1.1 on 2018-10-01 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='panda@panda.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='idade',
            field=models.IntegerField(default=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='salario',
            field=models.DecimalField(decimal_places=2, default=900, max_digits=10),
            preserve_default=False,
        ),
    ]
