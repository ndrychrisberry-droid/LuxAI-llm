import streamlit as st
import requests
import time
import random

# --- 1. CONFIGURAZIONE PAGINA (Deve essere la prima istruzione) ---
st.set_page_config(page_title="L U X U R Y | Retail Intelligence", page_icon="✨", layout="wide")

# --- 2. STILE CSS DARK LUXURY ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Montserrat:wght@300;400&display=swap');

    .stApp {
        background-color: #0A0A0A;
        color: #E0E0E0;
        font-family: 'Montserrat', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #FFFFFF !important;
        letter-spacing: 2px;
    }

    [data-testid="stSidebar"] {
        background-color: #111111;
        border-right: 1px solid #222222;
    }

    .stButton>button {
        background-color: transparent;
        color: #FFFFFF;
        border-radius: 0px; 
        border: 1px solid #444444;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 10px;
        padding: 10px 20px;
        transition: 0.4s;
    }
    .stButton>button:hover {
        background-color: #FFFFFF;
        color: #000000;
    }

    .stChatInputContainer {
        border-radius: 0px !important;
        border: 1px solid #333333 !important;
        background-color: #111111 !important;
    }

    [data-testid="stChatMessage"] {
        background-color: transparent;
        border-bottom: 1px solid #1A1A1A;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. LOGICA OLLAMA (Llama 3) ---
def interroga_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    # System Prompt per definire l'identità del brand
    # System Prompt per definire l'identità del brand
    system_instr = "Sei un raffinato Concierge di una boutique di lusso. Rispondi in italiano. Sii elegante, colto e sintetico. Non usare emoji eccessive."
    
    # Esempi Few-shot per forzare il tono e la pertinenza nel dominio retail
    few_shot_examples = """
    Esempio 1:
    Cliente: Cerco delle scarpe per tutti i giorni.
    Concierge: Per un look streetwear di tutti i giorni, le Air Force 1 bianche o le New Balance 550 sono la scelta più solida e versatile. Posso portarti anche una felpa in coordinato per completare l'outfit urbano.

    Esempio 2:
    Cliente: Ho bisogno di un abito per un evento formale.
    Concierge: Sarà un piacere assisterla. Le propongo un abito sartoriale dal taglio avvitato in lana fredda. Lo abbinerei a una cravatta in seta per un'eleganza senza tempo.
    """

    # Iniezione del prompt strutturato
    payload = {
        "model": "llama3",
        "prompt": f"{system_instr}\n{few_shot_examples}\n\nCliente: {prompt}\nConcierge:",
        "stream": False
    }
    
    try:
        # Timeout di 10 secondi per evitare blocchi infiniti
        response = requests.post(url, json=payload, timeout=15)
        if response.status_code == 200:
            return response.json().get('response', "Spiacente, non riesco a elaborare la richiesta.")
        else:
            return "Il sistema di consulenza remota non risponde. Verificare la connessione locale."
    except requests.exceptions.ConnectionError:
        return "ERRORE DI CONNESSIONE: Assicurati che l'app Ollama sia avviata sul tuo PC."
    except Exception as e:
        return f"Nota tecnica: Il servizio Concierge è momentaneamente offline. ({str(e)})"

# --- 4. SIDEBAR & NAVIGAZIONE ---
st.sidebar.title("L U X U R Y")
st.sidebar.markdown("<p style='letter-spacing: 3px; font-size: 10px; color: #666;'>RETAIL INTELLIGENCE</p>", unsafe_allow_html=True)
st.sidebar.divider()

choice = st.sidebar.radio("NAVIGAZIONE", ["📊 MODULO ANALITICO", "💬 CONCIERGE DIGITALE"])

st.sidebar.divider()
st.sidebar.markdown("<small style='color: #444;'>Versione 2.0.1 - Local LLM Pipeline</small>", unsafe_allow_html=True)

# --- 5. MODULO ANALITICO (Simulazione Parte 1) ---
if choice == "📊 MODULO ANALITICO":
    st.header("Analisi Predittiva del Sentiment")
    st.markdown("*Monitoraggio delle performance del modello DistilBERT.*")
    
    if st.button("AVVIA DIAGNOSTICA"):
        progress = st.progress(0)
        status = st.empty()
        for i in range(100):
            time.sleep(0.03)
            progress.progress(i + 1)
            if i == 20: status.text("Caricamento pesi del modello...")
            if i == 60: status.text("Valutazione accuracy sul dataset test...")
        
        st.success("Diagnostica completata.")
        st.divider()
        c1, c2, c3 = st.columns(3)
        c1.metric("Accuratezza Finale", "89.4%", "Sentiment Analysis")
        c2.metric("Loss", "0.241", "-0.05")
        c3.metric("Dataset Size", "100%", "Full Load")

# --- 6. CONCIERGE DIGITALE (Parte 2 con Ollama) ---
else:
    st.header("Concierge Digitale")
    st.markdown("*Servizio Clienti Esclusivo assistito da Llama 3.*")
    st.divider()

    # Inizializzazione memoria chat
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Benvenuto. È un piacere riceverla. Come posso assisterla oggi nella sua esperienza di shopping?"}
        ]

    # Visualizzazione messaggi
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    # Input utente
    if prompt := st.chat_input("Inserisca qui la sua richiesta..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Consultando l'archivio..."):
                risposta = interroga_ollama(prompt)
                st.markdown(risposta)
                st.session_state.messages.append({"role": "assistant", "content": risposta})