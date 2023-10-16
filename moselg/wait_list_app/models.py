from django.db import models


# Create your models here.
class MedOrgMod(models.Model):
    TYPE_MED_ORG_CHOICES = ['Стационар', 'Амбулаторка', 'Социалка']

    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    on_activ = models.CharField(max_length=150)
    def __str__(self):
        return f'{self.name}'

class ReportBedsMod(models.Model):
    med_org = models.ForeignKey(MedOrgMod, on_delete=models.CASCADE)
    m_employ = models.IntegerField()
    f_employ = models.IntegerField()
    m_free = models.IntegerField()
    f_free = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=150)

    def __str__(self):
        return f'Койки от : {self.med_org}'

class ZayavkaNaGospit(models.Model):
    fio = models.CharField(unique=True, max_length=150)
    birthday = models.DateField(unique=True)

    diagnoz = models.CharField(max_length=150)
    dateVk = models.DateField()
    quickly_categor = models.CharField(max_length=15,
                                        choices=[('Мед_план','Мед_план'),
                                                 ('Соц_план', 'Соц_план'),
                                                 ('Мед_CITO', 'Мед_CITO'),
                                                 ('Соц_CITO', 'Соц_CITO') ])
    gender = models.CharField(max_length=1,
                            choices=[('M', 'Male'), ('F', 'Female')])
    med_org = models.ForeignKey(MedOrgMod, on_delete=models.CASCADE)
    comment = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' Пациент {self.fio} {self.birthday}'

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f' Client {self.name}'


class UserPatient(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    on_activ = models.BooleanField()

    def __str__(self):
        return f'{self.username}'