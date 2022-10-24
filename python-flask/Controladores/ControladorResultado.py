from Modelos.Resultado import Resultado


class ControladorResultado():
    def __init__(self):
        print("Creando ControladorResultado")

    def index(self):
        # El metodo 'index' retorna una lista de todas las mesas registradas, con sus respectivos resultados
        # de votacion, cada una distribuida por partido politico y los candidatos que pertenecen a el.
        print("Listar todos los resultados generales de las mesas")
        listaResultados = [
            {
                "numero mesa": 1,
                "votos": {
                    "total mesa": 100,
                    "partidos": {
                        "verde": {
                            "total partido": 60,
                            "candidatos": {
                                "Juan Mendoza": 15,
                                "Juan Camilo Gonzales": 20,
                                "Maria Castillo": 10,
                                "Laura Velez": 5,
                                "Esteban Martinez": 10
                            }
                        },
                        "liberal": {
                            "total partido": 40,
                            "candidatos": {
                                "Cristina Sierra": 8,
                                "Carlos Uribe": 12,
                                "Sofia Alvarez": 11,
                                "Jairo Bernal": 9
                            }
                        }
                    }
                }
            },
            {
                "numero mesa": 2,
                "votos": {
                    "total mesa": 100,
                    "partidos": {
                        "verde": {
                            "total partido": 60,
                            "candidatos": {
                                "Juan Mendoza": 15,
                                "Juan Camilo Gonzales": 20,
                                "Maria Castillo": 10,
                                "Laura Velez": 5,
                                "Esteban Martinez": 10
                            }
                        },
                        "liberal": {
                            "total partido": 40,
                            "candidatos": {
                                "Cristina Sierra": 8,
                                "Carlos Uribe": 12,
                                "Sofia Alvarez": 11,
                                "Jairo Bernal": 9
                            }
                        }
                    }
                }
            },
        ]
        return listaResultados

    def show(self, numero):
        # El metodo 'show' retorna la informacion de una mesa con su resultado de votacion,
        # distribuido por partido politico y los candidatos que pertenecen a el
        print("Mostrando un resultado con numero de mesa ", numero)
        elResultado = {
            "numero mesa": 1,
            "votos": {
                "total mesa": 100,
                "partidos": {
                    "verde": {
                        "total partido": 60,
                        "candidatos": {
                            "Juan Mendoza": 15,
                            "Juan Camilo Gonzales": 20,
                            "Maria Castillo": 10,
                            "Laura Velez": 5,
                            "Esteban Martinez": 10
                        }
                    },
                    "liberal": {
                        "total partido": 40,
                        "candidatos": {
                            "Cristina Sierra": 8,
                            "Carlos Uribe": 12,
                            "Sofia Alvarez": 11,
                            "Jairo Bernal": 9
                        }
                    }
                }
            }
        }
        return elResultado

    def votacionPorMesa(self):
        # El metodo 'votacionPorMesa' retorna una lista con todas las mesas registradas,
        # cada una con el numero de mesa y total de votos
        print("Listado de resultados por mesa")
        resultadoOrdenado = [
            {
                "mesa": 3,
                "votos": 140
            },
            {
                "mesa": 1,
                "votos": 125
            },
            {
                "mesa": 2,
                "votos": 100
            }
        ]
        return resultadoOrdenado

    def votacionesPorPartidoGeneral(self):
        # El metodo 'votacionesPorPartidoGeneral' retorna una lista con todos los partidos inscritos,
        # cada uno con su nombre y total de votos en todas las mesas
        print("Listado de votos general de partidos politicos")
        resultadosPartido = [
            {
                "partido": "verde",
                "votos": 1620
            },
            {
                "partido": "liberal",
                "votos": 788
            },
            {
                "partido": "conservador",
                "votos": 197
            }
        ]
        return resultadosPartido

    def votacionesPorPartidoMesa(self, numeroMesa):
        # El metodo 'votacionesPorPartidoMesa' retorna una lista de todas las mesas registradas,
        # cada una con el numero de mesa, total de votos en la mesa, y total de votos distribuidos
        # entre cada partido
        print("Listado de votos de partidos politicos por mesa ", numeroMesa)
        resultadoPartidoMesa = {
            "mesa": 5,
            "total votos": 337,
            "votacion": [
                {
                    "partido": "verde",
                    "votos": 162
                },
                {
                    "partido": "liberal",
                    "votos": 78
                },
                {
                    "partido": "conservador",
                    "votos": 97
                }
            ]
        }
        return resultadoPartidoMesa

    def votacionesPorCandidatoGeneral(self):
        # El metodo 'votacionesPorCandidatoGeneral' retorna una lista con todos los candidatos registrados
        # cada uno con su nombre, partido y total de votos
        print("Listado de votos de candidatos general")
        resultadoCandidatosGeneral = [
            {
                "nombre": "Juan Mendoza",
                "partido": "verde",
                "votos": 250
            },
            {
                "nombre": "Juan Mendoza",
                "partido": "verde",
                "votos": 150
            },
            {
                "nombre": "Juan Mendoza",
                "partido": "verde",
                "votos": 50
            },
            {
                "nombre": "Juan Mendoza",
                "partido": "verde",
                "votos": 25
            },
        ]
        return resultadoCandidatosGeneral

    def votacionesPorCandidatoMesa(self, numeroMesa):
        # El metodo 'votacionesPorCandidatoMesa' retorna una lista de todas las mesas registradas con su
        # respectivo numero y votaciones por cada candidato.
        print("Listado de votos de cadidatos por mesa ", numeroMesa)
        resultadoCandidatoMesa = {
            "mesa": 5,
            "votacion": [
                {
                    "nombre": "Juan Mendoza",
                    "partido": "verde",
                    "votos": 250
                },
                {
                    "nombre": "Juan Mendoza",
                    "partido": "verde",
                    "votos": 150
                },
                {
                    "nombre": "Juan Mendoza",
                    "partido": "verde",
                    "votos": 50
                },
            ]
        }
        return resultadoCandidatoMesa

    def distribucionPartidos(self):
        # El metodo 'distribucionPartidos' retorna una lista con los partidos y su participacion porcentual
        # en el senado segun los resultados de la votaciones
        print("Distribucion porcentual de partidos politicos")
        distribucionPorcentual = [
            {
                "partido": "verde",
                "porcentaje": 50,
            },
            {
                "partido": "liberal",
                "porcentaje": 30,
            },
            {
                "partido": "conservador",
                "porcentaje": 20,
            },
        ]
        return distribucionPorcentual
