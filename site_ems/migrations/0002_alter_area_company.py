# Generated by Django 3.2.2 on 2021-05-19 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_ems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_ems.company'),
        ),
    ]