# Generated by Django 3.1 on 2020-09-07 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictive', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='endpoint',
            options={'verbose_name': 'Конечная точка', 'verbose_name_plural': 'Конечные точки'},
        ),
        migrations.AlterModelOptions(
            name='mlalgorithm',
            options={'verbose_name': 'Алгоритм ML', 'verbose_name_plural': 'Алгоритмы ML'},
        ),
        migrations.AlterModelOptions(
            name='mlalgorithmstatus',
            options={'verbose_name': 'Статус AML', 'verbose_name_plural': 'Статусы AML'},
        ),
        migrations.AlterModelOptions(
            name='mlrequest',
            options={'verbose_name': 'Запрос к ML', 'verbose_name_plural': 'Запросы к ML'},
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='owner',
            field=models.CharField(max_length=128, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='mlalgorithm',
            name='code',
            field=models.CharField(max_length=10000, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='mlalgorithm',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='mlalgorithm',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='mlalgorithm',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='mlalgorithm',
            name='owner',
            field=models.CharField(max_length=128, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='mlalgorithm',
            name='version',
            field=models.CharField(max_length=128, verbose_name='Версия'),
        ),
        migrations.AlterField(
            model_name='mlalgorithmstatus',
            name='active',
            field=models.BooleanField(verbose_name='Активность'),
        ),
        migrations.AlterField(
            model_name='mlalgorithmstatus',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='mlalgorithmstatus',
            name='created_by',
            field=models.CharField(max_length=128, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='mlalgorithmstatus',
            name='status',
            field=models.CharField(max_length=128, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='mlrequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='mlrequest',
            name='feedback',
            field=models.CharField(blank=True, max_length=10000, null=True, verbose_name='Обратная связь'),
        ),
        migrations.AlterField(
            model_name='mlrequest',
            name='full_response',
            field=models.CharField(max_length=10000, verbose_name='Полный ответ'),
        ),
        migrations.AlterField(
            model_name='mlrequest',
            name='input_data',
            field=models.CharField(max_length=10000, verbose_name='Входные данные'),
        ),
        migrations.AlterField(
            model_name='mlrequest',
            name='response',
            field=models.CharField(max_length=10000, verbose_name='Ответ'),
        ),
    ]
