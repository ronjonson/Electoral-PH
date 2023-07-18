from django.db import models

class Province(models.Model):
    province = models.CharField(max_length=50)    
    def __str__(self):
        return f"{self.province}"

class Candidate(models.Model):
    candidate = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return f"candidate {self.id} is {self.full_name}"

class Reps_2004(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    electors = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.id}: {self.province} with {self.electors} electors"
    
class Reps_2010(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    electors = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return f"{self.id}: {self.province} with {self.electors} electors"

class Reps_2016(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    electors = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.id}: {self.province} with {self.electors} electors"

class Reps_2022(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    electors = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.id}: {self.province} with {self.electors} electors"
    
class Pres_2004(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    Gloria_Arroyo = models.IntegerField()
    Fernando_Poe = models.IntegerField()
    Panfilo_Lacson = models.IntegerField()
    Raul_Roco = models.IntegerField()
    Eddie_Villanueva = models.IntegerField()

class Pres_2010(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    Benigno_Aquino = models.IntegerField()
    Joseph_Estrada = models.IntegerField()
    Manny_Villar = models.IntegerField()
    Gilbert_Teodoro = models.IntegerField()
    Eddie_Villanueva = models.IntegerField()
    Dick_Gordon = models.IntegerField()
    Nicanor_Perlas = models.IntegerField()
    Jamby_Madrigal = models.IntegerField()
    John_delosReyes = models.IntegerField()

class VicePres_2010(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    Jejomar_Binay = models.IntegerField()
    Mar_Roxas = models.IntegerField()
    Loren_Legarda = models.IntegerField()
    Bayani_Fernando = models.IntegerField()
    Edu_Manzano = models.IntegerField()
    Perfecto_Yasay = models.IntegerField()
    Jay_Sonza = models.IntegerField()
    Dominador_Chipeco = models.IntegerField()

class Pres_2016(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    Rodrigo_Duterte = models.IntegerField()
    Mar_Roxas = models.IntegerField()
    Grace_Poe = models.IntegerField()
    Jejomar_Binay = models.IntegerField()
    Miriam_Santiago = models.IntegerField()

class VicePres_2016(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    Leni_Robredo = models.IntegerField()
    Bongbong_Marcos = models.IntegerField()
    Alan_Cayetano = models.IntegerField()
    Chiz_Escudero = models.IntegerField()
    Sonny_Trillanes = models.IntegerField()
    Gringo_Honasan = models.IntegerField()

class Pres_2022(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    Bongbong_Marcos = models.IntegerField()
    Leni_Robredo = models.IntegerField()
    Manny_Pacquiao = models.IntegerField()
    Isko_Moreno = models.IntegerField()
    Panfilo_Lacson = models.IntegerField()
    Faisal_Mangondato = models.IntegerField()
    Ernesto_Abella = models.IntegerField()
    Leody_deGuzman = models.IntegerField()
    Norberto_Gonzales = models.IntegerField()
    Jose_Montemayor = models.IntegerField()

class VicePres_2022(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    Sara_Duterte = models.IntegerField()
    Kiko_Pangilinan = models.IntegerField()
    Tito_Sotto = models.IntegerField()
    Willie_Ong = models.IntegerField()
    Lito_Atienza = models.IntegerField()
    Manny_Lopez = models.IntegerField()
    Walden_Bello = models.IntegerField()
    Carlos_Serapio = models.IntegerField()
    Rizalito_David = models.IntegerField()