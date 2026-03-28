import os
import pandas as pd
from datasets import load_dataset

from models import initialize_chat_model
from processing import get_predicted_answer, get_most_common_answer
from evaluation import calculate_bertscore

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def main():
    model_name = "gpt-3.5-turbo"
    model = initialize_chat_model(model_name, OPENAI_API_KEY)

    dataset = load_dataset("gsm8k", "main", split="test")
    df = dataset.to_pandas()

    questions = df["question"].tolist()
    references = df["answer"].tolist()

    predictions = []
    steps_list = []

    for q in questions[:50]:  # اختصار للتجربة
        answers, steps = get_predicted_answer(q, model, None, None)
        final = get_most_common_answer(answers)

        predictions.append(final)
        steps_list.append(steps[0])

    P, R, F1 = calculate_bertscore(references[:50], steps_list)

    print(f"BERTScore F1: {F1:.4f}")

if __name__ == "__main__":
    main()
