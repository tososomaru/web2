from django.db import models


class Maint(models.Model):
    """Ремонт"""
    datetime = models.DateTimeField(verbose_name='Дата')
    machine_id = models.PositiveSmallIntegerField(verbose_name='ID Станка')
    comp_id = models.CharField(verbose_name='ID Ремонта', max_length=20)

    def __str__(self):
        return "{} {}".format(self.machine_id, self.comp_id)

    class Meta():
        db_table = 'maint_machine'
        verbose_name = 'Ремонт'
        verbose_name_plural = 'Ремонты'

class Errors(models.Model):
    """Ошибки"""
    datetime = models.DateTimeField(verbose_name='Дата')
    machine_id = models.PositiveSmallIntegerField(verbose_name='ID Станка')
    error_id = models.CharField(verbose_name='ID Ошибки', max_length=20)

    def __str__(self):
        return "{} {}".format(self.machine_id, self.error_id)

    class Meta():
        db_table = 'errors_machine'
        verbose_name = 'Ошибка'
        verbose_name_plural = 'Ошибки'

class Failures(models.Model):
    """ Поломки """
    datetime = models.DateTimeField(verbose_name='Дата')
    machine_id = models.PositiveSmallIntegerField(verbose_name='ID Станка')
    failure_id = models.CharField(verbose_name='ID Поломки', max_length=20)

    def __str__(self):
        return "{} {}".format(self.machine_id, self.failure_id)

    class Meta():
        db_table = 'failures'
        verbose_name = 'Поломка'
        verbose_name_plural = 'Поломки'

class Machines(models.Model):
    """ Станки """
    machine_id = models.PositiveSmallIntegerField(verbose_name='ID Станка')
    model = models.CharField(verbose_name='ID Модели', max_length=20)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')

    def __str__(self):
        return "{} {}".format(self.machine_id, self.model)

    class Meta():
        db_table = 'machines'
        verbose_name = 'станок'
        verbose_name_plural = 'станки'



class Telemetry(models.Model):
    """Телеметрия"""
    datetime = models.DateTimeField(verbose_name='Дата')
    machine_id = models.PositiveSmallIntegerField(verbose_name='ID Станка')
    volt = models.FloatField(verbose_name='Напряжение')
    rotate = models.FloatField(verbose_name='Поворот')
    pressure = models.FloatField(verbose_name='Давление')
    vibration = models.FloatField(verbose_name='Вибрация')

    def __str__(self):
        return self.machine_id

    class Meta():
        db_table = 'telemetry'
        verbose_name = 'телеметрия'
        verbose_name_plural = 'телеметрия'
