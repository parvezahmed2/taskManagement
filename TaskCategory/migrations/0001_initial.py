# Generated by Django 4.2.8 on 2023-12-16 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TaskModel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskCategorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=50)),
                ('tasks', models.ManyToManyField(to='TaskModel.tasks')),
            ],
        ),
    ]
