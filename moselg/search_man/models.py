from django.db import models


class Hospices(models.Model):
    name_hosp = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name_hosp}'


class VPS(models.Model):
    name_vps = models.CharField(max_length=260)

    def __str__(self):
        return f'{self.name_vps}'


class Pacient(models.Model):
    kod_p = models.CharField(primary_key = True, max_length=100)
    data_registracii = models.DateTimeField(blank=True)
    data_vkl_reestr = models.DateField(blank=True)
    data_na_uchet = models.DateField(blank=True)
    pacient = models.CharField(max_length=250)
    pol = models.CharField(max_length=10, blank=True)
    data_rozhd = models.DateField(blank=True)
    gr_status = models.CharField(max_length=100, blank=True)
    adres = models.CharField(max_length=500, blank=True)
    adres_fakt = models.CharField(max_length=500, blank=True)
    dul = models.CharField(max_length=150, blank=True)
    serija_nomer  = models.CharField(max_length=50, blank=True)
    kem_vydan = models.CharField(max_length=150, blank=True)
    svidetelstvo = models.CharField(max_length=150, blank=True)
    snils = models.CharField(max_length=50, blank=True)
    polis_oms = models.CharField(max_length=50, blank=True)
    invalidnost = models.CharField(max_length=50, blank=True)
    osnovnoj_mkb10 = models.CharField(max_length=150, blank=True)
    osn_kont_lico = models.CharField(max_length=150, blank=True)
    data_vk = models.DateField(blank=True)
    dokument_vk = models.CharField(max_length=150, blank=True)
    organizacija_vk = models.CharField(max_length=150, blank=True)
    razreshenie_dzm = models.CharField(max_length=50, blank=True)
    data_razreshenija_dzm = models.DateField(blank=True)
    nomer_razreshenija_dzm = models.CharField(max_length=50, blank=True)
    status_pacienta = models.CharField(max_length=150, blank=True)
    data_prekr_okaz_pmp = models.DateField(blank=True)
    osnovanija_prekr_pmp = models.CharField(max_length=150, blank=True)
    data_smerti = models.DateField(blank=True)
    kur_podr = models.ForeignKey(VPS, on_delete=models.DO_NOTHING)
    rc = models.CharField(max_length=10, blank=True)
    bk = models.CharField(max_length=10, blank=True)
    osn_diagnoz_obr = models.TextField(blank=True)
    komment = models.TextField(blank=True)
    svo = models.CharField(max_length=50, blank=True)
    kanal_post_inf = models.CharField(max_length=150, blank=True)
    kto_napravil = models.CharField(max_length=150, blank=True)
    data_poluch_ids = models.DateField(blank=True)
    amb_karta = models.CharField(max_length=150, blank=True)
    pom_udalenija = models.CharField(max_length=10, blank=True)
    gr = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f' Pacient {self.pacient}'



class Kis(models.Model):
    pacient = models.ForeignKey(Pacient, on_delete=models.DO_NOTHING)
    data_rozhd = models.DateField(blank=True)
    snils  = models.CharField(max_length=50, blank=False)
    adres_region  = models.CharField(max_length=500, blank=True)
    adres = models.CharField(max_length=500, blank=True)
    grazhdanstvo  = models.CharField(max_length=150, blank=True)
    soc_status = models.CharField(max_length=150, blank=True)
    data_gospit = models.DateTimeField()
    data_vipiski= models.DateTimeField(blank=True)
    otdelenie  = models.ForeignKey(Hospices, on_delete=models.DO_NOTHING)
    ishod  = models.CharField(max_length=150, blank=True)
    telefon = models.CharField(max_length=150, blank=True)
    kont_inf = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f'Kis {self.pacient}, {self.data_gospit} '


class Contacts(models.Model):
    kont_pac = models.ForeignKey(Pacient, on_delete=models.DO_NOTHING, related_name='cont')
    kont_tel = models.CharField(max_length=250)
    kont_fio = models.CharField(max_length=255)

    def __str__(self):
        return f'Cont {self.kont_pac} - {self.kont_fio}'
