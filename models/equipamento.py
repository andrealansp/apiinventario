class EquipamentoModel:
    def __init__(self, eid, ativo, serial, modelo):
        self.eid = eid
        self.ativo = ativo
        self.serial = serial
        self.modelo = modelo

    def json(self):
        return {
            "eid": self.eid,
            "ativo": self.ativo,
            "serial": self.serial,
            "modelo": self.modelo
        }

