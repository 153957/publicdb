# Generated by Django 1.11.12 on 2018-07-06 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inforecords', '0007_on_delete_set_contact_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(blank=True, default='', max_length=20),
            preserve_default=False,
        ),
    ]
