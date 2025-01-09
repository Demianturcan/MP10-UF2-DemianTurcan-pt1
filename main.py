from gestio_erp import Client
from gestio_erp import Comanda
from gestio_erp import Producte


print("\n           Crear comanda i afegir productes:"
      "\n")

comanda1 = Comanda(2)
prod1 = Producte(1,"taula")

comanda1.afegir_producte(prod1, 2) #afegim 2 unitats
comanda1.afegir_producte(prod1) #afegim unitats per defecte (1)

print(comanda1.resum_comanda())



print("\n           Crear client i mostrar comandes:"
      "\n")

client1 = Client(1, "Carla", "Carla@example.com")
print(client1)
client1.afegir_comanda(comanda1)
client1.consultar_comandes()