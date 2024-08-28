from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from typing import Tuple

device = "cuda:0" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert").to(device)
labels = ["positive", "negative", "neutral"]

def estimate_sentiment(news: list[str]) -> Tuple[float, str]:
    if news:
        tokens = tokenizer(news, return_tensors="pt", padding=True).to(device)
        result = model(tokens["input_ids"], attention_mask=tokens["attention_mask"])["logits"]
        result = torch.nn.functional.softmax(torch.sum(result, 0), dim=-1)
        probability = result[torch.argmax(result)].item()
        sentiment = labels[torch.argmax(result).item()]
        return probability, sentiment
    else:
        return 0.0, "neutral"

if __name__ == "__main__":
    tensor, sentiment = estimate_sentiment(['markets responded negatively to the news!', 'traders were displeased!'])
    print(tensor, sentiment)
    print(torch.cuda.is_available())