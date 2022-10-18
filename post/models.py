from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
import os
from django.conf import settings
from PIL import Image


class Receita(models.Model):
    titulo = models.CharField(max_length=50, verbose_name="Título")
    categoria = models.CharField(max_length=100)
    imagem = models.ImageField(
        upload_to='imagem', blank=True, null=True)
    publicada = models.BooleanField(default=True)
    tempo_preparo = models.CharField(max_length=50, verbose_name="Tempo de preparo", help_text="Ex: 30 minutos.")
    rende_ate = models.CharField(max_length=50, verbose_name="Rende até", help_text="Ex: 03 porções.")
    ingredientes = RichTextField()
    modo_de_preparo = RichTextUploadingField()

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def __str__(self):
        return self.titulo