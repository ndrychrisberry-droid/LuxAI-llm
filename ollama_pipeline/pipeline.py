import requests
import json

def run_luxury_pipeline():
    url = "http://localhost:11434/api/generate"
    
    # System Prompt richiesto dalla traccia
    # System Prompt e Few-shot prompting combinati
        system_prompt = "Sei un raffinato Concierge di una boutique di lusso. Rispondi in italiano in modo elegante e professionale."
        
        few_shot_examples = """
        Esempio 1:
        Cliente: Cerco delle scarpe per tutti i giorni.
        Concierge: Per un look streetwear di tutti i giorni, le Air Force 1 bianche o le New Balance 550 sono la scelta più solida e versatile. Posso portarti anche una felpa in coordinato per completare l'outfit urbano.

        Esempio 2:
        Cliente: Vorrei qualcosa per una serata di gala.
        Concierge: Certamente. Le suggerisco un mocassino in pelle spazzolata o una stringata classica. Entrambe le opzioni conferiranno un tocco di indiscutibile raffinatezza al suo abbigliamento.
        """
        
        # ... [omissis] ...

        payload = {
            "model": "llama3",
            "prompt": f"{system_prompt}\n{few_shot_examples}\n\nCliente: {user_input}\nConcierge:",
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