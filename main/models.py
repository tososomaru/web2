from django.db import models
from datetime import datetime
from django.utils import timezone


class TypeRequest(models.Model):
    """Тип заявки"""
    requestType = models.CharField('Тип заявки', max_length=30)

    def __str__(self):
        return self.requestType

    class Meta:
        db_table = 'type_request'
        verbose_name = 'Тип заявки'
        verbose_name_plural = 'Типы заявок'


class Specialty(models.Model):
    """Специальность"""
    specialty = models.CharField('Специальность', max_length=50)

    class Meta:
        db_table = 'specialty'
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

    def __str__(self):
        return self.specialty



class Position(models.Model):
    """Должность"""
    position = models.CharField('Должность', max_length=50)

    def __str__(self):
        return self.position

    class Meta:
        db_table = 'position'
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Manufacture(models.Model):
    """Цех"""
    manufacture = models.CharField('Цех', max_length=30)

    def __str__(self):
        return self.manufacture

    class Meta:
        db_table = "manufacture"
        verbose_name = 'Цех'
        verbose_name_plural = 'Цеха'


class FeatureMachine(models.Model):
    """Характеристики станка"""
    featureName = models.CharField('Название характеристики', max_length=100)
    featureDescription = models.TextField('Описание характеристики', blank=True)
    machine = models.ManyToManyField('Machine')
    featureValue = models.PositiveSmallIntegerField('Значание характеристики')
    def __str__(self):
        return self.featureName

    class Meta:
        db_table = 'feature_machine'
        verbose_name = 'Характеристика станка'
        verbose_name_plural = 'Характеристики станков'

class Machine(models.Model):
    """Станок"""
    model = models.SlugField('Станок', max_length=50)

    def __str__(self):
        return self.model

    class Meta:
        db_table = 'machine'
        verbose_name = 'Станок'
        verbose_name_plural = 'Станки'




class RequestStatus(models.Model):
    """Статус заявки"""
    status = models.CharField('Статус заявки', max_length=50)
    parentRequest = models.ForeignKey('Request', verbose_name='Заявка',
                               on_delete=models.DO_NOTHING)
    owner = models.CharField(max_length=128, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    class Meta:
        db_table = 'request_status'
        verbose_name = 'Статус завки'
        verbose_name_plural = 'Статусы заявки'


class MachineCondition(models.Model):
    """Состояние станка"""
    machineCondition = models.CharField('Cостояние станка', max_length=50)
    parentMachine = models.ForeignKey(Machine, verbose_name='Станок', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.machineCondition

    class Meta:
        db_table = 'machine_condition'
        verbose_name = 'Состояние станка'
        verbose_name_plural = 'Состояния станков'


class Employee(models.Model):
    """Сотрудник"""
    lastName = models.CharField('Фамилия', max_length=50)
    firstName = models.CharField('Имя', max_length=50)
    middleName = models.CharField('Отчество', max_length=50)
    position = models.ForeignKey(Position, verbose_name="Должность",
                                 on_delete=models.SET_NULL, null=True)
    specialty = models.ForeignKey(Specialty, verbose_name="Специальность",
                                  on_delete=models.SET_NULL, null=True)
    numberPhone = models.PositiveSmallIntegerField('Номер телефона')
    email = models.EmailField('Почта')


    def __str__(self):
        return "{} {}".format(self.lastName, self.firstName)

    class Meta:
        db_table = 'employee'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Request(models.Model):
    """Заявка"""

    sender = models.ForeignKey(Employee, verbose_name='Отправитель',
                               on_delete=models.DO_NOTHING)
    typeRequest = models.ForeignKey(TypeRequest, verbose_name='Тип заявки',
                                    on_delete=models.DO_NOTHING),
    machine = models.ForeignKey(Machine, verbose_name='Станок',
                                       on_delete=models.DO_NOTHING)
    malfunction = models.CharField(verbose_name='Неисправность', max_length=100)

    date = models.DateTimeField('Дата заявки', auto_now_add=True)
    def __str__(self):
        return "{} {}".format(self.sender, self.date)

    class Meta:
        db_table = 'request'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class MachineStatus(models.Model):
    """Статус работы станка"""
    machine = models.ForeignKey(Machine, verbose_name='Станок',
                                on_delete=models.CASCADE)
    machineCondition = models.ForeignKey(MachineCondition, verbose_name='Состояние станка',
                                         on_delete=models.CASCADE)
    workplace = models.ForeignKey('Workplace', verbose_name='Рабочее место',
                                 on_delete=models.CASCADE)
    repair = models.ForeignKey('Repair', verbose_name='Ремонт',
                               on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{} {}".format(self.machine, self.machineCondition)

    class Meta:
        db_table = 'machine_status'
        verbose_name = 'Статус работы станка'
        verbose_name_plural = 'Статусы работы станка'


class Workplace(models.Model):
    """Рабочее место"""
    worker = models.ForeignKey(Employee, verbose_name='Рабочий',
                               on_delete=models.CASCADE)
    manufacture = models.ForeignKey(Manufacture, verbose_name='Цех',
                                    on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, verbose_name='Станок',
                                on_delete=models.CASCADE)


    def __str__(self):
        return "Оператор: {} Станок: {}".format(self.worker, self.machine)

    class Meta:
        db_table = 'workplace'
        verbose_name = 'Рабочее место'
        verbose_name_plural = 'Рабочие места'


class Repair(models.Model):
    """Ремонт"""

    dateStartRepair = models.DateTimeField('Дата начала ремонта',auto_now_add=True, blank=True)
    repairWorker = models.ForeignKey(Employee, verbose_name='Рабочий',
                                     on_delete=models.CASCADE)

    requestRepair = models.ForeignKey(Request, verbose_name='Заявка', on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.repairWorker.firstName, self.repairWorker.lastName)

    class Meta:
        db_table = 'repair'
        verbose_name = 'Ремонт'
        verbose_name_plural = 'Ремонты'
