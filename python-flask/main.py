from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)
from Controladores.ControladorCandidato import ControladorCandidato
miControladorCandidato=ControladorCandidato()


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)
@app.route("/candidatos",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)
@app.route("/candidatos/<string:cedula>",methods=['GET'])
def getCandidato(cedula):
    json=miControladorCandidato.show(cedula)
    return jsonify(json)
@app.route("/candidatos/<string:cedula>",methods=['PUT'])
def modificarCandidato(cedula):
    data = request.get_json()
    json=miControladorCandidato.update(cedula,data)
    return jsonify(json)
@app.route("/estudiantes/<string:cedula>",methods=['DELETE'])
def eliminarCandidato(cedula):
    json=miControladorCandidato.delete(cedula)
    return jsonify(json)


from Controladores.ControladorMesa import ControladorMesa
miControladorMesa=ControladorMesa()

@app.route("/mesas",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)
@app.route("/mesas",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesas/<string:numero>",methods=['GET'])
def getMesa(numero):
    json=miControladorMesa.show(numero)
    return jsonify(json)
@app.route("/mesas/<string:numero>",methods=['PUT'])
def modificarMesa(numero):
    data = request.get_json()
    json=miControladorMesa.update(numero,data)
    return jsonify(json)
@app.route("/mesas/<string:numero>",methods=['DELETE'])
def eliminarMesa(numero):
    json=miControladorMesa.delete(numero)
    return jsonify(json)



from Controladores.ControladorPartido import ControladorPartido
miControladorPartido=ControladorPartido()

@app.route("/partidos",methods=['GET'])
def getPartidos():
    json=miControladorPartido.index()
    return jsonify(json)
@app.route("/partidos",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)


from Controladores.ControladorResultado import ControladorResultado
miControladorResultado=ControladorResultado()

@app.route("/resultados",methods=['GET'])
def getResultados():
    json=miControladorResultado.index()
    return jsonify(json)
@app.route("/resultados/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['POST'])
def crearResultado(id_candidato,id_mesa):
    data = request.get_json()
    json=miControladorResultado.create(data,id_candidato,id_mesa)
    return jsonify(json)
@app.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
    json=miControladorResultado.show(id)
    return jsonify(json)
@app.route("/resultados/<string:id_resultado>/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['PUT'])
def modificarResultado(id_resultado,id_candidato,id_mesa):
    data = request.get_json()
    json=miControladorResultado.update(id_resultado,data,id_candidato,id_mesa)
    return jsonify(json)
@app.route("/resultados/<string:id_resultado>",methods=['DELETE'])
def eliminarResultado(id_resultado):
    json=miControladorResultado.delete(id_resultado)
    return jsonify(json)

@app.route("/resultados/candidato/<string:id_candidato>",methods=['GET'])
def resultadosDeCandidato(id_candidato):
    json=miControladorResultado.listarResultadosDeCandidato(id_candidato)
    return jsonify(json)

@app.route("/resultados/totalmesas",methods=['GET'])
def resultadosTotalesDeMesas():
    json=miControladorResultado.totalVotosPorMesa()
    resultado = []
    for mesa in json:
        mesa_id = mesa['_id'][24:48]
        info_mesa = miControladorMesa.show(mesa_id)
        info_mesa['total_votos'] = mesa['total_votos']
        resultado.append(info_mesa)
    resultado_ordenado = sorted(resultado,key=lambda x: x['total_votos'], reverse=True)
    return jsonify(resultado_ordenado)

@app.route("/resultados/totalcandidatos",methods=['GET'])
def resultadosTotalesDeCandidatos():
    lista_candidatos = miControladorCandidato.index()
    for index, candidato in enumerate(lista_candidatos):
        lista_candidatos[index]['total_votos'] = 0
    votacion_candidatos=miControladorResultado.totalVotosPorCandidato()
    for candidato in votacion_candidatos:
        candidato_id = candidato['_id'][29:53]
        for index, cand in enumerate(lista_candidatos):
            if candidato_id == cand['_id']:
                lista_candidatos[index]['total_votos'] = candidato['total_votos']
    resultado_ordenado = sorted(lista_candidatos,key=lambda x: x['total_votos'], reverse=True)
    return jsonify(resultado_ordenado)

@app.route("/resultados/totalpartidos",methods=['GET'])
def resultadosTotalesDePartidos():
    lista_partidos = miControladorPartido.index()
    for index, partido in enumerate(lista_partidos):
        lista_partidos[index]['total_votos'] = 0
    votacion_candidatos=miControladorResultado.totalVotosPorCandidato()
    for candidato in votacion_candidatos:
        candidato_id = candidato['_id'][29:53]
        info_candidato = miControladorCandidato.show(candidato_id)
        for index, partido in enumerate(lista_partidos):
            if partido['_id'] == info_candidato['partido']['_id']:
                lista_partidos[index]['total_votos'] += candidato['total_votos']
                break
    resultado_ordenado = sorted(lista_partidos,key=lambda x: x['total_votos'], reverse=True)
    return jsonify(resultado_ordenado)

@app.route("/candidatos/<string:id>/partido/<string:id_partido>",methods=['PUT'])
def asignarPartidoACandidato(id,id_partido):
    json=miControladorCandidato.asignarPartido(id,id_partido)
    return jsonify(json)



def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
