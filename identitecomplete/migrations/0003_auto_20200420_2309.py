# Generated by Django 2.2.6 on 2020-04-20 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identitecomplete', '0002_auto_20200420_2223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='completeidentity',
            old_name='benefiaciary_mother_first_name',
            new_name='father_fullname_beneficiary',
        ),
        migrations.RenameField(
            model_name='completeidentity',
            old_name='beneficiary_father_first_name',
            new_name='mother_fullname_benefiaciary',
        ),
    ]