import requests
import json

def run_luxury_pipeline():
    url = "http://localhost:11434/api/generate"
    
    from config import SYSTEM_PROMPT, FEW_SHOT_EXAMPLES

system_instr = SYSTEM_PROMPT
few_shot_examples = FEW_SHOT_EXAMPLES
    
    print("--- Concierge Digitale Attivo (Ollama/Llama3) ---")
    print("(Scrivi 'esci' per chiudere)\n")

    while True:
        user_input = input("Cliente: ")
        
        if user_input.lower() in ['esci', 'exit', 'quit']:
            break

        payload = {
            "model": "llama3",
            "prompt": f"{system_prompt}\n{few_shot_examples}\n\nCliente: {user_input}\nConcierge:",
            "stream": False
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            # Mostriamo la risposta
            print(f"\nConcierge: {data['response']}\n")
            print("-" * 30)
        except Exception as e:
            print(f"\nErrore di connessione a Ollama: {e}")
            break

if __name__ == "__main__":
    run_luxury_pipeline()
