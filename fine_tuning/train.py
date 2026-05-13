from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
import numpy as np
import evaluate
import torch

# 1. CARICAMENTO E DIVISIONE DATASET
print("Caricamento dataset...")
full_dataset = load_dataset("hugginglearners/amazon-reviews-sentiment-analysis")

# Gestione della divisione Train/Test
if "test" not in full_dataset:
    dataset = full_dataset["train"].train_test_split(test_size=0.2)
else:
    dataset = full_dataset

# --- OTTIMIZZAZIONE PER IL 14 MAGGIO ---
# Prendiamo un sottoinsieme per finire il training in pochi minuti
#dataset["train"] = dataset["train"].select(range(1000)) 
#dataset["test"] = dataset["test"].select(range(200))
# ----------------------------------------

# 2. PREPARAZIONE TARGET (LABEL)
def map_sentiment(example):
    example["label"] = 1 if example["overall"] >= 4 else 0
    return example

print("Mappatura sentiment...")
dataset = dataset.map(map_sentiment)

# 3. TOKENIZZAZIONE
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

def tokenize_function(examples):
    text_column = [str(text) if text is not None else "" for text in examples["reviewText"]]
    return tokenizer(text_column, padding="max_length", truncation=True)

print("Tokenizzazione in corso...")
tokenized_datasets = dataset.map(tokenize_function, batched=True)

# 4. MODELLO
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)

# 5. METRICHE
metric = evaluate.load("accuracy")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)

# 6. IPERPARAMETRI
training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    num_train_epochs=1,
    weight_decay=0.01,
    logging_dir='./logs',
    push_to_hub=False,
)

# 7. TRAINER
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
    compute_metrics=compute_metrics,
)

# 8. ESECUZIONE
if __name__ == "__main__":
    print("\n--- Inizio Fine-Tuning per Lux-LLM ---")
    trainer.train()
    print("\nAddestramento completato con successo!")
