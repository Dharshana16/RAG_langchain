from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load tokenizer and model manually (correct for FLAN-T5 in v5.x)
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

def generate_answer(context: str, question: str) -> str:
    """
    Generates grounded answer using FLAN-T5.
    """

    prompt = (
    "You are a helpful assistant.\n"
    "Answer clearly and briefly.\n"
    "If the answer is not explicitly in the context, say you don't know.\n\n"
    f"Context:\n{context}\n\n"
    f"Question:\n{question}\n\n"
    "Answer in one sentence:"
)

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=200
        )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer