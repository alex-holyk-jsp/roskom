# Generated by Django 3.1.1 on 2020-09-04 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('domain', models.CharField(blank=True, default='', max_length=200)),
                ('ip', models.CharField(max_length=15)),
                ('owner_ip', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
