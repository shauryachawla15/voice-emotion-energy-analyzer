# 🎙️ Voice Emotion Energy Analyzer

A lightweight **Audio AI / Digital Signal Processing (DSP)** tool built in Python that analyzes voice signals to extract important speech characteristics such as **pitch, energy, and speech activity**.

The project uses the powerful Python audio analysis library **Librosa** to process `.wav` audio files and generate insights about the voice signal.

This project is designed as a **simple but practical demonstration of audio feature extraction** used in areas like:

* Speech emotion recognition
* Voice analysis
* Audio signal processing
* Voice AI systems

---

# 🚀 Features

The analyzer extracts and visualizes key audio features:

• **Pitch Detection** – estimates the fundamental frequency of the voice
• **Energy Analysis** – measures voice intensity using RMS energy
• **Speech Activity Detection** – calculated using Zero Crossing Rate (ZCR)
• **Basic Emotion Hint** – simple heuristic based on pitch and energy levels
• **Waveform Visualization** – displays the audio waveform
• **Pitch Contour Plot** – shows pitch variation over time

---

# 🧠 How It Works

The system processes an input `.wav` audio file and performs the following steps:

1. Load the audio file
2. Extract audio features using Librosa
3. Compute:

   * RMS Energy
   * Pitch using YIN algorithm
   * Zero Crossing Rate
4. Generate basic emotion hints using feature thresholds
5. Display waveform and pitch graphs

These techniques are commonly used in **speech processing and audio machine learning pipelines**.

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/voice-emotion-energy-analyzer.git
cd voice-emotion-energy-analyzer
```

Create a virtual environment (recommended):

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

Place a `.wav` audio file inside the project folder.

Run the analyzer:

```bash
python veeaa.py sample.wav
```

Example output:

```
------ Voice Analysis ------

Average Pitch: 182 Hz
Energy Level: 0.041
Speech Activity (ZCR): 0.12
Emotion Hint: Neutral
```

Graphs will also appear showing:

• Audio waveform
• Pitch contour

---

# 📂 Project Structure

```
voice-emotion-energy-analyzer
│
├── veeaa.py            # Main analyzer script
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── sample.wav          # Example audio file
```

---

# 🛠 Tech Stack

* Python
* Librosa
* NumPy
* Matplotlib
* SoundFile

---

# 📊 Audio Features Explained

**Pitch (Fundamental Frequency)**
Represents the perceived frequency of the voice and is important for speech analysis.

**RMS Energy**
Measures the intensity or loudness of the signal.

**Zero Crossing Rate (ZCR)**
Measures how often the signal waveform crosses the zero axis, often used for speech activity detection.

---

# Outputs



