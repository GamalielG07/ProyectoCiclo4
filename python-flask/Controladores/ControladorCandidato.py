from Modelos.Candidato import Candidato


class ControladorCandidato():
    def __init__(self):
        print("Creando ControladorCandidato")

    def index(self):
        # El metodo 'index' retorna una lista con todos los candidatos registrados en el sistema; cada uno
        # con su cedula, nombre, apellido y numero de resolucion que lo avala
        print("Listar todos los candidatos")
        unCandidato = [
            {
                "cedula": "1234567",
                "numero_resolucion": "1001",
                "nombre": "Juan",
                "apellido": "Meza"
            },
            {
                "cedula": "7654321",
                "numero_resolucion": "1002",
                "nombre": "Carlos",
                "apellido": "Castillo"
            },
        ]
        return unCandidato

    def create(self, infoCandidato):
        # El metodo 'create' es utilizado para registrar un nuevo candidato en el sistema
        print("Crear un candidato")
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def show(self, cedula):
        # El metodo 'show' retorna la informacion(cedula,nombre,apellido y numero de resolucion que lo avala)
        # de un candidato registrado
        elCandidato = {
            "cedula": "1234567",
            "numero_resolucion": "1001",
            "nombre": "Juan",
            "apellido": "Meza"
        }
        return elCandidato

    def update(self, cedula, infoCandidato):
        # El metodo 'update' actualiza la informacion de un candidato en especifico
        print("Actualizando candidato con cedula ", cedula)
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def delete(self, cedula):
        # El metodo 'delete' elimina el registro  de un candidato en el sistema
        print("Elimiando candidato con cedula ", cedula)
        return {"deleted_count": 1}
