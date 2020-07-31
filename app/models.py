from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy


""" SQLAlchemy object, needed to be initialised with `db.init_app(app)`"""
db = SQLAlchemy()

class Record(db.Model):
    __tablename__ = 'imagerecord'

    id = db.Column(db.Integer, primary_key=True)
    uploadname = db.Column(db.String(120), unique=True, nullable=False)
    downloadname = db.Column(db.String(120), unique=True, nullable=True)
    converttype = db.Column(db.Integer, unique=False, nullable=False)

    def get_json(self):
        return {"id":self.id, "uploadname":self.uploadname, "downloadname": self.downloadname, "converttype": self.converttype}
