from Modelos.Partido import Partido


class ControladorPartido():
    def __init__(self):
        print("Creando ControladorPartido")

    def index(self):
        # El metodo 'index' retorna una lista con todos los partidos registrados; cada uno con su respectiva
        # informacion(id,nombre y lema)
        print("Listar todos los partidos")
        unPartido = {
            "id": "abc123",
            "nombre": "Liberal",
            "lema": "Unidos por la paz"
        }
        return [unPartido]

    def create(self, infoPartido):
        # El metodo 'create' es utilizado para registrar un nuevo partido politico
        print("Crear un partido")
        elPartido = Partido(infoPartido)
        return elPartido.__dict__

    def show(self, id):
        # El metodo 'show' retorna la informacion de un partido en especifico(id,nombre y lema)
        print("Mostrando un partido con id ", id)
        elPartido = {
            "id": "abc123",
            "nombre": "Liberal",
            "lema": "Unidos por la paz"
        }
        return elPartido

    def update(self, id, infoPartido):
        # El metodo 'update' actualiza la informacion de un partido politico en especifico
        print("Actualizando partido con id ", id)
        elPartido = Partido(infoPartido)
        return elPartido.__dict__

    def delete(self, id):
        # El metodo 'delete' eliminia el registro de un partido politico en el sistema
        print("Elimiando partido con id ", id)
        return {"deleted_count": 1}
