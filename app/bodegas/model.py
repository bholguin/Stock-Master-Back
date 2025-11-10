from app.common.db import db, BaseModel
from app.documentos.models import Documento
#from app.movimientos.models import Movimiento
from app.common.error_handling import ObjectNotFound,InvalidUsage


class Bodega(db.Model, BaseModel):
    __tablename__ = "bodegas"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(100))
    descripcion = db.Column(db.String(200))
    empresa_id = db.Column(db.Integer, db.ForeignKey("empresas.id"), nullable=False)

    documentos = db.relationship(Documento, backref='bodega_documentos', lazy=True)
    # movimientos = db.relationship('Movimiento', backref='bodega_movimientos', lazy=True)

    def __init__(self, nombre: str, direccion: str, descripcion: str, empresa_id: int):
        self.nombre = nombre
        self.direccion = direccion
        self.descripcion = descripcion
        self.empresa_id = empresa_id

    # =====================================================
    # 🔍 Obtener una bodega por ID
    # =====================================================
    @classmethod
    def get_bodega(cls, bodega_id: int, empresa_id: int):
        if not isinstance(bodega_id, int) or bodega_id <= 0:
            raise InvalidUsage("El ID de la bodega debe ser un número entero válido")

        bodega = cls.query.filter_by(id=bodega_id, empresa_id=empresa_id).first()
        if bodega is None:
            raise ObjectNotFound(f'La bodega con ID {bodega_id} no existe para esta empresa')
        return bodega

    # =====================================================
    # 🏗️ Crear una nueva bodega
    # =====================================================
    @classmethod
    def create_bodega(cls, modelo: dict, empresa_id: int):
        # Validaciones básicas
        nombre = modelo.get("nombre")
        direccion = modelo.get("direccion", "")
        descripcion = modelo.get("descripcion", "")

        if not nombre or not nombre.strip():
            raise InvalidUsage("El nombre de la bodega es obligatorio")

        # Verificar duplicados por nombre dentro de la empresa
        existente = cls.query.filter_by(nombre=nombre.strip(), empresa_id=empresa_id).first()
        if existente:
            raise InvalidUsage(f"Ya existe una bodega con el nombre '{nombre}' en esta empresa")

        bodega = cls(
            nombre=nombre.strip(),
            direccion=direccion.strip() if direccion else "",
            descripcion=descripcion.strip() if descripcion else "",
            empresa_id=empresa_id
        )
        bodega.save()
        return bodega

    # =====================================================
    # ✏️ Actualizar una bodega existente
    # =====================================================
    @classmethod
    def update_bodega(cls, modelo: dict, empresa_id: int):
        if "id" not in modelo:
            raise InvalidUsage("Debe proporcionar el ID de la bodega para actualizar")

        bodega = cls.get_bodega(modelo["id"], empresa_id)

        nuevo_nombre = modelo.get("nombre", bodega.nombre)
        nueva_direccion = modelo.get("direccion", bodega.direccion)
        nueva_descripcion = modelo.get("descripcion", bodega.descripcion)

        # Validar que no se repita el nombre con otra bodega
        if nuevo_nombre.strip() != bodega.nombre:
            duplicada = cls.query.filter(
                cls.nombre == nuevo_nombre.strip(),
                cls.empresa_id == empresa_id,
                cls.id != bodega.id
            ).first()
            if duplicada:
                raise InvalidUsage(f"Ya existe otra bodega con el nombre '{nuevo_nombre}'")

        bodega.nombre = nuevo_nombre.strip()
        bodega.direccion = nueva_direccion.strip() if nueva_direccion else ""
        bodega.descripcion = nueva_descripcion.strip() if nueva_descripcion else ""
        bodega.update()

        return bodega

    # =====================================================
    # 🗑️ Eliminar una bodega
    # =====================================================
    @classmethod
    def delete_bodega(cls, bodega_id: int, empresa_id: int):
        bodega = cls.get_bodega(bodega_id, empresa_id)

        # Validación: no eliminar si tiene documentos o movimientos asociados
        if bodega.documentos and len(bodega.documentos) > 0:
            raise InvalidUsage("No se puede eliminar la bodega porque tiene documentos asociados")

        # Si tienes movimientos relacionados:
        # if bodega.movimientos and len(bodega.movimientos) > 0:
        #     raise InvalidUsage("No se puede eliminar la bodega porque tiene movimientos asociados")

        bodega.delete()
        return bodega_id