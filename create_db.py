from models import Base, engine, EmissionFactor, User
from database import session

# Tabloları oluştur
Base.metadata.create_all(engine)
print("✅ Veritabanı başarıyla oluşturuldu: karbon_app.db")

# Örnek emisyon faktörleri (sadece bir kere çalıştır)
sample_factors = [
    EmissionFactor(category="Elektrik", unit="kWh", emission_factor=0.233, source="IEA"),
    EmissionFactor(category="Doğalgaz", unit="m3", emission_factor=2.02, source="IEA"),
    EmissionFactor(category="Benzin", unit="litre", emission_factor=2.31, source="IEA"),
    EmissionFactor(category="Dizel", unit="litre", emission_factor=2.68, source="IEA"),
    EmissionFactor(category="Uçuş", unit="km", emission_factor=0.09, source="ICAO")
]

session.add_all(sample_factors)

# Örnek kullanıcı
sample_user = User(name="Nihan", email="nihan@example.com", password="1234")
session.add(sample_user)

session.commit()
print("✅ Örnek emisyon faktörleri ve kullanıcı eklendi.")
