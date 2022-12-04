# Generated by Django 4.1.3 on 2022-12-02 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название темы')),
                ('content', models.TextField(verbose_name='Теория')),
            ],
        ),
        migrations.CreateModel(
            name='TestsUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.FloatField(verbose_name='Результат')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_users', to='quiz_api.test', verbose_name='Тест')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests_users', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='test',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_api.topic', verbose_name='Тема'),
        ),
        migrations.AddField(
            model_name='test',
            name='users',
            field=models.ManyToManyField(through='quiz_api.TestsUsers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Описание вопроса')),
                ('test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to='quiz_api.test', verbose_name='Тест')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Описание варианта ответа')),
                ('is_right_option', models.BooleanField(default=False, verbose_name='Правильный ответ')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='options', to='quiz_api.question', verbose_name='Вопрос')),
            ],
        ),
    ]