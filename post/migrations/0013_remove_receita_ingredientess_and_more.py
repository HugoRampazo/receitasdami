# Generated by Django 4.1.1 on 2022-09-22 14:23

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0012_rename_ingredientes_receita_ingredientess_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="receita", name="ingredientess",),
        migrations.RemoveField(model_name="receita", name="modo_de_preparo",),
        migrations.AddField(
            model_name="receita",
            name="ingredientes_da_receita",
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="receita",
            name="passo_a_passo",
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1),
            preserve_default=False,
        ),
    ]
