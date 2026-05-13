import requests
import json

def run_luxury_pipeline():
    url = "http://localhost:11434/api/generate"
    
    # System Prompt richiesto dalla traccia
    system_prompt = "Sei un raffinato Concierge di una boutique di lusso. Rispondi in italiano in modo elegante e professionale."
    
    print("--- Concierge Digitale Attivo (Ollama/Llama3) ---")
    print("(Scrivi 'esci' per chiudere)\n")

    while True:
        user_input = input("Cliente: ")
        if user_input.lower() in ['esci', 'exit', 'quit']:
            break

        payload = {
            "model": "llama3",
            "prompt": f"{system_prompt}\n\nCliente: {user_input}",
            "stream": False
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            print(f"\nAssistant: {data['response']}\n")
            print("-" * 30)
        except Exception as e:
            print(f"\nErrore di connessione a Ollama: {e}")
            break

if __name__ == "__main__":
    run_luxury_pipeline()