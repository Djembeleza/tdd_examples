# Generated by Django 4.2.6 on 2023-11-16 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_item_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.TextField(default=''),
        ),
    ]
