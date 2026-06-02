import streamlit as st
import plotly.graph_objects as go

# Konfigurasi Halaman (Lebar Penuh untuk mode taktis)
st.set_page_config(page_title="Tactical Weather Dashboard", layout="wide")

# Custom CSS untuk warna Deep Navy Blue ala METOC
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #0A192F;
        color: white;
    }
    .main-header {
        background-color: #0A192F;
        padding: 15px;
        color: white;
        text-align: center;
        border-radius: 5px;
        margin-bottom: 20px;
        border-bottom: 3px solid #FFB300; /* Garis aksen kuning taktis */
    }
    </style>
""", unsafe_allow_html=True)

# 1. Header Banner
st.markdown('<div class="main-header"><h2>METEOROLOGY & CLIMATOLOGY TACTICAL PORTAL</h2></div>', unsafe_allow_html=True)

# 2. Sidebar Navigasi
with st.sidebar:
    st.markdown("### 🧭 NAVIGASI OPERASIONAL")
    st.write("---")
    menu = st.radio(
        "Pilih Panel Informasi:",
        ("📊 Observasi Aktual (API)", "📈 Aerodrome Climatological Summary", "⚠️ Sistem Peringatan Dini")
    )

# 3. Main Content Area (Berubah sesuai pilihan navigasi)
if menu == "📊 Observasi Aktual (API)":
    st.subheader("Kondisi Cuaca Permukaan Real-Time")
    st.write("Pantauan cuaca saat ini berdasarkan integrasi data API.")
    
    # Metrik Baris Pertama (Panel Kartu)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Arah & Kecepatan Angin", value="240° / 15 KT", delta="Stabil")
    col2.metric(label="Visibilitas", value="8 KM", delta="Clear")
    col3.metric(label="Suhu / Titik Embun", value="32°C / 26°C", delta="-1°C")
    col4.metric(label="QNH", value="1012 hPa", delta="Normal")
    
    st.divider()
    st.info("💡 Blok ini siap dihubungkan dengan skrip ekstraksi JSON dari API BMKG.")

elif menu == "📈 Aerodrome Climatological Summary":
    st.subheader("Ringkasan Statistik Klimatologi (ACS)")
    st.write("Referensi statistik jangka panjang untuk perencanaan operasional.")
    
    # Contoh visualisasi ACS menggunakan Plotly
    fig = go.Figure(data=[
        go.Bar(name='Rata-rata Curah Hujan (mm)', x=['Jan', 'Feb', 'Mar', 'Apr'], y=[250, 210, 180, 150], marker_color='#457b9d'),
        go.Scatter(name='Suhu Maksimum (°C)', x=['Jan', 'Feb', 'Mar', 'Apr'], y=[31, 32, 33, 33], mode='lines+markers', yaxis='y2', marker_color='#e63946')
    ])
    
    fig.update_layout(
        title="Tren Curah Hujan dan Suhu Permukaan",
        yaxis=dict(title='Curah Hujan (mm)'),
        yaxis2=dict(title='Suhu (°C)', overlaying='y', side='right'),
        barmode='group',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True)

else:
    st.subheader("Peringatan Cuaca Signifikan")
    # Menggunakan kotak peringatan bawaan Streamlit
    st.error("🚨 PERINGATAN: Deteksi awal potensi squall line di sektor barat laut dalam 2 jam ke depan.")
    st.warning("Status: Menunggu pembaruan analisis stabilitas atmosfer dan citra radar satelit.")
