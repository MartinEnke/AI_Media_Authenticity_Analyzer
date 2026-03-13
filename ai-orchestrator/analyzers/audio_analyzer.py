import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Any


def generate_spectrogram(file_path: str) -> str:
    y, sr = librosa.load(file_path, sr=None, mono=True)
    spectrogram_path = file_path + "_spectrogram.png"

    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

    plt.figure(figsize=(10, 4))
    librosa.display.specshow(D, sr=sr, x_axis="time", y_axis="log")
    plt.colorbar(format="%+2.0f dB")
    plt.title("Spectrogram")
    plt.tight_layout()
    plt.savefig(spectrogram_path)
    plt.close()

    return spectrogram_path


def analyze_audio(file_path: str) -> Dict[str, Any]:
    y, sr = librosa.load(file_path, sr=None, mono=True)
    duration = librosa.get_duration(y=y, sr=sr)

    rms = librosa.feature.rms(y=y)[0]
    avg_rms = float(np.mean(rms))
    peak = float(np.max(np.abs(y)))

    zero_crossings = librosa.feature.zero_crossing_rate(y)[0]
    avg_zcr = float(np.mean(zero_crossings))

    flags = []
    base_score = 0.2

    if duration < 1.0:
        flags.append("very_short_audio")
        base_score += 0.10

    if peak > 0.99:
        flags.append("possible_clipping")
        base_score += 0.10

    spectrogram_path = generate_spectrogram(file_path)

    return {
        "sample_rate": sr,
        "duration_seconds": duration,
        "average_rms": avg_rms,
        "peak_amplitude": peak,
        "average_zero_crossing_rate": avg_zcr,
        "spectrogram_path": spectrogram_path,
        "flags": flags,
        "base_score": min(base_score, 0.95),
    }