import datetime
from sqlalchemy import DateTime, Float
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    balance = db.Column(db.Integer, nullable=False)

    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance
# class Patient(db.Model):
#     __tablename__="patients"
#     PatientID = db.Column(db.Integer, primary_key=True)
#     Geslacht = db.Column(db.String(1), nullable=False)
#     Geboortedatum = db.Column(db.DateTime, nullable=False)
#     Status = db.Column(db.String(1), nullable=False)
#     episode = db.relationship("Episode", backref="patients")
#     lab = db.relationship("Lab", backref="patients")
#     med = db.relationship("Med", backref="patients")
#     contact = db.relationship("Contact", backref="patients")
#
#     def __init__(self, PatientID, Geslacht, Geboortedatum, Status):
#         self.PatientID = PatientID
#         self.Geslacht = Geslacht #V=woman, M=man
#         self.Geboortedatum = Geboortedatum
#         self.Status = Status
#
# class Episode(db.Model):
#     __tablename__="episodes"
#     id = db.Column(db.Integer, primary_key=True)
#     PatientID = db.Column(db.Integer, db.ForeignKey("patients.PatientID"))
#     EpisodeID = db.Column(db.Integer, nullable=False)
#     EpisodeTitel = db.Column(db.String(128), nullable=False)
#     ICPC = db.Column(db.String(128), nullable=False)
#     ICD = db.Column(db.String(128), nullable=False)
#     EpisodeStart = db.Column(db.DateTime, nullable=False)
#     EpisodeEind = db.Column(db.DateTime)
#
#     def __init__(self, EpisodeID, EpisodeTitel, ICPC, ICD, EpisodeStart, EpisodeEind):
#         self.EpisodeID = EpisodeID
#         self.EpisodeTitel = EpisodeTitel
#         self.ICPC = ICPC
#         self.ICD = ICD
#         self.EpisodeStart = EpisodeStart
#         self.EpisodeEind = EpisodeEind
#
# class Lab(db.Model):
#     __tablename__="labs"
#     id = db.Column(db.Integer, primary_key=True)
#     PatientID =db.Column(db.Integer, db.ForeignKey("patients.PatientID"))
#     Memocode = db.Column(db.String(128), nullable=False)
#     Mat = db.Column(db.String(128), nullable=False)
#     Bijz = db.Column(db.String(128), nullable=False)
#     DatumAanvraag = db.Column(db.DateTime, nullable=False)
#     UitslagDiag = db.Column(db.Float(precision=10, decimal_return_scale=None), nullable=False)
#     Ondergrens = db.Column(db.Float(precision=10, decimal_return_scale=None), nullable=False)
#     Bovengrens = db.Column(db.Float(precision=10, decimal_return_scale=None), nullable=False)
#
#     def __init__(self, Memocode, Mat, Bijz, DatumAanvraag, UitslagDiag, Ondergrens, Bovengrens):
#         self.Memocode = Memocode
#         self.Mat = Mat
#         self.Bijz = Bijz
#         self.DatumAanvraag = DatumAanvraag
#         self.UitslagDiag = UitslagDiag
#         self.Ondergrens = Ondergrens
#         self.Bovengrens = Bovengrens
#
# class Med(db.Model):
#     __tablename__="meds"
#     id = db.Column(db.Integer, primary_key=True)
#     PatientID = db.Column(db.Integer, db.ForeignKey("patients.PatientID"))
#     ATCCODE = db.Column(db.String(128), nullable=False)
#     Dosering = db.Column(db.String(128), nullable=False)
#     StartMedicatie = db.Column(db.DateTime, nullable=False)
#     VervalMedicatie = db.Column(db.DateTime)
#
#     def __init__(self, ATCCODE, Dosering, StartMedicatie, VervalMedicatie):
#         self.ATCCODE = ATCCODE
#         self.Dosering = Dosering
#         self.StartMedicatie = StartMedicatie
#         self.VervalMedicatie = VervalMedicatie
#
# class Contact(db.Model):
#     __tablename__="contacts"
#     id = db.Column(db.Integer, primary_key=True)
#     PatientID = db.Column(db.Integer, db.ForeignKey("patients.PatientID"))
#     ContactDatum = db.Column(db.DateTime, nullable=False)
#     ContactID = db.Column(db.Integer, nullable=False)
#     ICPC = db.Column(db.String(128), nullable=False)
#     SOEP = db.Column(db.String(128), nullable=False)
#     SOEPtekst = db.Column(db.String(128), nullable=False)
#
#     def __init__(self, ContactDatum, ContactID, ICPC, SOEP, SOEPtekst):
#         self.ContactDatum = ContactDatum
#         self.ContactID = ContactID
#         self.ICPC = ICPC
#         self.SOEP = SOEP
#         self.SOEPtekst = SOEPtekst
#
# class Test(db.Model):
#     __tablename__="tests"
#     id = db.Column(db.Integer, primary_key=True)
#     Memocode = db.Column(db.String(128), nullable=False)
#     Ondergrens = db.Column(db.Float(precision=10, decimal_return_scale=None), nullable=False)
#     Bovengrens = db.Column(db.Float(precision=10, decimal_return_scale=None), nullable=False)
#
#     def __init__(self, Memocode, Ondergrens, Bovengrens):
#         self.Memocode = Memocode
#         self.Ondergrens = Ondergrens
#         self.Bovengrens = Bovengrens
