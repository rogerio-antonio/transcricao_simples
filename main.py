import whisper

modelo = whisper.load_model("base")

resposta = modelo.transcribe("my.mp3")

print(resposta)



