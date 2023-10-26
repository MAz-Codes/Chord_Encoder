# Define a mapping of note names to integers (intervals from C)
note_mapping = {
    "C": 0,
    "C#": 1, "Db": 1,
    "D": 2,
    "D#": 3, "Eb": 3,
    "E": 4, "Fb": 4,
    "E#": 5, "F": 5,
    "F#": 6, "Gb": 6,
    "G": 7,
    "G#": 8, "Ab": 8,
    "A": 9,
    "A#": 10, "Bb": 10,
    "B": 11, "Cb": 11
}

# Mapping for note durations
duration_mapping = {
    "w": 4.000,  # Whole note
    "dh": 3.000,  # Dotted half note
    "h": 2.000,  # Half note
    "dq": 1.500,  # Dotted quarter note
    "q": 1.000, # Quarter note
    "tq": 0.666, # Quarter triplets
    "de": 0.750,  # Dotted eighth note
    "e": 0.500, # eighth note
    "te": 0.333, # eighth triplets
    "ds": 0.375, # Dotted sixteenth note
    "s": 0.250, # quarter note
}

def encode_note(note_with_duration):
    """Encode a note into its interval from C and its duration."""
    # Splitting note name and duration
    note_name = ''.join([char for char in note_with_duration if char.isalpha() and char.isupper()])
    duration_char = ''.join([char for char in note_with_duration if char != note_name])
    
    interval = note_mapping.get(note_name, None)
    duration_value = duration_mapping.get(duration_char, None)
    
    if interval is None or duration_value is None:
        raise ValueError(f"Invalid note or duration: {note_with_duration}")
    
    return (interval, duration_value)



def encode_melody(melody_notes):
    """Encode a sequence of melody notes into readable sequences."""
    return [encode_note(note + duration) for note, duration in melody_notes]


# Example usage:
melody = [("C", "q"), ("G", "h"), ("E", "q")]
encoded_melody = encode_melody(melody)
print(encoded_melody)
