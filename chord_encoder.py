#The Chord Index is: Major ="M", Minor ="m", Dominant ="D", Diminished ="d".
#You can combine them with numbers, flats and sharps to create top notes and tentions.
#For example Cmajor7#11 will be ["C", "M7#11"], or a D#7b9b13 will be ["D#","D7b9b13"] etc.

# Define an enharmonic mapping
enharmonic_mapping = {
    "C#": "Db",
    "Db": "C#",
    "D#": "Eb",
    "Eb": "D#",
    "F#": "Gb",
    "Gb": "F#",
    "G#": "Ab",
    "Ab": "G#",
    "A#": "Bb",
    "Bb": "A#",
    "B#": "C",
    "C" : "B#",
    "E#": "F",
    "F" : "E#"
}
# Define the original chromatic scale and associated functions
chromatic_scale_36 = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B",
                        "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B",
                        "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]




def get_enharmonic(note):
    """Return the enharmonic equivalent of a note, if it exists."""
    return enharmonic_mapping.get(note, note)

def chord_to_notes_36(root, chord_type):
    """Given a root note and a chord type, return the notes of the chord in a 36 half tone system."""

    root = root if root in chromatic_scale_36 else get_enharmonic(root)
    
    # Define chord templates as intervals for the 24 half tone system
    chord_templates = {
        "M": [0, 4, 7],
        "m": [0, 3, 7],
        "M7": [0, 4, 7, 11],
        "m7": [0, 3, 7, 10],
        "d": [0, 3, 6],
        "d7": [0, 3, 6, 9],
        "m9": [0, 3, 7, 10, 14],
        "m11": [0, 3, 7, 10, 14, 17],
        "m13": [0, 3, 7, 10, 14, 17, 21],
        "D7": [0, 4, 7, 10],
        "m7b5": [0, 3, 6, 10],
        "M6": [0, 4, 7, 9],
        "M9": [0, 4, 7, 11, 14],
        "m6": [0, 3, 7, 9],
        "M#11": [0, 4, 7, 11, 14, 18],
        "M13": [0, 4, 7, 11, 14, 18, 21],
        "D7b5": [0, 4, 6, 10],
        "D7#9": [0, 4, 7, 10, 15],
        "D7b9": [0, 4, 7, 10, 13],
        "D7#5": [0, 4, 8, 10],
        "D7b9b13": [0, 4, 7, 10, 13, 20],
    }
    
    # Calculate the notes in the chord based on the root and the chord type
    root_idx = chromatic_scale_36.index(root)
    chord_intervals = chord_templates[chord_type]
    chord_notes = [(root_idx + interval) % 36 for interval in chord_intervals]
    
    return [chromatic_scale_36[idx] for idx in chord_notes]



def encode_chord(root, chord_type):
    """Encode the chord in a 36 half-tone system with the root always being the first note to receive a 1.
    
    Args:
        root (str): The root note of the chord.
        chord_type (str): The type of chord based on the chord index.

    Returns:
        list: An encoded list of length 36, where each position corresponds to a half-tone in the chromatic scale.
              A value of '1' at a position indicates the presence of that note in the chord.
    """
    chord_notes = chord_to_notes_36(root, chord_type)
    encoded = [0] * 36

    # Convert the root to its enharmonic equivalent if it exists
    root_enharmonic = root if root in chromatic_scale_36 else get_enharmonic(root)
    
    # Find the position of the root note in the chromatic scale
    root_position = chromatic_scale_36.index(root_enharmonic)
    
    # Mark the root note first in the encoded list
    encoded[root_position] = 1
    
    # Mark the positions of the other notes of the chord relative to the root in the encoded list
    for note in chord_notes:
        if note != root_enharmonic:
            position = (chromatic_scale_36.index(note) - root_position) % 12 + root_position
            encoded[position % 36] = 1


    # Convert the chord notes to their enharmonic versions (if available)
    chord_notes_enharmonic = [get_enharmonic(note) for note in chord_notes]

    print("*Unnecessary Information*The chord notes are: " + ', '.join(chord_notes if root in chromatic_scale_36 else chord_notes_enharmonic))
    
    return encoded

# Testing the function with a root of F#
encode_chord("Eb", "D7b9b13")
