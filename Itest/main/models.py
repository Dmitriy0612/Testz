from django.db import models
from django.core.validators import MinValueValidator,MinValueValidator
class Articles(models.Model):
    id_class = models.IntegerField("id_класса",validators=[MinValueValidator(1)],unique=True)
    name_class = models.CharField("Класс",max_length=20)
    def __str__(self):
        return self.name_class
    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
class Articles2(models.Model):
    id_teacher = models.IntegerField("id_учителя",validators=[MinValueValidator(1)],unique=True)
    full_name = models.CharField("ФИО",max_length=20)
    Qualification=models.CharField("Квалификация",max_length=20)
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

class Articles3(models.Model):
    id_subject = models.IntegerField("id предмета",validators=[MinValueValidator(1)],unique=True)
    name_subject = models.CharField("Название предмета",max_length=20)

    def __str__(self):
        return self.name_subject

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

class Articles4(models.Model):
    id_class = models.ForeignKey(Articles,on_delete=models.CASCADE)
    id_teacher = models.ForeignKey(Articles2,on_delete=models.CASCADE)
    id_subject = models.ForeignKey(Articles3,on_delete=models.CASCADE)

    def __str__(self):
        return f'{[self.id_teacher,self.id_class,self.id_subject]!r}'

    class Meta:
        verbose_name = 'Учебная деятельность'
        verbose_name_plural = 'Учебная деятельность'
