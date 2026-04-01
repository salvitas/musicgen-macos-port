from audiocraft.models import MusicGen
import torchaudio

PROMPT = 'dark cinematic shark attack cue, ominous low drones, pulsing bass, tense strings'
OUT = 'shark_cue.wav'

def main():
    model = MusicGen.get_pretrained('facebook/musicgen-small')
    model.set_generation_params(duration=6)
    audio = model.generate([PROMPT])
    torchaudio.save(OUT, audio[0].cpu(), model.sample_rate)
    print(OUT)

if __name__ == '__main__':
    main()
