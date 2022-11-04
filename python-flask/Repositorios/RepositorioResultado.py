from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado

from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):
    def getListadoResultadosDeCandidato(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)

    "Obtener votos totales por mesa"
    def votosTotalesPorMesa(self):
        query = {
            "$group": {
                "_id": "$mesa",
                "total_votos": {
                    "$sum": "$numero_votos"
                },
            }
        }
        pipeline = [query]
        return self.queryAggregation(pipeline)

    "Obtener votos totales por candidato"

    def votosTotalesPorCandidato(self):
        query = {
            "$group": {
                "_id": "$candidato",
                "total_votos": {
                    "$sum": "$numero_votos"
                },
            }
        }
        pipeline = [query]
        return self.queryAggregation(pipeline)

    "Obtener votos totales de candidatos por mesa"

    def votosTotalesPorCandidatoMesa(self,numero):
        theQuery = {"mesa.$id": ObjectId(numero)}
        return self.query(theQuery)