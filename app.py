import streamlit as st
import base64
import os
import time

# --- 1. CONFIGURACIÓN Y FUNCIONES ---
st.set_page_config(
    page_title="Carlos Soto | Portfolio", 
    page_icon="🛡️", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

# --- 2. CARGA DE RECURSOS ---
ruta_base = os.path.dirname(__file__)
bg_img = get_base64('imagenciberseguridad.jpg')
perfil_img = get_base64('imagencarlos.jpg')
bg_card_img = get_base64('imagenciberseguridad2.jpg')
icon_habilidades_img = get_base64(os.path.join(ruta_base, 'iconohabilidades.png'))
img_sobre_mi = get_base64('imagensobremi.jpg')
img_sobre_mi = get_base64('imagentextosobremi.jpg')

# --- 3. DATOS ---
experiencias = [
    {
        "titulo": "Service Desk Analyst | Vector (Salcobrand)",
        "periodo": "08/2025 – Presente",
        "puntos": [
            "Gestión de identidades (IAM) en Azure AD (Entra ID) y Active Directory, administrando accesos y políticas de seguridad.",
            "Administración de Seguridad de Endpoints, incluyendo antivirus, endurecimiento de sistemas (Hardening) mediante GPOs y conectividad segura vía VPN (SSL/IPsec).",
            "Respuesta a incidentes N1/N2 bajo cumplimiento de SLA, realizando triaje y mitigación de amenazas.",
            "Control y gestión de activos para asegurar la trazabilidad del hardware y mitigar usos no autorizados."
        ]
    },
    {
        "titulo": "Soporte Técnico e Infraestructura IT | UpcomDTS",
        "periodo": "02/2023 – 07/2025",
        "puntos": [
            "Administración de seguridad en Microsoft 365, configurando controles de acceso e identidades en entornos híbridos.",
            "Implementación de accesos remotos seguros vía VPN y monitoreo de conectividad para garantizar la integridad de la red.",
            "Documentación de activos críticos y mantenimiento de hardware/software para asegurar la disponibilidad y continuidad operativa del negocio."
        ]
    },
    {
        "titulo": "Encargado de Computación | Red de Colegios SIP",
        "periodo": "01/2022 – 01/2023",
        "puntos": [
            "Gestión y segmentación de red segura mediante la configuración de Firewalls y Switches (L2/L3).",
            "Monitoreo de tráfico y detección de anomalías utilizando herramientas de sniffing para asegurar la integridad de la red.",
            "Administración integral de infraestructura física en Data Center, incluyendo gestión de Racks y sistemas de respaldo eléctrico (UPS).",
            "Control de acceso y filtrado de contenido conforme a normativas de seguridad y políticas institucionales."
        ]
    }
]

habilidades = {
    "Pentesting & Ethical Hacking": "Uso de herramientas como Metasploit, Nmap y Burp Suite para identificar vulnerabilidades.",
    "Hardening de Sistemas": "Endurecimiento de servidores y estaciones de trabajo bajo mejores prácticas de seguridad.",
    "OWASP Top 10": "Mitigación de los riesgos de seguridad más críticos en aplicaciones web.",
    "Criptografía": "Implementación de algoritmos y protocolos como PKI, AES y RSA.",
    "Gestión de Vulnerabilidades": "Identificación, clasificación y priorización de brechas mediante Nessus.",
    "Active Directory & Azure AD": "Administración avanzada de identidades, Entra ID y servicios de dominio.",
    "Networking & Protocolos": "Gestión de TCP/IP, segmentación VLANs, enrutamiento OSPF y túneles VPN SSL/IPsec.",
    "Firewalls": "Configuración y administración de reglas de seguridad perimetral.",
    "Linux (Ubuntu/Debian)": "Administración avanzada de sistemas, personalización de entorno y Bash scripting.",
    "Windows Server": "Gestión de infraestructura de servidores en entornos Windows.",
    "Análisis de Tráfico": "Captura y diagnóstico de paquetes de red mediante Wireshark.",
    "Docker & Virtualización": "Despliegue de contenedores y gestión de máquinas virtuales con VMware.",
    "Python para Seguridad": "Desarrollo de scripts para automatización de tareas y herramientas de seguridad.",
    "SQL": "Gestión de bases de datos relacionales y consultas.",
    "Normativas y Frameworks": "Conocimiento académico en ISO 27001 y NIST Cybersecurity Framework."
}

# --- 4. ESTILOS CSS GENERALES ---
fondo_b64 = bg_img if bg_img else ""
tarjeta_b64 = bg_card_img if bg_card_img else ""

st.markdown(f"""
    <style>
    /* Ocultar elementos por defecto de Streamlit y el margen superior */
    header {{visibility: hidden !important;}}
    .main .block-container {{ padding-top: 2rem !important; padding-bottom: 0rem; z-index: 10; position: relative; }}
    #MainMenu, footer {{visibility: hidden !important;}}
    
    /* FONDO PRINCIPAL: Directo al .stApp (como funcionaba antes) pero con espacio para moverse */
    .stApp {{
        background-image: linear-gradient(rgba(5, 10, 48, 0.95), rgba(0, 0, 0, 0.95)), url("data:image/jpeg;base64,{fondo_b64}") !important;
        background-size: 200% 200% !important; /* Lo hacemos el doble de grande para que pueda "viajar" */
        background-repeat: no-repeat !important;
        color: white !important;
        animation: moverFondo 30s linear infinite alternate !important;
    }}
    
    /* Animación de paneo horizontal sin el !important que a veces rompen los navegadores */
    @keyframes moverFondo {{
        0% {{ background-position: 0% 50%; }}
        100% {{ background-position: 100% 50%; }}
    }}

    @media (max-width: 640px) {{
        .stApp {{
            background-size: cover !important; 
            background-position: center center !important; 
            animation: none !important; /* Apagado en celular */
        }}
        .main .block-container {{ padding-top: 1rem !important; }}
    }}

    @keyframes fadeIn {{ 0% {{ opacity: 0; }} 100% {{ opacity: 1; }} }}
    @keyframes slideIn {{ 0% {{ transform: translateX(100px); opacity: 0; }} 100% {{ transform: translateX(0); opacity: 1; }} }}
    
    /* CSS Nav Menu */
    .nav-bar {{
        display: flex; justify-content: center; flex-wrap: wrap; gap: 25px;
        margin-top: 5px; margin-bottom: 35px; padding-bottom: 15px;
        border-bottom: 1px solid rgba(0, 242, 255, 0.2);
    }}
    .nav-link {{
        color: #dcdcdc !important; text-decoration: none; font-size: 17px; font-weight: bold;
        font-family: 'Segoe UI', sans-serif; transition: all 0.3s ease; padding: 5px 10px; border-radius: 8px;
    }}
    .nav-link:hover {{
        color: #00f2ff !important; background-color: rgba(0, 242, 255, 0.1); text-shadow: 0 0 10px rgba(0, 242, 255, 0.5);
    }}

    /* CSS Tarjetas de Experiencia */
    .exp-card {{
        background: linear-gradient(rgba(17, 34, 64, 0.85), rgba(17, 34, 64, 0.85)), url("data:image/jpeg;base64,{tarjeta_b64}");
        background-size: cover; background-position: center; padding: 40px; border-radius: 20px;
        border: 2px solid rgba(0, 242, 255, 0.3); backdrop-filter: blur(12px);
        animation: slideIn 0.8s ease-out, fadeIn 1.2s ease-out;
        transition: transform 0.3s ease, border 0.3s ease, box-shadow 0.3s ease;
    }}
    .exp-card:hover {{
        transform: scale(1.02); border: 2px solid #00f2ff; box-shadow: 0 0 35px rgba(0, 242, 255, 0.5);
    }}
    
    /* CSS Tags de Habilidades */
    .skill-tag {{
        background: rgba(0, 242, 255, 0.1); border: 1px solid #00f2ff; padding: 6px 14px; 
        border-radius: 15px; display: inline-block; margin: 5px; font-size: 14px;
        position: relative; cursor: pointer; color: white !important; font-weight: bold !important; transition: all 0.3s ease;
    }}
    .skill-tag:hover {{ background: rgba(0, 242, 255, 0.3); transform: translateY(-2px); box-shadow: 0 0 10px rgba(0, 242, 255, 0.5); }}
    .skill-tag:hover::after {{
        content: attr(data-description); position: absolute; bottom: 125%; left: 50%; transform: translateX(-50%);
        background: rgba(255, 255, 255, 0.95); color: #050a30; padding: 10px; border-radius: 8px; width: 200px;
        font-size: 12px; font-weight: bold; text-align: center; z-index: 1000; box-shadow: 0 0 15px rgba(0, 242, 255, 0.6);
        border: 1px solid #00f2ff; white-space: normal; line-height: 1.4;
    }}
    </style>
""", unsafe_allow_html=True)

# --- 5. SOCIAL HEADER ---
# Agregamos margin-top negativo (-40px) para "jalar" los íconos hacia arriba
st.markdown(f"""
<div style="display: flex; justify-content: flex-end; gap: 25px; padding: 0; margin-top: -40px; flex-wrap: wrap;">
    <a href="https://www.linkedin.com/in/carlos-e-soto-v%C3%A1squez-8366b3241" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" style="width: 32px; transition: transform 0.3s ease;">
    </a>
    <a href="mailto:sotovasquezcarlos1614@gmail.com">
        <img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Gmail_icon_%282020%29.svg" style="width: 32px; transition: transform 0.3s ease;">
    </a>
    <a href="https://www.instagram.com/" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174855.png" style="width: 32px; transition: transform 0.3s ease;">
    </a>
    <a href="https://www.facebook.com/" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/124/124010.png" style="width: 32px; transition: transform 0.3s ease;">
    </a>
</div>
""", unsafe_allow_html=True)

# --- 6. MENÚ DE NAVEGACIÓN ---
st.markdown("""
<div class="nav-bar">
    <a href="#experiencia" class="nav-link">Experiencia</a>
    <a href="#educacion" class="nav-link">Educación</a>
    <a href="#habilidades" class="nav-link">Habilidades Técnicas</a>
    <a href="#certificados" class="nav-link">Certificados y Cursos</a>
    <a href="#sobre-mi" class="nav-link">Sobre mí</a>
</div>
""", unsafe_allow_html=True)

# --- 7. HERO SECTION (Cabecera) ---
st.markdown(f"""
    <style>
    .hero-container {{ padding: 0px 0px 40px 10px; text-align: left; }}
    .header-group {{ display: flex; align-items: center; gap: 20px; margin-bottom: 10px; }}
    .hero-profile-pic {{
        width: 120px; height: 120px; border-radius: 50%;
        background-size: 180%; background-position: 70% 20%; background-repeat: no-repeat;
        border: 3px solid #00f2ff; box-shadow: 0 0 20px #00f2ff;
        transition: transform 0.3s ease; cursor: pointer;
    }}
    .hero-profile-pic:hover {{ transform: scale(1.15); }}
    .badge {{
        background-color: rgba(17, 34, 64, 0.8); border: 1px solid #00f2ff;
        color: white; padding: 5px 15px; border-radius: 20px; font-size: 14px; font-weight: bold;
    }}
    .salute {{ font-size: 50px; font-weight: 900; color: white; margin: 10px 0px; font-family: 'Segoe UI', sans-serif; }}
    .experience-para {{ font-size: 19px; line-height: 1.6; color: #f0f0f0; max-width: 800px; font-family: 'Segoe UI', sans-serif; }}
    .highlight {{ color: #fffd8d; font-weight: bold; }}
    @media (max-width: 640px) {{ .salute {{ font-size: 35px; }} }}
    </style>

    <div class="hero-container">
        <div class="header-group">
            <div class="hero-profile-pic" style="background-image: url('data:image/jpeg;base64,{perfil_img}');"></div>
            <div class="badge">Disponible para trabajar</div>
        </div>
        <div class="salute">Hey, soy Carlos Soto</div>
        <div class="experience-para">
            <span class="highlight">+4 años de experiencia</span>. 
            Estudiante de <span class="highlight">Ingeniería en Ciberseguridad</span> y Auditoría Informática 
            de Santiago de Chile cl. Especializado en el área de <span class="highlight">soporte técnico, infraestructura TI</span> 
            y gestión de identidades (IAM). Apasionado por crear soluciones seguras que generen valor real.
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 8. SECCIÓN EXPERIENCIA (Recuadros apilados) ---
# Nota: ID="experiencia" agregado aquí para el ancla del menú
st.markdown(f"""
    <div id="experiencia" style="display: flex; align-items: center; gap: 12px; margin-bottom: 25px; padding-left: 10px;">
        <img src="https://cdn-icons-png.flaticon.com/512/2092/2092204.png" width="35" height="35" style="filter: brightness(0) invert(1) drop-shadow(0 0 5px #00f2ff);">
        <h2 style="margin: 0; color: #00f2ff; font-size: 32px; font-family: 'Segoe UI', sans-serif;">Experiencia</h2>
    </div>
""", unsafe_allow_html=True)

for exp in experiencias:
    puntos_html = "".join([f"<li style='margin-bottom: 8px;'>{p}</li>" for p in exp['puntos']])
    st.markdown(f"""
    <div class="exp-card" style="margin-bottom: 35px; min-height: auto; padding: 35px;">
        <h2 style='text-align: left; margin-top: 0; font-size: 26px; color: #00f2ff;'>{exp['titulo']}</h2>
        <p style='color:#00f2ff; font-size: 18px; text-align: left; margin-bottom: 15px;'><b>{exp['periodo']}</b></p>
        <ul style='font-size: 17px; line-height: 1.6; color: #f0f0f0; text-align: left; margin: 0;'>{puntos_html}</ul>
    </div>
    """, unsafe_allow_html=True)

# --- 9. EDUCACIÓN Y HABILIDADES ---
st.markdown("---")
c1, c2 = st.columns(2)

with c1:
    # ID="educacion" agregado
    st.markdown(f"""
            <div id="educacion" style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
                <img src="https://cdn-icons-png.flaticon.com/512/3135/3135810.png" width="40" height="40" style="filter: brightness(0) invert(1) drop-shadow(0 0 5px #00f2ff);">
                <span style="color: #00f2ff; font-size: 28px; font-weight: bold; font-family: 'Segoe UI', sans-serif;">Educación</span>
            </div>
        """, unsafe_allow_html=True)
    st.write("**Ingeniería en Ciberseguridad y Auditoría Informática**")
    st.write("Universidad San Sebastián (03/2022 - Presente)")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ID="certificados" agregado
    st.markdown(f"""
            <div id="certificados" style="display: flex; align-items: center; gap: 12px; margin-top: 20px; margin-bottom: 10px;">
                <img src="https://cdn-icons-png.flaticon.com/512/2436/2436633.png" width="40" height="40" style="filter: brightness(0) invert(1) drop-shadow(0 0 5px #00f2ff);">
                <span style="color: #00f2ff; font-size: 28px; font-weight: bold; font-family: 'Segoe UI', sans-serif;">Certificados y Cursos</span>
            </div>
        """, unsafe_allow_html=True)
    certificados = ["NSE 1, 2 y 3 Fortinet", "Cisco Certified Network Associate (CCNA)", "Conceptos básicos de redes", "Introducción a la Ciberseguridad", "Personalización de entorno en Linux", "Licencia de conducir clase B"]
    for cert in certificados:
        st.write(f"• {cert}")

with c2:
    # ID="habilidades" agregado
    st.markdown(f"""
        <div id="habilidades" style="display: flex; align-items: center; gap: 12px; margin-bottom: 15px;">
          <img src="https://cdn-icons-png.flaticon.com/512/2092/2092663.png" width="45" height="45" style="vertical-align: middle; filter: brightness(0) invert(1) drop-shadow(0 0 5px #00f2ff);">
            <span style="color: #00f2ff; font-size: 28px; font-weight: bold;">Habilidades Técnicas</span>
        </div>
    """, unsafe_allow_html=True)
    html_habilidades = "".join([f'<span class="skill-tag" data-description="{desc}">{nombre}</span> ' for nombre, desc in habilidades.items()])
    st.markdown(html_habilidades, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")

# --- 10. TEXTO DE PERFIL / SOBRE MÍ ---
col_texto, col_img = st.columns([1.4, 1], vertical_alignment="center")

with col_texto:
    st.markdown(f"""
        <div id="sobre-mi" style="display: flex; justify-content: flex-start; align-items: center; gap: 12px; margin-bottom: 15px; padding-left: 5px;">
            <img src="https://cdn-icons-png.flaticon.com/512/1000/1000997.png" width="38" height="38" style="filter: brightness(0) invert(1) drop-shadow(0 0 5px #00f2ff);">
            <h2 style="margin: 0; color: #00f2ff; text-align: left; font-size: 32px;">Sobre Mí</h2>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <style>
        /* ESTE ES EL CSS QUE CREA EL EFECTO ZOOM */
        .efecto-zoom {{
            transition: transform 0.4s ease, box-shadow 0.4s ease !important;
            cursor: pointer;
        }}
        .efecto-zoom:hover {{
            transform: scale(1.06) !important; /* Agranda un 6% para que sea suave */
            box-shadow: 0 0 35px rgba(0, 242, 255, 0.6) !important;
            border-color: #00f2ff !important;
        }}
        </style>
        
        <div class="efecto-zoom" style="font-size: 17px; line-height: 1.6; text-align: justify; padding: 25px; background: rgba(17, 34, 64, 0.6); border-radius: 15px; border: 1px solid rgba(0, 242, 255, 0.2); box-shadow: 0 4px 15px rgba(0,0,0,0.3); margin: 0;">
            Soy un joven de 25 años profundamente apasionado por la tecnología y la ciberseguridad. Actualmente me encuentro cursando mi <b style="color: #fffd8d;">último año de la carrera de Ingeniería en Ciberseguridad y Auditoría Informática</b>. 
            <br><br>
            Me considero una persona proactiva y en constante aprendizaje; disfruto expandiendo mis conocimientos analíticos y técnicos, explorando siempre nuevas herramientas y metodologías dentro del mundo de la seguridad de la información. Cuando me alejo de las pantallas, <b style="color: #fffd8d;">mi otra gran pasión es el fútbol</b>, un deporte que disfruto muchísimo y que me ayuda a mantener un buen equilibrio, liberar estrés y aplicar el valor del trabajo en equipo en mi día a día.
            <br><br>
            A lo largo de mi trayectoria, he consolidado más de 4 años de experiencia en soporte técnico, infraestructura TI y gestión de identidades (IAM). Me especializo en el endurecimiento de sistemas (Hardening), redes bajo el modelo OSI y respuesta a incidentes (N1/N2). Mi objetivo profesional es seguir enfrentando nuevos desafíos e implementar soluciones que protejan los activos críticos bajo los más altos estándares operativos.
        </div>
    """, unsafe_allow_html=True)

with col_img:
    if img_sobre_mi:
        st.markdown(f"""
            <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                <img class="efecto-zoom" src="data:image/jpeg;base64,{img_sobre_mi}" style="width: 100%; max-width: 380px; height: auto; border-radius: 15px; border: 2px solid #00f2ff; box-shadow: 0 0 20px rgba(0, 242, 255, 0.3); object-fit: cover;">
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
