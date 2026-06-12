# Un script simple pour tester les réponses de l'IA
import subprocess

def ask_ai(prompt):
    # Appel de llama-cli avec votre modèle téléchargé
    cmd = ["llama-cli", "-m", "model.gguf", "-p", prompt, "-n", "20"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

# Test Textuel
print("Test Textuel : Allume la lumière")
print(ask_ai("Allume la lumière"))
