from django.db import models


# Create your models here.


class Hospis(models.Model):
    name = models.CharField(max_length=150)
    beds_gz = models.IntegerField()
    on_activ = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'

class Status_now(models.Model):
    #     ---------- текущий статус -------
    name_status = models.CharField(max_length=50)

    def __str__(self):
        # return f'Текущий статус = {self.name_status}'
        return f'{self.name_status}'

class PokanzNaGospit(models.Model):
    #     ---------- показания на госпитализац -------
    name_pokazOnGospit = models.CharField(max_length=50)

    def __str__(self):
        return f'Показ на госп. = {self.name_pokazOnGospit}'

class Pacient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    pat_name = models.CharField(max_length=255)

    birthday = models.DateField()
    gender = models.CharField(max_length=50,
                              choices=[('м', 'Мужчина'),
                                       ('ж', 'Женщина')])
    diagnoz = models.CharField(max_length=255)
    escort_filial = models.ForeignKey(Hospis, on_delete=models.CASCADE )

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
    now_status = models.ForeignKey(Status_now, on_delete=models.CASCADE)
    pokaz_on_gospit = models.ForeignKey(PokanzNaGospit, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    location_from = models.CharField(max_length=150)
    med_critary = models.IntegerField()
    reason_hospit = models.TextField()
    iniciator_hospit = models.TextField()
    type_transport = models.CharField(max_length=50,
                                      choices=[('СМП', 'СМП'),
                                               ('Машина с  носилками', 'Машина с  носилками'),
                                               ('Cобственным транспортом', 'Cобственным транспортом'),
                                               ('ЦЭМП', 'ЦЭМП'),
                                               ('Машина без носилок', 'Машина без носилок')])

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

class Kis(models.Model):
    kod = models.CharField(max_length=50)
    fio = models.CharField(max_length=250)
    dr = models.DateField()
    snils = models.CharField(max_length=150)
    adress_town = models.CharField(max_length=150)
    adress_reg = models.CharField(max_length=500)
    citizen = models.CharField(max_length=150)
    soc = models.CharField(max_length=150)
    fil = models.CharField(max_length=150)
    date_gospit = models.DateField()
    date_out = models.DateField()
    hospis = models.CharField(max_length=500)
    res_gospit = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.fio}'



# class Kontacts(models.Model):
#     kod = models.CharField(max_length=250)
#     dr = models.DateField()
#     tel_1 = models.CharField(max_length=150, blank=True)
#     tel_2 = models.CharField(max_length=150, blank=True)
#     tel_3 = models.CharField(max_length=500, blank=True)
#     tel_4 = models.CharField(max_length=150, blank=True)
#     tel_5 = models.CharField(max_length=150, blank=True)
#
#
#     def __str__(self):
#         return f'{self.kod}'


class Contacts(models.Model):
    kod = models.CharField(max_length=50, blank=True)
    fio_cont = models.CharField(max_length=150, blank=True)
    all_tel = models.CharField(max_length=150, blank=True)
    def __str__(self):
        return f'{self.kod}'