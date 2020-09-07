from django.db import models

class Endpoint(models.Model):

    """Информация о конечных точках алгоритмов"""
    name = models.CharField(max_length=128, verbose_name='Название')
    owner = models.CharField(max_length=128, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')

    def __str__(self):
        return "{} {}".format(self.name, self.owner)

    class Meta:
        verbose_name = 'Конечная точка'
        verbose_name_plural = 'Конечные точки'


class MLAlgorithm(models.Model):
    """Модель машинного обучения"""
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.CharField(max_length=1000, verbose_name='Описание')
    code = models.CharField(max_length=10000, verbose_name='Код')
    version = models.CharField(max_length=128, verbose_name='Версия')
    owner = models.CharField(max_length=128, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE, verbose_name='Конечная точка')

    def __str__(self):
        return "{} {} Версия: {}".format(self.name, self.owner, self.version)

    class Meta:
        verbose_name = 'Алгоритм ML'
        verbose_name_plural = 'Алгоритмы ML'

class MLAlgorithmStatus(models.Model):
    """Статус модели машинного обучения"""
    status = models.CharField(max_length=128, verbose_name='Статус')
    active = models.BooleanField(verbose_name='Активность')
    created_by = models.CharField(max_length=128, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name="status", verbose_name='Алгоритм')

    def __str__(self):
        return "Статус {} {} Версия: {}".format(self.status, self.active, self.created_by)

    class Meta:
        verbose_name = 'Статус AML'
        verbose_name_plural = 'Статусы AML'

class MLRequest(models.Model):
    """Модель хранит все запросы к моделям ML"""
    input_data = models.CharField(max_length=10000, verbose_name='Входные данные')
    full_response = models.CharField(max_length=10000, verbose_name='Полный ответ')
    response = models.CharField(max_length=10000, verbose_name='Ответ')
    feedback = models.CharField(max_length=10000, blank=True, null=True, verbose_name='Обратная связь')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, verbose_name='Алгоритм')

    def __str__(self):
        return self.created_at

    class Meta:
        verbose_name = 'Запрос к ML'
        verbose_name_plural = 'Запросы к ML'

