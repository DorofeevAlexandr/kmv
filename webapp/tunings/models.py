from webapp.db import db

class Lines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    line_number = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    port = db.Column(db.Integer, nullable=False)
    adr = db.Column(db.Integer, nullable=False)
    k = db.Column(db.Float, nullable=False)
    no_connection_counter = db.Column(db.Boolean, nullable=True)
    indikator_value = db.Column(db.Integer, nullable=True)
    length = db.Column(db.Float, nullable=True)
    speed_line = db.Column(db.Float, nullable=True)
    description = db.Column(db.String, nullable=True)
    created_dt = db.Column(db.DateTime, nullable=True)
    updated_dt = db.Column(db.DateTime, nullable=True)


    def __repr__(self):
        result = f'{self.id} name = {self.name}, '
        result += f'{self.length} ' 
        return result