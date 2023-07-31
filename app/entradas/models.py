from app.documentos.models import Documento
from app.documentos.items.models import Item
from app.tipos_documento.models import TipoDocumento
class Entrada(Documento):

    @classmethod
    def get_entradas(self, empresa_id: int):
        entradas = self.query.filter(self.empresa_id==empresa_id).all()
        return entradas

    @classmethod
    def create_entrada(self, modelo: dict, usuario_id: int, empresa_id: int):
        tipodoc = TipoDocumento.get_tipo_doc(int(modelo["tipodoc_id"]), empresa_id)
        consecutivo = (tipodoc.consecutivo +1)
        entrada = Entrada(consecutivo=consecutivo,
                           tipodoc_id=int(modelo["tipodoc_id"]),
                           bodega_id=int(modelo["bodega_id"]),
                           concepto=modelo.get('concepto', None),
                           usuario_id=usuario_id,
                           vehiculo_id=None,
                           empresa_id=empresa_id)

        tipodoc.consecutivo = consecutivo
        entrada.save()
        tipodoc.update()

        for item in modelo['productos']:
            product = Item(cantidad=int(item['cantidad']),
                           producto_id=int(item['producto_id']),
                           documento_id=entrada.id)
            product.save()

        return entrada