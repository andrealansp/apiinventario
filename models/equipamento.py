class EquipamentoModel:
    def __init__(self, eid, ativo, serial, tipo_equipamento):
        self.eid = eid
        self.ativo = ativo
        self.serial = serial
        self.tipo_equipamentos = tipo_equipamento

    def json(self):
        return {
            "eid": self.eid,
            "ativo": self.ativo,
            "serial": self.serial,
            "tipo_equipamento": self.tipo_equipamentos
        }
