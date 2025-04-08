# Chatbot con Llama 3.2 y Streamlit

Este proyecto utiliza el modelo `llama-3.2-1b-instruct` a través de LM Studio, integrándolo en una interfaz web con **Streamlit** para construir un chatbot conversacional.

## Paso 1: Configurar LM Studio

1. Descarga LM Studio desde [lmstudio.ai](https://lmstudio.ai).
2. Dentro de LM Studio, descarga el modelo `llama-3.2-1b-instruct`.
3. Asegúrate de que el servidor de LM Studio esté corriendo localmente.

## Paso 2: Probar el modelo con Python

```python
import lmstudio as lms

model = lms.llm("llama-3.2-1b-instruct")
result = model.respond("What is the meaning of life?")
print(result)

