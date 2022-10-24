from Modelos.Mesa import Mesa


class ControladorMesa():
    def __init__(self):
        print("Creando ControladorMesa")

    def index(self):
        # el metodo 'index' muestra una lista con todas las mesas registradas; cada una con su informacion
        # relacionada(numero de mesa, cedulas inscritas, los votos totales de la mesa, votos por partido y
        # votos por candidato)
        print("Listar todas las mesas")
        unaMesa = {
            "cedulas inscritas": "150",
            "numero": "2",
            "votos": {
                "partidos": {
                    "liberal": {
                        "candidatos": {
                            "Carlos Uribe": 12,
                            "Cristina Sierra": 8,
                            "Jairo Bernal": 9,
                            "Sofia Alvarez": 11
                        },
                        "total votos": 40
                    },
                    "verde": {
                        "candidatos": {
                            "Esteban Martinez": 10,
                            "Juan Camilo Gonzales": 20,
                            "Juan Mendoza": 15,
                            "Laura Velez": 5,
                            "Maria Castillo": 10
                        },
                        "total votos": 60
                    }
                },
                "total": 100
            }
        }
        return [unaMesa]

    def create(self, infoMesa):
        # El metodo 'create' es utilizado para registrar una nueva mesa
        print("Crear una mesa")
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__

    def show(self, numero):
        # El metodo 'show' es utilizado para mostrar la informacion relacionada con una mesa en especifico
        # (numero de mesa, cedulas inscritas, los votos totales de la mesa, votos por partido y
        #  votos por candidato)
        print("Mostrando una mesa con numero ", numero)
        laMesa = {
            "cedulas inscritas": "150",
            "numero": "2",
            "votos": {
                "partidos": {
                    "liberal": {
                        "candidatos": {
                            "Carlos Uribe": 12,
                            "Cristina Sierra": 8,
                            "Jairo Bernal": 9,
                            "Sofia Alvarez": 11
                        },
                        "total votos": 40
                    },
                    "verde": {
                        "candidatos": {
                            "Esteban Martinez": 10,
                            "Juan Camilo Gonzales": 20,
                            "Juan Mendoza": 15,
                            "Laura Velez": 5,
                            "Maria Castillo": 10
                        },
                        "total votos": 60
                    }
                },
                "total": 100
            }
        }
        return laMesa

    def update(self, numero, infoMesa):
        # El metodo 'update' se utiliza para actualizar la informacion de una mesa
        print("Actualizando mesa con numero ", numero)
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__

    def delete(self, numero):
        # El metodo 'delete' se utiliza para eliminar una determinada mesa del sistema.
        print("Elimiando partido con numero ", numero)
        return {"deleted_count": 1}
