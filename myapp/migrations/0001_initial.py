# Generated by Django 2.2.7 on 2020-06-24 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=45)),
                ('tz', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Activity_periods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=100)),
                ('end_time', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Users')),
            ],
        ),
    ]
