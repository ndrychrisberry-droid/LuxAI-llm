
# 🛍️ LuxAI-LLM: Retail Intelligence & Concierge Digitale

Un'applicazione AI-driven sviluppata in **Streamlit** e progettata per rivoluzionare l'esperienza cliente all'interno degli store fisici. Il progetto integra modelli di Natural Language Processing (NLP) e Large Language Models (LLM) eseguiti in locale per fornire analisi in tempo reale e assistenza alla vendita.

## 🎯 Obiettivo del Progetto
Nel settore Fashion & Luxury, la personalizzazione dell'esperienza e la comprensione del cliente sono fondamentali. Questo progetto mira a:
1. **Analizzare il feedback** dei clienti in tempo reale per estrarre insight sul sentiment.
2. **Supportare lo staff di vendita** (o i clienti stessi) attraverso un assistente virtuale intelligente capace di suggerire abbinamenti e strategie di cross-selling mirate.

## ⚙️ Stack Tecnologico e Architettura
Il progetto sfrutta un'architettura ibrida di modelli di intelligenza artificiale:

*   **Interfaccia Utente:** App **Streamlit** per una dashboard interattiva e user-friendly.
*   **Sentiment Analysis:** Pipeline NLP basata su **DistilBERT** per analizzare testi e interazioni, classificando il sentiment del cliente in modo rapido ed efficiente.
*   **Concierge Digitale (LLM):** Modello **Llama 3** eseguito interamente in locale tramite **Ollama** per garantire massima privacy dei dati.
*   **Prompt Engineering:** Ottimizzazione del modello linguistico tramite tecniche di **Few-Shot Prompting** per generare risposte altamente contestualizzate e suggerimenti di **cross-selling** realistici.

## 🚀 Funzionalità Principali
- **Analisi del Sentiment Istantanea:** Inserendo log di conversazioni o feedback dei clienti, il modello DistilBERT valuta immediatamente la soddisfazione del cliente.
- **Motore di Cross-Selling:** Il "Concierge Digitale" riceve l'input sugli articoli a cui il cliente è interessato e, sfruttando il Few-Shot Prompting, genera suggerimenti di up-selling e cross-selling in perfetto stile retail.
- **Privacy by Design:** L'utilizzo di Ollama permette di processare dati sensibili dei clienti interamente in locale, senza appoggiarsi a server cloud esterni o API a pagamento.

## ⚠️ Note sulla Demo e Limitazioni Attuali
L'interfaccia Streamlit include un pulsante "AVVIA DIAGNOSTICA" progettato come mock-up UI per dimostrare la user experience finale per lo staff in store. Attualmente, l'animazione della progress bar e l'output del 89.4% sono simulati per scopi dimostrativi. Nelle prossime release, questa funzione verrà collegata direttamente agli script di validazione per mostrare le metriche di inferenza del modello aggiornate in tempo reale.

## 🛠️ Come installare ed eseguire il progetto

1. **Clona la repository:**
   ```bash
   git clone [https://github.com/ndrychrisberry-droid/LuxAI-llm.git](https://github.com/ndrychrisberry-droid/LuxAI-llm.git)
   cd LuxAI-llm
