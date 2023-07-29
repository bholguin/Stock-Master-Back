from app.documentos.models import Documento
class Entrada(Documento):

    @classmethod
    def get_entradas(self, empresa_id: int):
        entradas = self.query.filter(self.empresa_id==empresa_id).all()
        return entradas