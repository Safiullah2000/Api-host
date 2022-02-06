# Generated by Django 4.0.1 on 2022-01-30 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=100)),
                ('is_completed', models.BooleanField(default=False)),
                ('last_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
