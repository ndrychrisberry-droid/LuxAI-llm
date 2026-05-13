
# Progetto finale: LuxAI-llm - Retail Intelligence
Autore: IChris Berry N'dry 

## Parte 1 — Fine-tuning
- **Modello scelto e motivazione:** Ho scelto `distilbert-base-uncased`. Essendo un modello "distillato", offre un eccellente bilanciamento tra le performance di un modello transformer puro e la leggerezza computazionale, permettendoci di fare fine-tuning su hardware locale senza incorrere in continui Out-Of-Memory (OOM).
- **Dataset scelto e motivazione:** `hugginglearners/amazon-reviews-sentiment-analysis`. Abbiamo optato per recensioni e-commerce reali perché l'obiettivo del progetto è applicare l'AI al settore retail (nello specifico, l'analisi del sentiment dei clienti per migliorare l'esperienza in store). 
- **Risultati ottenuti (metriche):** Configurati gli iperparametri (learning rate 2e-5, batch size 8), il modello ha calcolato l'accuracy sulle predizioni del validation set. Per ragioni di tempi di computazione legati alla data di consegna, l'addestramento è stato ridotto a un sottoinsieme rappresentativo per testare l'integrità della pipeline.
- **Difficoltà incontrate:**
  1. *Data Cleaning:* Valori nulli (NaN) nella colonna testo che causavano `TypeError` durante la tokenizzazione. Risolto forzando la conversione in stringa (`str(text)`).
  2. *Dataset Splitting:* Il dataset originale non prevedeva una chiave 'test' di default causando un `KeyError`. Risolto implementando un `train_test_split(test_size=0.2)` manuale.
  3. *Dipendenze:* Cambiamenti di sintassi nelle nuove versioni della libreria Transformers (es. `evaluation_strategy` deprecato in favore di `eval_strategy`).

## Parte 2 — Pipeline Ollama
- **Task scelto e motivazione:** Abbiamo creato un "Luxury Personal Shopper" virtuale. L'obiettivo è assistere il personale di vendita o il cliente suggerendo outfit o articoli (es. sneakers urban, abiti eleganti) basati sul contesto e sul tono di voce di una boutique di alto livello.
- **Strategie di prompting usate:** 1. *System Prompt personalizzato:* Per definire il ruolo, il tono colto e la conoscenza del dominio (materiali, brand).
  2. *Few-shot prompting:* Abbiamo inserito esempi strutturati (User/Assistant) nel codice per forzare il modello a rispondere con uno stile specifico e formattato prima di passargli la domanda reale.
- **Esempio di input/output:** - *Input:* "Cerco delle scarpe per tutti i giorni."
  - *Output:* "Per un look streetwear di tutti i giorni, le Air Force 1 bianche o le New Balance 550 sono la scelta più solida e versatile. Posso portarti anche una felpa in coordinato per completare l'outfit urbano."
- **Considerazioni sui risultati:** Il System Prompt è cruciale. Senza di esso il modello dava risposte robotiche e generiche. Con l'aggiunta del Few-shot, le risposte sono diventate molto più orientate alla vendita assistita, perfette per un'applicazione pratica in uno store fisico.