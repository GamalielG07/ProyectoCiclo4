from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorResultado import ControladorResultado

app = Flask(__name__)
cors = CORS(app)

# CONTROLADORES: Se importan los controladores de cada modelo y se asignan cada uno a una variable
# para ser utilizados en las siguientes lineas
controladorPartido = ControladorPartido()
controladorCandidato = ControladorCandidato()
controladorMesa = ControladorMesa()
controladorResultado = ControladorResultado()


# metodo general para corroborar que el servidor esta en linea y no se presenta ningun error
@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


# SOLICITUDES DE PARTIDOS
# Lista de todos los partidos registrados
@app.route("/partidos", methods=['GET'])
def getPartidos():
    json = controladorPartido.index()
    return jsonify(json)


# Crear partido
@app.route("/partidos", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = controladorPartido.create(data)
    return jsonify(json)


# Informacion de un partido en especifico
@app.route("/partidos/<string:id>", methods=['GET'])
def getPartido(id):
    json = controladorPartido.show(id)
    return jsonify(json)


# Actualizar informacion de un partido en especifico
@app.route("/partidos/<string:id>", methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = controladorPartido.update(id, data)
    return jsonify(json)


# Eliminar un partido del sistema
@app.route("/partidos/<string:id>", methods=['DELETE'])
def eliminarPartido(id):
    json = controladorPartido.delete(id)
    return jsonify(json)


# SOLICITUDES DE CANDIDATO
# Lista de todos los candidatos registrados
@app.route("/candidatos", methods=['GET'])
def getCandidatos():
    json = controladorCandidato.index()
    return jsonify(json)


# Crear candidato
@app.route("/candidatos", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = controladorCandidato.create(data)
    return jsonify(json)


# Informacion de un candidato en especifico
@app.route("/candidatos/<string:cedula>", methods=['GET'])
def getCandidato(cedula):
    json = controladorCandidato.show(cedula)
    return jsonify(json)


# Actualizar infromacion de un candidato
@app.route("/candidatos/<string:cedula>", methods=['PUT'])
def modificarCandidato(cedula):
    data = request.get_json()
    json = controladorCandidato.update(cedula, data)
    return jsonify(json)


# Eliminar un candidato del sistema
@app.route("/candidatos/<string:cedula>", methods=['DELETE'])
def eliminarCandidato(cedula):
    json = controladorCandidato.delete(cedula)
    return jsonify(json)


# SOLICITUDES MESAS
# Lista de todas las mesas registradas
@app.route("/mesas", methods=['GET'])
def getMesas():
    json = controladorMesa.index()
    return jsonify(json)


# Crear mesa en el sistema
@app.route("/mesas", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = controladorMesa.create(data)
    return jsonify(json)


# informacion de una mesa en especifico
@app.route("/mesas/<string:numero>", methods=['GET'])
def getMesa(numero):
    json = controladorMesa.show(numero)
    return jsonify(json)


# Actualizar informacion de una mesa
@app.route("/mesas/<string:numero>", methods=['PUT'])
def modificarMesa(numero):
    data = request.get_json()
    json = controladorMesa.update(numero, data)
    return jsonify(json)


# Eliminar el registro de una mesa del sistema
@app.route("/mesas/<string:numero>", methods=['DELETE'])
def eliminarMesa(numero):
    json = controladorMesa.delete(numero)
    return jsonify(json)


# SOLICITUDES DE RESULTADOS
# Lista con de todas las mesas con los resultados en general
@app.route("/resultados", methods=['GET'])
def getResuladosGenerales():
    json = controladorResultado.index()
    return jsonify(json)


# Informacion de los resultados asociados a una mesa en especifico
@app.route("/resultados/<string:numero>", methods=['GET'])
def getResultado(numero):
    json = controladorResultado.show(numero)
    return jsonify(json)


# Lista de todas las mesas con los resultados de votaciones totales
@app.route("/resultadosmesas", methods=['GET'])
def getResuladosMesas():
    json = controladorResultado.votacionPorMesa()
    return jsonify(json)


# Lista de todos los partidos politicos con las votaciones totales de cada uno
@app.route("/resultadospartido", methods=['GET'])
def getResuladosPartido():
    json = controladorResultado.votacionesPorPartidoGeneral()
    return jsonify(json)


# Resultados de votaciones en una mesa en especifico, con los totales por partido
@app.route("/resultadospartido/<string:numero>", methods=['GET'])
def getResuladosPartidoMesa(numero):
    json = controladorResultado.votacionesPorPartidoMesa(numero)
    return jsonify(json)


# Lista con todos los candidatos, cada uno con su respectiva votacion
@app.route("/resultadoscandidato", methods=['GET'])
def getResuladosCandidato():
    json = controladorResultado.votacionesPorCandidatoGeneral()
    return jsonify(json)


# Resultados de votaciones en una mesa especifica, distribuida con la votacion de cada candidato
@app.route("/resultadoscandidato/<string:numero>", methods=['GET'])
def getResuladosCandidatoMesa(numero):
    json = controladorResultado.votacionesPorCandidatoMesa(numero)
    return jsonify(json)


# Ditribucion porcentual del senado por partido
@app.route("/resultadosdistribucion", methods=['GET'])
def getDistribucionPartidos():
    json = controladorResultado.distribucionPartidos()
    return jsonify(json)




def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
