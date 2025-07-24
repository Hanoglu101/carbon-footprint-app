from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey

# DB bağlantısı
engine = create_engine('sqlite:///karbon_app.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Kullanıcı Modeli
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

# Proje Modeli
class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    location = Column(String)
    start_date = Column(String)

# Faaliyet Verisi Modeli
class ActivityData(Base):
    __tablename__ = 'activity_data'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    activity_type = Column(String)
    source_description = Column(String)
    amount = Column(Float)
    unit = Column(String)
    emission_factor = Column(Float)
    scope = Column(String)
    emissions = Column(Float)

# Emisyon Katsayısı Modeli
class EmissionFactor(Base):
    __tablename__ = "emission_factors"

    id = Column(Integer, primary_key=True)
    category = Column(String)
    activity_type = Column(String)
    emission_factor = Column(Float)
    unit = Column(String)
    unit = Column(String)
    factor = Column(Float)
