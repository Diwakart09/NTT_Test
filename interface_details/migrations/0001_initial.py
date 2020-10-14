# Generated by Django 3.1 on 2020-10-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='router',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sapid', models.CharField(max_length=18)),
                ('hostname', models.CharField(max_length=14)),
                ('loopback', models.GenericIPAddressField()),
                ('mac_address', models.CharField(max_length=17)),
            ],
        ),
    ]