from flask import Flask
from flask_restful import Api
from resources.equipamentos import Equipamentos, Equipamento, Consultas

app = Flask(__name__)
api = Api(app)

api.add_resource(Equipamentos, '/equipamentos')
api.add_resource(Equipamento, '/equipamento/<string:eid>')
api.add_resource(Consultas, '/equipamento/consulta/<string:ativo>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
