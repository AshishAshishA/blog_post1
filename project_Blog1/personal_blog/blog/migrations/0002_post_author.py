# Generated by Django 4.2.6 on 2023-10-30 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='ashish', max_length=30),
            preserve_default=False,
        ),
    ]
