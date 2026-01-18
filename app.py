import streamlit as st
import base64

# ================= HELPER =================
def img_to_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="My RizkyAS",
    layout="wide"
)

# ================= GLOBAL STYLE =================
st.markdown("""
<style>
/* MAIN BACKGROUND */
.stApp {
    background-color: #ffffff;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #f1f5f9;
}

/* REMOVE DEFAULT CONTAINER COLOR */
div[data-testid="stVerticalBlock"] {
    background-color: transparent;
}

/* GLOBAL TEXT */
html, body, [class*="css"] {
    color: #111111;
}

/* ===== HEADER SQL TAGLINE ===== */
.sql-tagline {
    text-align: center;
    font-family: 'Courier New', monospace;
    font-size: 15px;
    color: #7A1E1E;
    margin-bottom: 5px;
    font-weight: bold;
}

/* ===== MAIN NAME HEADER ===== */
.main-name {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    color: #7A1E1E;
    margin-bottom: 5px;
}

/* ===== SUBTITLE ===== */
.sub-title {
    text-align: center;
    font-size: 20px;
    color: #2F4F4F;
    margin-bottom: 20px;
}

/* SECTION TITLE */
.section-title {
    color: #FFFFFF;
    background: linear-gradient(to right, #7A1E1E, #a83232);
    padding: 12px 18px;
    border-radius: 10px;
    font-weight: bold;
    margin-top: 35px;
}

/* PROFILE IMAGE */
.profile-img {
    display: flex;
    justify-content: center;
    margin: 25px 0;
}

.profile-img img {
    width: 180px;
    height: 180px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid #7A1E1E;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
}

/* SOCIAL ICONS */
.social-icons {
    display: flex;
    gap: 20px;
    align-items: center;
    justify-content: center;
    margin-top: 10px;
}

.social-icons img {
    width: 32px;
    height: 32px;
    cursor: pointer;
    transition: transform 0.2s ease;
}

.social-icons img:hover {
    transform: scale(1.2);
}

.contact-icons {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 24px;
    margin-top: 10px;
}

.contact-icons a {
    display: flex;
    align-items: center;
    justify-content: center;
}

.contact-icons img {
    width: 36px !important;
    height: 36px !important;
}
</style>
""", unsafe_allow_html=True)


# ================= SIDEBAR =================
st.sidebar.title("📌 Rizky A.S")
st.sidebar.markdown("""
- [01. About Me](#about-me)
- [02. Projects](#projects)
- [03. Certificates & Experience](#certificates)
- [04. About](#contact)
""")

# ================= HEADER =================
st.markdown("""
<div class="sql-tagline">
    SELECT * FROM me WHERE role = 'Data Analyst';
</div>

<div class="main-name">
    Rizky Agung Setiawan
</div>

<div class="sub-title">
    Junior Data Analyst
</div>
""", unsafe_allow_html=True)

ig = img_to_base64("assets/sosmed/logoig.png")
ln = img_to_base64("assets/sosmed/logoin.png")
gh = img_to_base64("assets/sosmed/logogit.png")
em = img_to_base64("assets/sosmed/logomail.png")

st.markdown(f"""
<div class="social-icons">
    <a href="https://www.instagram.com/iky_o1" target="_blank">
        <img src="data:image/png;base64,{ig}">
    </a>
    <a href="https://www.linkedin.com/in/rizky-agung-setiawan" target="_blank">
        <img src="data:image/png;base64,{ln}">
    </a>
    <a href="https://github.com/ucupcupacups" target="_blank">
        <img src="data:image/png;base64,{gh}">
    </a>
    <a href="mailto:agungrizky733@gmail.com">
        <img src="data:image/png;base64,{em}">
    </a>
</div>
""", unsafe_allow_html=True)

st.divider()

# ================= ABOUT ME =================
st.markdown('<div id="about-me"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">01. 👋 About Me</div>', unsafe_allow_html=True)

st.write("""
Saya adalah **fresh graduate Sarjana Komputer (S.Kom) Universitas Pamulang**
dengan minat kuat pada bidang **Data**, khususnya sebagai **Data Analyst**. Saya terbiasa melakukan pengolahan data, visualisasi, serta membangun sistem berbasis web melalui tugas akademik, kerja praktek, dan penelitian skripsi.
""")

st.write("""
Saya memiliki kemampuan dasar dalam **MySQL**, **Microsoft Excel**, dan **Python**,
serta sedang aktif mendalami **Machine Learning** untuk memperkuat kemampuan
analisis data dan pengambilan keputusan berbasis data.
""")

# ===== FOTO PROFILE =====
img_base64 = img_to_base64("assets/me/gua.jpeg")
st.markdown(f"""
<div class="profile-img">
    <img src="data:image/jpeg;base64,{img_base64}">
</div>
""", unsafe_allow_html=True)

