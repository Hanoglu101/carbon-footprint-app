import streamlit as st
from sqlalchemy.orm import Session
from models import User, Project, ActivityData
from database import session
import pandas as pd

st.set_page_config(page_title="Kullanıcı Özeti", layout="centered")

# 🔐 Kullanıcı oturum kontrolü
user = st.session_state.get("logged_in_user", None)

if user is None:
    st.warning("Lütfen önce giriş yapın.")
    st.stop()

# 🎯 Kullanıcıya ait verileri çek
total_projects = session.query(Project).filter_by(user_id=user.id).count()
total_activities = session.query(ActivityData).filter_by(user_id=user.id).count()
total_emission = session.query(ActivityData.total_emission).filter_by(user_id=user.id).all()
total_emission_sum = sum([em[0] for em in total_emission if em[0] is not None])

# 📊 Sayfa başlığı ve metrikler
st.title(f"👤 Kullanıcı Paneli Özeti")
st.markdown(f"*Ad Soyad:* {user.name}")
st.markdown(f"*E-posta:* {user.email}")
st.divider()

st.subheader("📈 Genel Bakış")
col1, col2, col3 = st.columns(3)
col1.metric("📁 Proje Sayısı", total_projects)
col2.metric("📝 Faaliyet Sayısı", total_activities)
col3.metric("🌍 Toplam Emisyon", f"{total_emission_sum:.2f} Kg CO₂e")
