from . import db

class Hogar(db.Model):
    __tablename__ = 'hogares'
    id_hogar = db.Column(db.String, primary_key=True)
    tipo_vivienda = db.Column(db.String)
    n_personas_vivienda = db.Column(db.String)
    presupuesto_compartido = db.Column(db.String)

class Persona(db.Model):
    __tablename__ = 'personas'
    id_hogar = db.Column(db.String, db.ForeignKey('hogares.id_hogar'), primary_key=True)
    id_persona = db.Column(db.String, primary_key=True)
    sexo = db.Column(db.String)
    edad = db.Column(db.String)


class Educacion(db.Model):
    __tablename__ = 'educacion'

    id_hogar = db.Column(db.String, db.ForeignKey('hogares.id_hogar'), primary_key=True)
    id_persona = db.Column(db.String, nullable=False, primary_key=True)
    asiste_educacion = db.Column(db.String)
    nivel_educacional = db.Column(db.String, primary_key=True)
    dependencia_establecimiento = db.Column(db.String)

    def __repr__(self):
        return f"<Educacion(id_hogar={self.id_hogar}, id_persona={self.id_persona}, nivel_educacional={self.nivel_educacional})>"

class Trabajo(db.Model):
    __tablename__ = 'trabajo'

    id_hogar = db.Column(db.String, primary_key=True)
    id_persona = db.Column(db.String, primary_key=True)
    ocupacion = db.Column(db.String, primary_key=True)
    tipo_contrato = db.Column(db.String)
    horas_trabajadas = db.Column(db.String)

    # Relación con la tabla personas
    id_hogar_fk = db.Column(db.String, db.ForeignKey('personas.id_hogar'))
    id_persona_fk = db.Column(db.String, db.ForeignKey('personas.id_persona'))

    def __repr__(self):
        return f"<Trabajo(id_hogar={self.id_hogar}, id_persona={self.id_persona}, ocupacion={self.ocupacion})>"
