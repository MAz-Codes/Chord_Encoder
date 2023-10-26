# Chord Encoder for a 36 Half-Tone System

This library provides functions to encode chords based on a 36 half-tone system. The chromatic scale is repeated three times to cover a range of 36 half-tones.

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
