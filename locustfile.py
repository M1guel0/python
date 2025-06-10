from locust import HttpUser, task, between

class traficodeusuarios( HttpUser):
    tiempo_espera = between(1, 5)

def trafico_variado(self):
    self.client.get("/")