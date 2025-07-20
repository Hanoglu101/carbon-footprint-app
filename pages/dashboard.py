import streamlit as st
from models import Session, User, Project, ActivityData

st.set_page_config(page_title="Kullanıcı Paneli", layout="wide")

# Oturum kontrolü
if 'username' not in st.session_state or 'name' not in st.session_state:
    st.warning("Lütfen önce giriş yapın.")
    st.stop()

user_email = st.session_state['username']
user_name = st.session_state['name']

def load_user_data(user_email):
    session = Session()
    user = session.query(User).filter_by(email=user_email).first()

    if not user:
        session.close()
        return 0, 0, 0.0

    user_id = user.id

    total_projects = session.query(Project).filter_by(user_id=user_id).count()
    total_activities = session.query(ActivityData).filter_by(user_id=user_id).count()
    total_emissions = session.query(ActivityData.total_emission).filter_by(user_id=user_id).all()

    total_emission_sum = sum([e[0] for e in total_emissions if e[0] is not None])

    session.close()
    return total_projects, total_activities, total_emission_sum


def run_dashboard(user_email, user_name):
    st.title("📊 Kullanıcı Paneli")
    st.subheader(f"Merhaba, {user_name} 👋")

    st.markdown("---")
    st.markdown("### 📌 Genel Bakış")

    projects, activities, emissions = load_user_data(user_email)

    col1, col2, col3 = st.columns(3)
    col1.metric("📁 Proje Sayısı", projects)
    col2.metric("📄 Faaliyet Sayısı", activities)
    col3.metric("🌍 Toplam Emisyon", f"{emissions:.2f} kg CO₂e")

# Fonksiyonu çağır
run_dashboard(user_email, user_name)
