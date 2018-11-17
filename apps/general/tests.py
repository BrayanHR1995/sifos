from django.test import TestCase

from .models import Municipio
from .models import Especie
from .models import EspecieMunicipio
from .models import Robot
from .models import TipoPatron
import unittest
# Create your tests here.
class MunicipioTests(TestCase):

    def setUp(self):
        print("Prueba Unitaria Municipio")
        if (Municipio.objects.create(nombre='Villavicencio',longitd = "24.000", latitud="24.000")):
            print("Exitoso")
        else:
            print("No Exitoso")

    def test_text_content(self):
        municipio = Municipio.objects.get(id=1)

        
    def comp_text(self):
        a= 'Villavicencio'
        self.assertEqual(municipio.nombre,a)
 
        
        
class EspecieTests(TestCase):

    def setUp(self):
        print("Prueba Unitaria Especie")
        if (Especie.objects.create(nombre='Prueba',nombre_cientifico  = "prueba1", porcentaje_oxigeno="20%", porcentaje_carbono="15%")):
            print("Exitoso")
        else:
            print("No Exitoso")

    def test_text_content(self):
        especie = Especie.objects.get(id=1)

            
class RobotTests(TestCase):

    def setUp(self):
        print("Prueba Unitaria Robot")
        if (Robot.objects.create(nombre='Walle',gps  = "Prueba GPS", modelo="2016", estado="Bueno")):
            print("Exitoso")
        else:
            print("No Exitoso")

    def test_text_content(self):
        robot = Robot.objects.get(id=1)

          
class TipoPatronTests(TestCase):

    def setUp(self):
        print("Prueba Unitaria TipoPatron")
        if (TipoPatron.objects.create(nombre='t1',figura  = "Triangulo", distancia_interna =200)):
            print("Exitoso")
        else:
            print("No Exitoso")

    def test_text_content(self):
        tipoPatron = TipoPatron.objects.get(id=1)


