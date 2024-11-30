from mido import Message, MidiFile, MidiTrack

# Create a new MIDI file and add a track
midi = MidiFile()
track = MidiTrack()
midi.tracks.append(track)

# Define a simple piano melody
notes = [
    (60, 480),  # C4, 1 beat
    (62, 480),  # D4
    (64, 480),  # E4
    (65, 480),  # F4
    (67, 480),  # G4
    (65, 480),  # F4
    (64, 480),  # E4
    (62, 480),  # D4
    (60, 960),  # C4, 2 beats
]

for note, duration in notes:
    track.append(Message('note_on', note=note, velocity=64, time=0))
    track.append(Message('note_off', note=note, velocity=64, time=duration))

# Save the file
with open("SaiGonDiuDangTrongToi.mid", "wb") as output_file:
    midi.save(output_file)

print("MIDI file created: SaiGonDiuDangTrongToi.mid")
