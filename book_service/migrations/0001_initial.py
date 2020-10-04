# Generated by Django 2.2.7 on 2020-10-04 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(default='', max_length=64, verbose_name='用户名称')),
                ('phone', models.CharField(default='1', max_length=200, verbose_name='电话号码')),
            ],
            options={
                'verbose_name': '通信录用户',
                'verbose_name_plural': '通信录用户',
            },
        ),
    ]
