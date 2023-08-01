from app.documentos.models import Documento
from app.documentos.items.models import Item
from app.tipos_documento.models import TipoDocumento
from app.movimientos.models import Movimiento
from app.common.error_handling import ObjectNotFound
class Salida(Documento):

    @classmethod
    def get_salidas(self, empresa_id: int):
        salidas = self.query.join(TipoDocumento).filter(TipoDocumento.submodulo_id=="SALIDAS", empresa_id==empresa_id).all()
        return salidas

    @classmethod
    def get_items(self, salida_id: int):
        items = Item.query.filter(Item.documento_id==salida_id).all()
        return items

    @classmethod
    def get_salida(self, salida_id: int, empresa_id: int):
        salidas = self.query.join(TipoDocumento).filter(TipoDocumento.submodulo_id=="SALIDAS", self.id==salida_id, self.empresa_id == empresa_id).first()
        if salidas is None:
            raise ObjectNotFound('La salida de bodega no existe')
        return salidas

    @classmethod
    def create_salida(self, modelo: dict, usuario_id: int, empresa_id: int):
        tipodoc = TipoDocumento.get_tipo_doc(int(modelo["tipodoc_id"]), empresa_id)
        consecutivo = (tipodoc.consecutivo +1)
        salida = Salida(consecutivo=consecutivo,
                           tipodoc_id=int(modelo["tipodoc_id"]),
                           bodega_id=int(modelo["bodega_id"]),
                           concepto=modelo.get('concepto', None),
                           usuario_id=usuario_id,
                           vehiculo_id=None,
                           empresa_id=empresa_id)

        tipodoc.consecutivo = consecutivo
        salida.save()
        tipodoc.update()

        for item in modelo['productos']:
            product = Item(cantidad=int(item['cantidad']),
                           producto_id=int(item['producto_id']),
                           documento_id=salida.id)
            product.save()

            movimiento = Movimiento(
                empresa_id=empresa_id,
                producto_id=product.producto_id,
                documento_id=product.documento_id,
                item_id=product.id,
                cantidad=product.cantidad,
                usuario_id=usuario_id,
                bodega_id=salida.bodega_id,
                tipo="S"
            )

            movimiento.save()

        return salida