# ================= SKILLS =================
st.subheader("🛠️ My Skills")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
**Hard Skills / Tools**
- Python (Basic)
- MySQL
- Microsoft Excel
- Streamlit (basic)
- Google Colab
- PHP Native
- HTML, CSS, Bootstrap
""")

with c2:
    st.markdown("""
**Soft Skills**
- Analytical Thinking  
- Problem Solving  
- Fast Learner  
- Attention to Detail  
- Teamwork  
- Time Management  
""")

with c3:
    st.markdown("""
**Languages**
- Bahasa Indonesia (Native)
- English (Basic – Intermediate)
""")

st.divider()

# ================= PROJECTS =================
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">02. 📊 Projects</div>', unsafe_allow_html=True)

# ---------- PROJECT 1 ----------
st.header("📊 Project 1 – Data Analyst")
st.write("""
Analisis dan perbandingan metode **K-Nearest Neighbor (KNN)** dan
**Decision Tree C4.5** untuk memprediksi curah hujan di
**Kota Tangerang Selatan** berdasarkan data BMKG Stasiun Klimatologi Banten.
""")

st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
st.image(
    "assets/project/hujan.png",
    caption="Dashboard Prediksi Curah Hujan – Streamlit",
    width=450
)
st.markdown("</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("🧠 Information")
    st.markdown("""
- **Dataset**: BMKG  
- **Tools**: Python (Google Colab)  
- **Libraries**: Pandas, NumPy, Scikit-learn  
- **Process**: Data Cleaning, EDA, Modeling, Evaluation
""")

with col2:
    st.subheader("📈 Insight")
    st.markdown("""
- Decision Tree C4.5 memberikan performa lebih stabil
- Parameter KNN sangat mempengaruhi akurasi
- Visualisasi membantu analisis pola curah hujan
""")
    st.markdown("🔗 **[Lihat Dashboard Streamlit 👈](https://dataminingcurahhujantangsel.streamlit.app/)**")

st.divider()

# ---------- PROJECT 2 ----------
st.header("💻 Project 2 – Sistem Tabungan Siswa")
st.write("""
Sistem Informasi Tabungan Siswa berbasis web untuk
**SMA Bina Indonesia Gemilang Depok** dengan dukungan multi-role user.
""")

st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
st.image(
    "assets/project/tabsis.png",
    caption="Sistem Tabungan Siswa – Web Application",
    width=450
)
st.markdown("</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("🧠 Information")
    st.markdown("""
- **Platform**: PHP Native  
- **Database**: MySQL  
- **Roles**: Admin, Petugas, Orang Tua  
- **Fitur**: CRUD, Transaksi, Laporan
""")

with col2:
    st.subheader("📈 Insight")
    st.markdown("""
- Implementasi Role-Based Access Control
- Data tabungan terstruktur & terdokumentasi
- Laporan mempermudah monitoring
""")
    st.markdown("🔗 **[Source Code GitHub 👈](https://github.com/ucupcupacups/binaindonesia)**")

st.divider()

# ---------- PROJECT 3 ----------
st.header("🗄️ Project 3 – SQL Database")
st.write("""
Perancangan dan implementasi **SQL** menggunakan **Microsoft SQL Server** untuk mengelola data.
""")

# Screenshot Project 3
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
st.image(
    "assets/project/sql_siakad.png",
    caption="Query & Struktur Database – SQL Server",
    width=450
)
st.markdown("</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("🧠 Information")
    st.markdown("""
- **Database Engine**: Microsoft SQL Server  
- **Tools**: SQL Server Management Studio (SSMS)  
- **Techniques**:
  - DDL (CREATE, ALTER, DROP)
  - DML (INSERT, UPDATE, DELETE)
  - JOIN (INNER, LEFT)
  - Stored Procedure
  - Trigger
""")

with col2:
    st.subheader("📈 Insight")
    st.markdown("""
- Database dirancang dengan **relational approach** dan primary–foreign key
- Query digunakan untuk menampilkan data
- Stored procedure membantu standarisasi proses pengambilan data
- Trigger digunakan untuk menjaga **validasi dan konsistensi data**
- Proyek ini menunjukkan pemahaman **struktur data, relasi, dan query logic**
""")
    st.markdown("🔗 **[Dokumentasi SQL 👈](https://drive.google.com/file/d/1hwFLt_fy4xHNW4NGaHCWZE6Z0Xtvy5eH/view?usp=drive_link)**")

st.divider()

# ================= CERTIFICATES =================
st.markdown('<div id="certificates"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">03. 📜 Academic Certificates & Experience</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.subheader("🎓 Akademik")
    st.markdown("""
- Universitas Pamulang – IPK 3.57  
- Sertifikat TOEFL  
- Sertifikat BNSP Programmer  
- Aktif seminar & webinar IT  
""")
with st.expander("📄 Lihat Sertifikat Akademik"): 
    st.image( 
        "assets/certificates/toefl.png",
        caption="Sertifikat TOEFL",
        use_container_width=True )

    st.image(
        "assets/certificates/bnsp1.png",
        caption="Sertifikat BNSP–Programmer",
        use_container_width=True ) 
        
    st.image(
        "assets/certificates/bnsp2.png",
        caption="Daftar Unit Kompetensi", 
        use_container_width=True )


with c2:
    st.subheader("🤝 Non-Akademik")
    st.markdown("""
- Kepanitiaan Latihan Dasar Kepemimpinan Siswa   -> Koordinator Divisi Peralatan  
- Aktif Kejuaraan Olahraga Tingkat Nasional & Kota 
- Aktif dalam organisasi kemahasiswaan saat kuliah
""")

with st.expander("📄 Lihat Sertifikat Non-Akademik"): 
    st.image(
        "assets/certificates/voli.png",
        caption="Sertifikat Juara III - Pekan Olahraga Pelajar Tingkat Kota Jakarta Pusat",
        use_container_width=True ) 
    
    st.image(
        "assets/certificates/voli2.png",
        caption="Sertifikat Juara Voli - Festival Olahraga Rakyat Sepanjang Tahun DKI Jakarta",
        use_container_width=True ) 
    
    st.image(
        "assets/certificates/karate.png",
        caption="Sertifikat Juara II Jurus Junior Putra - Kejuaraan Nasional Karate Funakoshi Indonesia Tahun 2019",
        use_container_width=True )

with c3:
    st.subheader("📜 Experience")
    st.markdown("""
    - Pengabdian Kepada Masyarakat -> SMP Falatehan Kota Tangerang Selatan **2023**
    - MAPALA Archa Buana Universitas Pamulang -> Anggota Muda Divisi Gunung Hutan **2023**
    - Kerja Praktek -> SMA Bina Indonesia Gemilang Depok **2024**

    """)

with st.expander("📄 Lihat Experience & Skill"): 
   
    st.image(
        "assets/certificates/pkm.png",
        caption="Kegiatan PKM - SMP Falatehan Tangsel 2023",
        use_container_width=True )

    st.image(
        "assets/certificates/mapala.png",
        caption="Sertifikat Organisasi - Pecinta Alam",
        use_container_width=True ) 

    st.image(
       "assets/certificates/big.png",
        caption="Kegiatan Kerja Praktek - SMA Bina Indonesia Gemilang 2024",
        use_container_width=True )
    
    st.image(
       "assets/certificates/sql.png",
        caption="Sertifikat Sololearn - Introduction to SQL",
        use_container_width=True )

    st.image(
       "assets/certificates/sql2.png",
        caption="Setifikat Sololearn - SQL Intermediate",
        use_container_width=True )
    
    st.image(
       "assets/certificates/css.png",
        caption="Sertifikat Sololearn - Introduction to CSS",
        use_container_width=True )

    st.image(
       "assets/certificates/html.png",
        caption="Sertifikat Sololearn - Introduction to HTML",
        use_container_width=True )

    st.image(
       "assets/certificates/java.png",
        caption="Sertifikat Sololearn - Introduction to JavaScript",
        use_container_width=True )

st.divider()


# ================= CONTACT =================
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">📬 2025 | Rizky A.S</div>', unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; padding:20px 0; color: #555; font-size: 14px;">
    <strong>2025 | Rizky AS</strong><br><br>
    This portfolio website was built using <b>Python</b>, <b>Streamlit</b>, 
    <b>HTML</b>, and <b>CSS</b>.<br>
    Designed and developed by <b>Rizky Agung Setiawan</b>.
</div>
""", unsafe_allow_html=True)
mail = img_to_base64("assets/sosmed/logomail.png")
git  = img_to_base64("assets/sosmed/logogit.png")
ig   = img_to_base64("assets/sosmed/logoig.png")
ln   = img_to_base64("assets/sosmed/logoin.png")

st.markdown("""
<div class="contact-icons">
<a href="https://github.com/ucupcupacups" target="_blank">
    <img src="data:image/png;base64,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" title="GitHub">
</a>

<a href="https://www.instagram.com/iky_o1" target="_blank">
    <img src="data:image/png;base64,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"title="Instagram">
</a>

<a href="https://www.linkedin.com/in/rizky-agung-setiawan" target="_blank">
    <img src="data:image/png;base64=data:image/png;base64,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" title="LinkedIn">
</a>
</div>
""", unsafe_allow_html=True)
