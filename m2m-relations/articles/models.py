from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Раздел')
    main = models.BooleanField(default=False, verbose_name='Основной')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')

    class Meta:
        verbose_name = 'Тема статьи'
        verbose_name_plural = 'Тема cтатьи'
        ordering = ['-main', 'tag__name']
