# Generated by Django 3.2.19 on 2023-09-01 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=20)),
                ('role', models.CharField(choices=[('admin', 'admin'), ('employer', 'employer'), ('help desk', 'help desk'), ('technicien', 'technicien')], default='1', max_length=20)),
                ('password', models.CharField(max_length=21)),
            ],
        ),
    ]
