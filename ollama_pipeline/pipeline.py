from transformers import pipeline

print("Caricamento del Personal Shopper leggero...")
# Usiamo un modello piccolo (GPT-2 o simile) che non richiede Ollama
generator = pipeline('text-generation', model='gpt2')

def luxury_chat(user_input):
    # Prompt semplificato per modelli piccoli
    prompt = f"Context: I am a luxury personal shopper in Via Roma. Customer asks: {user_input} Answer:"
    
    res = generator(prompt, max_new_tokens=50, num_return_sequences=1, truncation=True)
    return res[0]['generated_text'].split("Answer:")[1]

if __name__ == "__main__":
    print("\n--- Lux-LLM: Modalità Emergenza attiva ---")
    while True:
        domanda = input("Cliente: ")
        if domanda.lower() in ['esci', 'exit']: break
        
        try:
            risposta = luxury_chat(domanda)
            print(f"\nAssistant: {risposta}\n")
        except Exception as e:
            print(f"Errore: {e}")