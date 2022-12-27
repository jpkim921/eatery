# Generated by Django 4.1.4 on 2022-12-27 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_menuitem_meal_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='meal_time',
        ),
    ]