
# Lux-LLM: Retail Intelligence & Brand Perception

 Chris Berry N'dry 
 Retail / Luxury Fashion

## Introduzione al progetto
Questo progetto nasce con l'obiettivo di applicare tecniche di Natural Language Processing (NLP) al settore del retail di lusso. L'idea è quella di fornire strumenti analitici per monitorare la percezione del brand e offrire un'esperienza di assistenza al cliente di alto livello.

---

## Parte 1 — Fine-tuning (Encoder-only)

### Modello scelto e motivazione
Ho scelto **DistilBERT** (`distilbert-base-uncased`) perché offre un eccellente compromesso tra prestazioni e velocità. Nel settore retail, è fondamentale avere modelli leggeri capaci di analizzare migliaia di recensioni in tempo reale senza richiedere infrastrutture eccessivamente costose.

### Dataset scelto e motivazione
Il dataset utilizzato è **Amazon Reviews Sentiment Analysis**. Sebbene sia un dataset generalista, rappresenta il punto di partenza ideale per addestrare il modello a riconoscere le sfumature del linguaggio dei consumatori (feedback positivi vs negativi). L'obiettivo è dimostrare come il modello possa essere poi specializzato sull'analisi di prodotti di lusso e calzature.
