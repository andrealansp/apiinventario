from flask import Flask, render_template
from flask_restful import Api

from resources.equipamentos import Equipamentos, Equipamento, Consultas

app = Flask(__name__, template_folder="views")
api = Api(app)


@app.route('/')
def index():
    return render_template("index.html")


api.add_resource(Equipamentos, '/equipamentos')
api.add_resource(Equipamento, '/equipamento/<string:eid>')
api.add_resource(Consultas, '/equipamento/consulta/<string:ativo>')

if __name__ == '__main__':
    app.run(debug=True)
