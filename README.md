# Chord and Melody Data Pre-Processing for Machine Learning Models

This project encompasses a system to preprocess musical data, designed to facilitate the training of an improvisational algorithm. The project consists of three main components:

1. **Melody Encoder**: Converts melodies into a sequence of note intervals and durations.
2. **Chord Encoder**: Encodes chords based on a 36 half-tone system.
3. **Dataset Creator**: A script that combines the outputs of the Melody and Chord Encoders to produce a dataset suitable for training.

## Melody Encoder:

The melody encoder takes a sequence of notes and their respective durations, then encodes them into a sequence of intervals from the note C and the respective note durations.

**Usage**:

```python
from melody_encoder import encode_melody

melody = [("C", "q"), ("G", "h"), ("E", "q")]
encoded_melody = encode_melody(melody)
print(encoded_melody)
```

## Chord Encoder for a 36 Half-Tone System

The chord encoder provides functions to encode chords based on a 36 half-tone system. The chromatic scale is repeated three times to cover a range of 36 half-tones.

## Features:

- **Enharmonic Mapping**: Converts notes to their enharmonic equivalents, e.g., C# to Db.
- **Chord to Notes**: Converts a root note and a chord type into the notes that constitute that chord in the 36 half-tone system.
- **Encode Chord**: Provides an encoded representation of a chord in the 36 half-tone system.

## Usage:

1. **Defining a Chord**:
   The Chord Index follows specific conventions:

   - Major = "M"
   - Minor = "m"
   - Dominant = "D"
   - Diminished = "d"

   These basic chord types can be combined with numbers, flats, and sharps to create top notes and tensions.
   Example: "Cmajor7#11" is represented as ["C", "M7#11"]

2. **Getting the Enharmonic Equivalent**:
   ```python
   note = "Db"
   print(get_enharmonic(note))  # Outputs: C#
   ```

## Getting Chord Notes:

```python
 root = "C"
 chord_type = "M7#11"
 print(chord_to_notes_36(root, chord_type))  # Outputs: ['C', 'E', 'G', 'B', 'F#']
```

## Encoding a Chord:

```python
 root = "C"
 chord_type = "M7#11"
 print(encode_chord(root, chord_type))  # Outputs the encoded representation in the 36 half-tone system

```

## DataSetCreator

This script integrates the outputs of the Melody and Chord Encoders. It takes a list of melodies and chords, encodes them using the respective encoders, and then combines the encoded results to generate a dataset.

**Usage**:

Simply run the dataset_creator.py script after ensuring that the Melody and Chord Encoder modules are available in the same directory or are appropriately imported.
