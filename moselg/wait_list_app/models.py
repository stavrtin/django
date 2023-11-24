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
    m_gz = models.IntegerField()
    f_gz = models.IntegerField()
    mf_gz = models.IntegerField()

    m_remont = models.IntegerField()
    f_remont = models.IntegerField()
    mf_remont = models.IntegerField()

    m_dop = models.IntegerField()
    f_dop = models.IntegerField()
    mf_dop = models.IntegerField()

    m_free = models.IntegerField()
    f_free = models.IntegerField()
    mf_free = models.IntegerField()

    create_at = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=150)

    def __str__(self):
        return f'Койки от : {self.med_org}'


class Filials(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f' Filial {self.name}'

class ZayavkaNaGospit(models.Model):
    now_status = models.CharField(max_length=50,
                                        choices=[('Ожидает одобрения', 'Ожидает одобрения'),
                                                ('Одобрена', 'Одобрена'),
                                                ('Отложена', 'Отложена'),
                                                ('Отменена', 'Отменена'),
                                                ('Умер', 'Умер'),
                                                ('Госпитализирован', 'Госпитализирован') ])
    pokaz_on_gospit = models.CharField(max_length=15,
                                       choices=[('Мед план', 'Мед план'),
                                                ('Мед срочно', 'Мед срочно'),
                                                ('ОРДП план', 'ОРДП план')])
    date_created = models.DateTimeField(auto_now_add=True)
    location_from = models.CharField(max_length=150)
    med_critary = models.IntegerField(max_length=5)
    reason_hospit = models.TextField()
    type_transport = models.CharField(max_length=50,
                                        choices=[('СМП', 'СМП'),
                                                ('Машина с  носилками', 'Машина с  носилками'),
                                                ('Cобственным транспортом', 'Cобственным транспортом'),
                                                ('ЦЭМП', 'ЦЭМП'),
                                                ('Умер', 'Умер'),
                                                ('Машина без носилок', 'Машина без носилок') ])

    prefer_filial = models.ForeignKey(Filials, on_delete=models.CASCADE)

    who_agreed_zayavka = models.CharField(max_length=15,
                                       choices=[('Зав_ОВПП', 'Зав_ОВПП'),
                                                ('Зав_филиалом', 'Зав_филиалом'),
                                                ('Зав_ОДРП', 'Зав_ОДРП'),
                                                ('Врач_КЦ', 'Врач_КЦ'),
                                                ('Врач_деж_админ', 'Врач_деж_админ'),
                                                ('Глав_врач', 'Глав_врач'),
                                                ('Зам_по_амб', 'Зам_по_амб'),
                                                ('Зам_по_стац', 'Зам_по_стац'),
                                                ('ГВС', 'ГВС')])


    def __str__(self):
        return f' Заявка {self.fio} {self.birthday}'





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

class Hospis(models.Model):
    hospisname = models.CharField(max_length=150)
    hosp_m_dostup_bed = models.IntegerField()
    hosp_f_dostup_bed = models.IntegerField()
    hosp_m_busy_bed = models.IntegerField()
    hosp_f_busy_bed = models.IntegerField()
    hosp_m_free_bed = models.IntegerField()
    hosp_f_free_bed = models.IntegerField()
    hosp_m_wait_bed = models.IntegerField()
    hosp_f_wait_bed = models.IntegerField()

    def __str__(self):
        return f'{self.hospisname}, свободныхM {self.hosp_m_free_bed}'