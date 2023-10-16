import sys

import librosa
import soundfile as sf

subject = sys.argv[1]
date    = sys.argv[2]

y, sr = librosa.load(
    f'./zip/wav/{subject}-{date}.wav',
    sr=16000,
    mono=True
)

sf.write(
    f'./wav/{subject}.wav',
    y, sr, subtype='PCM_16'
)