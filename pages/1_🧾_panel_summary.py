import streamlit as st
from sqlalchemy.orm import Session
from models import User, Project, ActivityData
from database import session  # Eğer session = Session() burada tanımlıysa
import pandas as pd

# Sayfa yapılandırması
st.set_page_config(page_title="Kullanıcı Özeti", layout="centered")

# 🔐 Kullanıcı oturum kontrolü
if "username" not in st.session_state:
    st.warning("Lütfen önce giriş yapın.")
    st.stop()

# Giriş yapan kullanıcının e-posta adresi
user_email = st.session_state["username"]

# Kullanıcıyı veritabanından al
user = session.query(User).filter_by(email=user_email).first()

if user:
    # Kullanıcıya ait verileri çek
    total_projects = session.query(Project).filter_by(user_id=user.id).count()
    total_activities = session.query(ActivityData).filter_by(user_id=user.id).count()
    total_emissions = session.query(ActivityData.total_emission).filter_by(user_id=user.id).all()
    total_emission_sum = sum([em[0] for em in total_emissions if em[0] is not None])

    # 🎯 Sayfa başlığı ve özet
    st.title("📊 Kullanıcı Panel Özeti")
    st.markdown(f"👤 *Ad Soyad:* {user.name}")
    st.markdown(f"📧 *E-posta:* {user.email}")
    st.divider()

    st.subheader("🔍 Genel Bakış")

    col1, col2, col3 = st.columns(3)
    col1.metric("📁 Proje Sayısı", total_projects)
    col2.metric("🧾 Faaliyet Sayısı", total_activities)
    col3.metric("🌍 Toplam Emisyon", f"{total_emission_sum:.2f} kg CO₂e")

else:
    st.error("❌ Kullanıcı bulunamadı.")
