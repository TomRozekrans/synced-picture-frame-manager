# Generated by Django 4.2.3 on 2023-11-24 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selector', '0008_picturegroup_admins'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'permissions': [('view_devices', 'Can view devices'), ('view_device_admin', 'Can view all devices')]},
        ),
        migrations.AlterModelOptions(
            name='picturegroup',
            options={'permissions': [('view_picturegroup_admin', 'Can view all picture groups')]},
        ),
    ]