# Transcrição de Áudio com Modelo de Linguagem Whisper
- Este é um exemplo simples de como usar o modelo de linguagem Whisper para transcrever áudio em Python. O Whisper é uma biblioteca de aprendizado de máquina desenvolvida para processamento de fala.

# Pré-requisitos
- Antes de começar, certifique-se de ter o Whisper instalado. Você pode instalá-lo usando:
pip install whisper

# Uso
Baixe o modelo Whisper pré-treinado:
- wget https://whisper-prod.s3.amazonaws.com/models/base_model.zip
- unzip base_model.zip -d base_model

# Adicione o código ao seu projeto:
import whisper
modelo = whisper.load_model("base_model")
resposta = modelo.transcribe("seu_audio.mp3")
print(resposta)
Certifique-se de substituir "seu_audio.mp3" pelo caminho do seu próprio arquivo de áudio.

# Execute o script:
python seu_script.py
Isso imprimirá a transcrição do áudio no console.

# Contribuições
- Contribuições são bem-vindas! Se você encontrar problemas ou melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

# Licença
- Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
