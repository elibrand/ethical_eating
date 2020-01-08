# Generated by Django 3.0.2 on 2020-01-08 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('site', models.URLField()),
                ('review', models.CharField(max_length=500)),
            ],
        ),
    ]
