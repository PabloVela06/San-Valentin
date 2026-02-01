import streamlit as st
import random

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Para ti ❤️", page_icon="💌", layout="wide")

# 2. MEMORIA
if 'si' not in st.session_state:
    st.session_state.si = False
if 'pos_top' not in st.session_state:
    st.session_state.pos_top = None
if 'pos_left' not in st.session_state:
    st.session_state.pos_left = None

# 3. FUNCIÓN MOVIMIENTO
def mover_boton():
    st.session_state.pos_top = random.randint(10, 80)
    st.session_state.pos_left = random.randint(10, 80)

# 4. CSS DINÁMICO
if st.session_state.pos_top is not None:
    estilo_movimiento = f"""
        position: fixed !important;
        top: {st.session_state.pos_top}% !important;
        left: {st.session_state.pos_left}% !important;
        z-index: 9999 !important;
        width: auto !important;
        min-width: 150px !important;
        transition: top 0.15s ease, left 0.15s ease !important; 
    """
else:
    estilo_movimiento = "position: relative; transition: all 0.15s ease;"

# 5. INYECCIÓN DE ESTILOS PRINCIPALES (CON TEXTO NEGRO FORZADO)
st.markdown(f"""
<style>
    /* Ocultar elementos extra */
    header {{visibility: hidden;}} .stApp > header {{display: none;}} footer {{visibility: hidden;}}
    
    /* Fondo y alineación general */
    .stApp {{
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        background-color: #ffe6f0;
    }}
    
    /* Contenedor Flotante */
    div.block-container {{
        width: 100%; max-width: 1400px; padding: 2rem 0; margin: auto;
    }}

    /* TARJETA CENTRAL */
    div[data-testid="stColumn"]:nth-of-type(3) {{
        background-color: #fcfcfc;
        padding: 50px;
        border-radius: 30px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        border: 2px solid #ffbdd2;
        display: flex; flex-direction: column; justify-content: center; align-items: center;
        color: black !important; /* Forzamos texto negro */
    }}

    /* Limpieza de estilos fantasmas */
    div[data-testid="stColumn"] div[data-testid="stColumn"] {{
        background-color: transparent !important; box-shadow: none !important;
        border: none !important; padding: 0 !important;
    }}

    /* Textos (Forzamos color negro) */
    h1 {{ 
        text-align: center !important; width: 100%; margin-bottom: 0.5rem;
        color: black !important; 
    }}
    p {{ 
        text-align: center !important; width: 100%; font-size: 1.1rem;
        color: #333333 !important; 
    }}
    
    /* Texto de los botones */
    button p {{ color: inherit !important; }}

    /* Botones */
    div[data-testid="stButton"] button[kind="primary"] {{
        background-color: #FF69B4 !important; border: none !important; padding: 15px 30px !important;
        font-size: 20px !important; border-radius: 15px !important; width: 100%;
        box-shadow: 0 4px 10px rgba(255, 105, 180, 0.3);
        color: white !important; 
    }}
    div[data-testid="stButton"] button[kind="secondary"] {{
        {estilo_movimiento}
        background-color: #f0f2f6 !important; border: 1px solid #d6d6d8 !important;
        padding: 15px 30px !important; font-size: 20px !important; border-radius: 15px !important;
        color: black !important; 
    }}
</style>
""", unsafe_allow_html=True)

# 6. ESTRUCTURA (5 columnas para separar gatos)
col_izq, col_hueco1, col_cen, col_hueco2, col_der = st.columns([1.2, 0.5, 2, 0.5, 1.2], vertical_alignment="center")

with col_cen:
    st.markdown("""<div style="display: flex; justify-content: center; align-items: center; margin-bottom: 10px;">
            <img src="https://media1.tenor.com/m/X1XlcJhJPZUAAAAC/love.gif" width="250" style="border-radius: 10px; display: block;"></div>""", unsafe_allow_html=True)
    st.title("¿Quieres ser mi San Valentín? 🌹")
    
    # LÓGICA DEL TEXTO
    if st.session_state.si:
        st.write("¡SABÍA QUE DIRÍAS QUE SÍ! Te quiero mucho muchito ❤️")
    elif st.session_state.pos_top is not None:
        st.write("Uy no te he entendido bien, prueba otra vez 😋")
    else:
        st.write("Espero que digas que sí 🥰")
    st.write("") 
    
    # Los botones SOLO se muestran si NO ha dicho que sí todavía.
    if not st.session_state.si:
        btn_si, btn_no = st.columns(2)
        with btn_si:
            if st.button("¡SÍ!💖", type="primary"):
                st.balloons()
                st.session_state.pos_top = None; st.session_state.pos_left = None
                st.session_state.si = True
                st.rerun()
        with btn_no:
            if st.button("No...🥀", on_click=mover_boton): pass

# 7. ZONA DE GATITOS
if st.session_state.si:
    estilo_tarjeta_gato = """
        background-color: #fcfcfc; 
        padding: 20px; 
        border-radius: 25px; 
        border: 2px solid #ffbdd2; 
        box-shadow: 0 8px 30px rgba(0,0,0,0.1);
        width: fit-content; 
        margin: auto;
        line-height: 0; 
    """

    with col_izq:
        st.markdown(f"""
            <div style="{estilo_tarjeta_gato}">
                <img src="https://media1.tenor.com/m/HKLQMQlHz6gAAAAC/cat.gif" width="350" style="border-radius: 10px; display: block;">
            </div>
        """, unsafe_allow_html=True)
        
    with col_der:
        st.markdown(f"""
            <div style="{estilo_tarjeta_gato}">
                <img src="https://media1.tenor.com/m/HKLQMQlHz6gAAAAC/cat.gif" width="350" style="border-radius: 10px; display: block; transform: scaleX(-1);">
            </div>
        """, unsafe_allow_html=True)
