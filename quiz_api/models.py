from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import ValidationError


class Topic(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название темы')
    content = models.TextField(verbose_name='Теория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Question(models.Model):
    content = models.TextField(verbose_name='Описание вопроса')
    test = models.ForeignKey('Test', on_delete=models.SET_NULL, null=True, related_name='questions', verbose_name='Тест')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Option(models.Model):
    content = models.TextField(verbose_name='Описание варианта ответа')
    is_right_option = models.BooleanField(default=False, verbose_name='Правильный ответ')
    question = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True, related_name='options', verbose_name='Вопрос')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Варинант ответа'
        verbose_name_plural = 'Варианты ответов'


class Test(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название теста')
    users = models.ManyToManyField(get_user_model(), through='TestsUsers')
    topic = models.OneToOneField('Topic', on_delete=models.CASCADE, verbose_name='Тема')

    def __str__(self):
        return self.name if self.name else 'Тест...'

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class TestsUsers(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tests_users', verbose_name='Пользователь')
    test = models.ForeignKey('Test', on_delete=models.CASCADE, related_name='tests_users', verbose_name='Тест')
    result = models.FloatField(verbose_name='Результат')

    def __str__(self):
        return f'{self.user} - {self.test}'

    class Meta:
        verbose_name = 'Пользователь и результат тестов'
        verbose_name_plural = 'Пользователи и результаты тестов'
