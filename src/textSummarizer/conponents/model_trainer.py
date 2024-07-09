import os

from textSummarizer.entity import ModelTrainerConfig

from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import torch

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer,model_pegasus)

        samsum_dataset_pt = load_from_disk(self.config.data_path)
        print("model extracting")
        training_args = TrainingArguments(
            output_dir='artifacts/model_trainer', num_train_epochs=1, warmup_steps=500,
            per_device_train_batch_size=1, per_device_eval_batch_size=1,
            weight_decay=0.01, logging_steps=10,
            eval_strategy='steps', eval_steps=500, save_steps=1e6,
            gradient_accumulation_steps=16
        )

        trainer = Trainer(model=model_pegasus, args=training_args,
                  tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                  train_dataset=samsum_dataset_pt["test"], 
                  eval_dataset=samsum_dataset_pt["validation"])
        print("training model");
        trainer.train()

        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))
        
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))