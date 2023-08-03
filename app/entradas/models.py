from app.documentos.models import Documento
from sqlalchemy import desc
from app.documentos.items.models import Item
from app.tipos_documento.models import TipoDocumento
from app.movimientos.models import Movimiento
from app.common.error_handling import ObjectNotFound
class Entrada(Documento):

    @classmethod
    def get_entradas(self, empresa_id: int):
        entradas = self.query.join(TipoDocumento).filter(TipoDocumento.submodulo_id=="ENTRADAS", empresa_id==empresa_id).order_by(desc(self.creado)).all()
        return entradas

    @classmethod
    def get_items(self, entrada_id: int):
        items = Item.query.filter(Item.documento_id==entrada_id).all()
        return items

    @classmethod
    def get_entrada(self, entrada_id: int, empresa_id: int):
        entrada = self.query.join(TipoDocumento).filter(TipoDocumento.submodulo_id=="ENTRADAS", self.id==entrada_id, self.empresa_id == empresa_id).first()
        if entrada is None:
            raise ObjectNotFound('La entrada a bodega no existe')
        return entrada

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

            movimiento = Movimiento(
                empresa_id=empresa_id,
                producto_id=product.producto_id,
                documento_id=product.documento_id,
                item_id=product.id,
                cantidad=product.cantidad,
                usuario_id=usuario_id,
                bodega_id=entrada.bodega_id,
                tipo="E"
            )

            movimiento.save()

        return entrada