from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# Cargar el modelo y el tokenizador
model_name = "distilgpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_advice(prompt: str) -> str:
    # Tokenizar el prompt
    inputs = tokenizer(prompt, return_tensors="pt")
    
    # Generar texto
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=150,  # Ajusta la longitud máxima del texto generado
            num_return_sequences=1,
            top_k=50,         # Controla la cantidad de palabras posibles a considerar
            pad_token_id=tokenizer.eos_token_id  # Configura el token de padding
        )
    
    print(outputs[0])

    # Decodificar el texto generado
    advice = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Limpiar el texto para evitar espacios en blanco excesivos
    advice = advice.strip()

    return advice
