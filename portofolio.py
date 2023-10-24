import streamlit as st 
from PIL import Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.set_page_config(layout="wide")



with open("st.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

col1,col2=st.columns(2,gap="small")
with col1 :
    #     # Path ke foto
    photo_path = "/home/hendra/Dokumen/portofolio/img/11zon_cropped.png"
    # Tampilkan foto
    st.image(photo_path, width=300)
with col2 :
    st.title('Hendra Cahyo Setiawan')
    st.subheader("Welcome to my profile! :wave:")
    st.write("I am a recent graduate from Padang Institute of Technology with an interest in informatics engineering. I have experience in various fields, including project management, ERP implementation, and software development.")
    
    # Icon kecil untuk tautan sosial media
    st.write("[Instagram](https://www.instagram.com/bi.ruu_/) | [GitHub](https://github.com/Hendrasetyawan1945) | [LinkedIn](https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile)")

    st.write("Feel free to contact me or follow my profile on these platforms.")
st.write('---')

col1, col2 = st.columns([3,1])
with col1:
    st.header("Career Objective")
    st.write("I am Hendra Cahyo Setiawan, a fresh graduate from Padang Institute of Technology with GPA 3.87, majoring in Informatics Engineering. I have experience in participating in various industry programs, including SIB ERP Studies, Hasmicro bootcamp on Odoo ERP, and FGA Database SQL Oracle bootcamp. My passion for learning comes from my work experience which encourages me to keep developing myself. I always focus on understanding challenging material and am willing to go the extra mile in the learning process. During this journey, I have built my teamwork skills and am always ready to collaborate. Currently, I am still in the study stage, but I have a vision to apply these skills more effectively in the future.")

st.write('---')

with col2:
    st.header("Additional Skills")
    st.write('🚀 Manajemen Proyek')
    st.write('📊 Implementasi ERP')
    st.write('🐍 Python')
    st.write('🔍 C++')
    st.write('🌐 HTML, CSS, Bootstrap')
    st.write('📦 Odoo & Database')

col1,col2=st.columns(2)
with col1:
    st.write('\n')
    st.subheader("Experience & Qulifications")
    st.write(
        """
        - ✔️ Business Needs Analysis - Accounting and Finance
        - ✔️ Business Needs Analysis - Supply Chain 
        - ✔️ Create a Blueprint Project document and manage changes in the document. 
        - ✔️ Manage time analysis of problems, solutions, and user responses • Business Needs Analysis - Manufacturing
        - ✔️ Designing the system according to the Blueprint 
        - ✔️ Plan go-live and daily activities 
        - ✔️ Create training plans, and train end users 
        - ✔️ Lead a small team to conduct training and provide solutions to users 
        - ✔️ Implement dynamic team collaboration
        """
        )

with col2:
    st.write('\n')
    st.subheader("Education")
    st.image("data:image/png;base64,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", width=50)  # Ganti dengan URL ikon sekolah
    st.markdown("### Institut Teknologi Padang")
    st.write("Tahun: 2019 - 2023")
    st.markdown('<img src="https://img.icons8.com/color/452/star--v2.png" width="20" height="20"> **GPA: 3.87/4.0**', unsafe_allow_html=True)
    st.write("Technical Information")

st.write('---')
st.subheader("Certifications")
col1,col2=st.columns(2)
with col1:
    st.markdown("📜 Database Design and programin with sql  "'<a href="https://drive.google.com/file/d/1PFJHDdtlmbML3Cwp2vJL-tJYKWddvXYo/view?usp=drive_link" target="_blank" download><img src="https://img.icons8.com/color/452/pdf.png" width="16"> Download Sertifikat</a>', unsafe_allow_html=True)
    st.markdown("📊 Database Programing Oracel  "'<a href="https://drive.google.com/file/d/1PGTtOJ9EDl-tY-_fuw9eDm1XGUAGXtb7/view?usp=drive_link" target="_blank" download><img src="https://img.icons8.com/color/452/pdf.png" width="16"> Download Sertifikat</a>', unsafe_allow_html=True)
    st.markdown("🐍Belajar Dasar Data Science  "'<a href="https://drive.google.com/file/d/1WWTtZq1Y_kzyBn-TuJKO_VCB9JYkjBPJ/view?usp=sharing" target="_blank" download><img src="https://img.icons8.com/color/452/pdf.png" width="16"> Download Sertifikat</a>', unsafe_allow_html=True)
    st.markdown("🌐 Memulai Pemrograman dengan Haskell  "'<a href="https://drive.google.com/file/d/1KN85CzYvufVFUeYc8vau-2J816nFIOIU/view?usp=sharing" target="_blank" download><img src="https://img.icons8.com/color/452/pdf.png" width="16"> Download Sertifikat</a>', unsafe_allow_html=True)
    st.markdown("🚀 Belajar Dasar Structured Query Language (SQL)  "'<a href="https://drive.google.com/file/d/19uPnXqfJdrV2Tfkct0pelfryr9SBHkl5/view?usp=sharing" target="_blank" download><img src="https://img.icons8.com/color/452/pdf.png" width="16"> Download Sertifikat</a>', unsafe_allow_html=True)
    st.markdown("🔍Belajar Dasar-Dasar DevOps  "'<a href="https://drive.google.com/file/d/1VqbjrMiDlRnPfyNQK-mu8-33CgFuwSaA/view?usp=sharing" target="_blank" download><img src="https://img.icons8.com/color/452/pdf.png" width="16"> Download Sertifikat</a>', unsafe_allow_html=True)
    st.markdown("👨‍💻Belajar Dasar Git dengan GitHub  "'<a href="https://drive.google.com/file/d/1-WOVwhH1qkF3PA0lopeBvcA2sQq-4ZUj/view?usp=sharing" target="_blank" download><img src="https://img.icons8.com/color/452/pdf.png" width="16"> Download Sertifikat</a>', unsafe_allow_html=True)
    st.markdown("📧Belajar Dasar Pemrograman JavaScript  "'<a href="https://drive.google.com/file/d/1GIGZ8FrPDmqm4gDH3Imk9MC9JDi_1-wK/view?usp=sharing" target="_blank" download><img src="https://img.icons8.com/color/452/pdf.png" width="16"> Download Sertifikat</a>', unsafe_allow_html=True)
    st.markdown("📸 Cloud Practitioner Essentials (Belajar Dasar AWS Cloud)   "'<a href="https://drive.google.com/file/d/1z2lS9nSuU_IKa6HNHdAXl6m4llxgmXrH/view?usp=sharing" target="_blank" download><img src="https://img.icons8.com/color/452/pdf.png" width="16"> Download Sertifikat</a>', unsafe_allow_html=True)

with col2:
    st.markdown("🔗Memulai Dasar Pemrograman untuk Menjadi Pengemban Software  "'<a href="https://drive.google.com/file/d/1uk8uEkxONMW370jK_91oiLxqridRfjD4/view?usp=sharing" target="_blank" download><img src="https://img.icons8.com/color/452/pdf.png" width="16"> Download Sertifikat</a>', unsafe_allow_html=True)
    st.markdown("🗂️Memulai Pemrograman Dengan Dart  "'<a href="https://drive.google.com/file/d/1ULoqLngQrO9hgADZUGpRE1I62umNBztJ/view?usp=sharing" target="_blank" download><img src="https://img.icons8.com/color/452/pdf.png" width="16"> Download Sertifikat</a>', unsafe_allow_html=True)
    st.markdown("📰Belajar Dasar Visualisasi Data  "'<a href="https://drive.google.com/file/d/1oIQDcc8TaAZbRxV3Y3FY3yW3EOiM3Gqd/view?usp=sharing" target="_blank" download><img src="https://img.icons8.com/color/452/pdf.png" width="16"> Download Sertifikat</a>', unsafe_allow_html=True)
    st.markdown("📅Belajar Prinsip Pemrograman SOLID "'<a href="https://drive.google.com/file/d/1AAh0xlVlANRiOTKk66oZ3Bq5I7LgTHHi/view?usp=sharing" target="_blank" download><img src="https://img.icons8.com/color/452/pdf.png" width="16"> Download Sertifikat</a>', unsafe_allow_html=True)
    st.markdown("📚Belajar Dasar Pemrograman Web  "'<a href="https://drive.google.com/file/d/1wUFHJHO7wo5TYiCe6hlsxTtbo5-mxjaG/view?usp=sharing" target="_blank" download><img src="https://img.icons8.com/color/452/pdf.png" width="16"> Download Sertifikat</a>', unsafe_allow_html=True)
    st.markdown("📋Memulai Pemrograman Dengan Python "'<a href="https://drive.google.com/file/d/1G8r3fYa3awACpVxWwZQZ6BThJwtVquoa/view?usp=sharing" target="_blank" download><img src="https://img.icons8.com/color/452/pdf.png" width="16"> Download Sertifikat</a>', unsafe_allow_html=True)
    st.markdown("🎯 Program SIB : ERP Pada Industri Kecil dan Menegah   "'<a href="https://drive.google.com/file/d/1FI6jA06KupqcsUxzFUdOv0b8AtQpeWgd/view?usp=sharing" target="_blank" download><img src="https://img.icons8.com/color/452/pdf.png" width="16"> Download Sertifikat</a>', unsafe_allow_html=True)
    st.markdown("📫HIT Bootcamp in ERP Programing "'<a href="https://drive.google.com/file/d/1OfUBOMmjcB7hkFhDNx8aBwYz1ulkOrXZ/view?usp=sharing" target="_blank" download><img src="https://img.icons8.com/color/452/pdf.png" width="16"> Download Sertifikat</a>', unsafe_allow_html=True)
    st.markdown("📝 Python Fundamental for Data Science "'<a href="https://drive.google.com/file/d/1W2iWAwdUlcd3_0LtSjvYh1fURgK7X8g2/view?usp=sharing" target="_blank" download><img src="https://img.icons8.com/color/452/pdf.png" width="16"> Download Sertifikat</a>', unsafe_allow_html=True)


st.write('---')


st.caption('Copyright (c) Hendra Cahyo Setiawan 2023')
