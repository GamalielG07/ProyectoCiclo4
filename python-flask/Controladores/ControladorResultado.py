from Repositorios.RepositorioResultado import RepositorioResultado
from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        return self.repositorioResultado.findAll()

    """
    Asignacion candidato y mesa a inscripción
    """

    def create(self,infoResultado,id_candidato,id_mesa):
        nuevoResultado = Resultado(infoResultado)
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        nuevoResultado.candidato = elCandidato
        nuevoResultado.mesa = laMesa
        return self.repositorioResultado.save(nuevoResultado)

    def show(self,id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    """
    Modificación de resultado (candidato y mesa)
    """

    def update(self, id, infoResultado,id_candidato,id_mesa):
        resultadoActual = Resultado(self.repositorioResultado.findById(id))
        resultadoActual.numero_votos = infoResultado["numero_votos"]
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        resultadoActual.candidato = elCandidato
        resultadoActual.mesa = laMesa
        return self.repositorioResultado.save(resultadoActual)

    def delete(self, id):
        return self.repositorioResultado.delete(id)

    "Obtener todos los resultados de un candidato"
    def listarResultadosDeCandidato(self, id_candidato):
        return self.repositorioResultado.getListadoResultadosDeCandidato(id_candidato)

    "Obtener votos totales por mesa"
    def totalVotosPorMesa(self):
        return self.repositorioResultado.votosTotalesPorMesa()

    "Obtener votos totales por candidato"
    def totalVotosPorCandidato(self):
        return self.repositorioResultado.votosTotalesPorCandidato()

    "Obtener votos totales de candidatos por mesa"
    def totalVotosPorCandidatoMesa(self,numero):
        return self.repositorioResultado.votosTotalesPorCandidatoMesa(numero)