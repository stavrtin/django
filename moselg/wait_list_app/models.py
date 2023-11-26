from django.db import models


# Create your models here.

class Hospis(models.Model):

    name = models.CharField(max_length=150)
    beds_gz = models.IntegerField()
    on_activ = models.CharField(max_length=150)
    def __str__(self):
        return f'{self.name}'

class Pacient(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    pat_name = models.CharField(max_length=255)

    birthday = models.DateField()
    gender = models.CharField(max_length=50,
                                        choices=[('м' , 'Мужчина'),
                                                ('ж', 'Женщина')])
    def __str__(self):
        return f' Pacient {self.first_name}'


class ReportBeds(models.Model):
    filial = models.ForeignKey(Hospis, on_delete=models.CASCADE)
    beds_remont = models.IntegerField()
    beds_dop = models.IntegerField()
    m_free = models.IntegerField()
    f_free = models.IntegerField()
    m_busy = models.IntegerField()
    f_busy = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=150)

    def __str__(self):
        return f'Койки {self.filial} свободных {self.m_free + self.f_free} '


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
    med_critary = models.IntegerField()
    reason_hospit = models.TextField()
    type_transport = models.CharField(max_length=50,
                                        choices=[('СМП', 'СМП'),
                                                ('Машина с  носилками', 'Машина с  носилками'),
                                                ('Cобственным транспортом', 'Cобственным транспортом'),
                                                ('ЦЭМП', 'ЦЭМП'),
                                                ('Умер', 'Умер'),
                                                ('Машина без носилок', 'Машина без носилок') ])

    prefer_filial = models.ForeignKey(Hospis, on_delete=models.CASCADE)

    who_agreed_zayav = models.CharField(max_length=15,
                                       choices=[('Зав_ОВПП', 'Зав_ОВПП'),
                                                ('Зав_филиалом', 'Зав_филиалом'),
                                                ('Зав_ОДРП', 'Зав_ОДРП'),
                                                ('Врач_КЦ', 'Врач_КЦ'),
                                                ('Врач_деж_админ', 'Врач_деж_админ'),
                                                ('Глав_врач', 'Глав_врач'),
                                                ('Зам_по_амб', 'Зам_по_амб'),
                                                ('Зам_по_стац', 'Зам_по_стац'),
                                                ('ГВС', 'ГВС')])

    pacient_data = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    def __str__(self):
        return f' Заявка {self.pacient_data}'

class Gospitalization(models.Model):
    zayavka = models.ForeignKey(ZayavkaNaGospit, on_delete=models.CASCADE)
    date_gospit = models.DateTimeField()
    mksb = models.CharField(max_length=20)

class UserPatient(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    on_activ = models.BooleanField()

    def __str__(self):
        return f'{self.username}'

# class Hospis(models.Model):
#     hospisname = models.CharField(max_length=150)
#     hosp_m_dostup_bed = models.IntegerField()
#     hosp_f_dostup_bed = models.IntegerField()
#     hosp_m_busy_bed = models.IntegerField()
#     hosp_f_busy_bed = models.IntegerField()
#     hosp_m_free_bed = models.IntegerField()
#     hosp_f_free_bed = models.IntegerField()
#     hosp_m_wait_bed = models.IntegerField()
#     hosp_f_wait_bed = models.IntegerField()
#
#     def __str__(self):
#         return f'{self.hospisname}, свободныхM {self.hosp_m_free_bed}'