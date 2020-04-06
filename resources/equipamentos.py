from flask_restful import Resource, reqparse
from models.equipamento import EquipamentoModel
import json

equipamentos = []


class Equipamentos(Resource):
    def get(self):
        return equipamentos


class Equipamento(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('ativo')
    argumentos.add_argument('tipo_equipamento')
    argumentos.add_argument('serial')

    @staticmethod
    def find_equipamento(eid):
        for equi in equipamentos:
            if equi['eid'] == eid:
                return equi
        return {"message": "Equipamento ainda não cadastrado"}

    @staticmethod
    def get(eid):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('eid')
        dados = argumentos.parse_args()
        Equipamento.find_equipamento(dados[eid])

    def post(self, eid):
        dados = self.argumentos.parse_args()
        equi_objeto = EquipamentoModel(eid, **dados)
        equi_novo = equi_objeto.json()
        equipamentos.append(equi_novo)
        try:
            from csv import writer
            with open('computadores.csv', 'a', encoding='UTF-8') as arquivo:
                escritor_csv = writer(arquivo)
                escritor_csv.writerow([equi_novo['eid'], equi_novo['ativo'],
                                       equi_novo['serial'], equi_novo["tipo_equipamento"]])

        except FileExistsError:
            print('Error')

        return equi_novo

    def put(self, eid):
        pass

    def delete(self, eid):
        global equipamentos
        equipamentos = [equi for equi in equipamentos if equi != eid]
        return equipamentos


class Consultas(Resource):
    def get(self, ativo):
        if len(equipamentos) == 0:
            return {"Status": "Nenhum Equipamento Cadastrado"}
        for i in equipamentos:
            if i['ativo'] == ativo:
                return json.load(i)
