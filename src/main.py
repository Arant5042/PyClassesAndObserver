from observer_practice.canal import CanalNoticias
from observer_practice.suscriptores import SuscriptorEmail, SuscriptorSMS

canal = CanalNoticias("DonPepe")
suscriptor1 = SuscriptorEmail("Andres")
suscriptor2 = SuscriptorSMS("Sergio")

canal.suscribir(suscriptor1)
canal.suscribir(suscriptor2)

canal.publicar("Buenas, se vende aire a domicilio")

print(suscriptor1.mensajes)
print(suscriptor2.mensajes)