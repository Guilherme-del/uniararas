from . import db

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)

class Casa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    endereco = db.Column(db.String(200), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    comodos = db.relationship('Comodo', backref='casa', lazy=True)

class Comodo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    casa_id = db.Column(db.Integer, db.ForeignKey('casa.id'), nullable=False)
    sensores = db.relationship('Sensor', secondary='comodo_x_sensores', backref=db.backref('comodos', lazy=True))

class ComodoXSensores(db.Model):
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), primary_key=True)
    comodo_id = db.Column(db.Integer, db.ForeignKey('comodo.id'), primary_key=True)
