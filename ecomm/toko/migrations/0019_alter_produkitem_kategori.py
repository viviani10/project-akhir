# Generated by Django 4.2.1 on 2023-05-31 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0018_delete_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkitem',
            name='kategori',
            field=models.CharField(choices=[('K', 'Kaos/Kemeja'), ('J_S', 'Jaket/Sweater'), ('C', 'Celana')], max_length=4),
        ),
    ]
