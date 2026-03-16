import librosa
import numpy as np
import matplotlib.pyplot as plt

file = "sample1.wav"

y, sr = librosa.load(file)

# Energy
energy = np.mean(librosa.feature.rms(y=y))

# Pitch using YIN
f0 = librosa.yin(y, fmin=50, fmax=400)
pitch = np.nanmean(f0)

# Zero crossing rate (speech activity)
zcr = np.mean(librosa.feature.zero_crossing_rate(y))

print("------ Voice Analysis ------")
print(f"Average Pitch: {pitch:.2f} Hz")
print(f"Energy Level: {energy:.4f}")
print(f"Speech Activity (ZCR): {zcr:.4f}")

# Emotion Hint (very basic rule)
if pitch > 200 and energy > 0.05:
    emotion = "Excited"
elif pitch < 120 and energy < 0.03:
    emotion = "Calm"
else:
    emotion = "Neutral"

print("Emotion Hint:", emotion)

# Plot waveform
plt.figure(figsize=(10,4))
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform")
plt.show()

# Plot pitch contour
plt.figure(figsize=(10,4))
plt.plot(f0)
plt.title("Pitch Contour")
plt.ylabel("Frequency (Hz)")
plt.show()