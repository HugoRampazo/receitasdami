# Generated by Django 4.1.1 on 2022-09-30 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0022_alter_receita_categoria"),
    ]

    operations = [
        migrations.DeleteModel(name="Categoria",),
    ]
