# Generated by Django 3.2.7 on 2021-09-16 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.JSONField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_food.customer', verbose_name='Покупатель')),
            ],
        ),
    ]