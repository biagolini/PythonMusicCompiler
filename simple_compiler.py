import os
import random
from pydub import AudioSegment

# Define the output format (mp3 or wav)
output_format = "mp3"  # Default is mp3

# Define the folder containing the audio files
source_audio_folder = "SourceFiles"

# Define the folder to deposit the audio combination file
destination_audio_folder = "OutputFiles"

# Define the output file name (default is None)
output_file_name = None  # If None, the file name will match the destination folder name

# Definition of fade in (first 3 seconds) and fade out (last 3 seconds)
fade_in_duration = 3000  # in milliseconds (3 seconds)
fade_out_duration = 3000  # in milliseconds (3 seconds)

# Flag to control the order of processing (True for random, False for alphabetical)
random_order = True

# Target duration for the final audio file in seconds
target_duration_seconds = 14400  # 4 hours
# target_duration_seconds = None # To not limit the maximum size of the song, use None

# Ensure the destination folder exists
os.makedirs(destination_audio_folder, exist_ok=True)

# Determine the output file name based on the folder name if not provided
if output_file_name is None:
    folder_name = os.path.basename(os.path.normpath(destination_audio_folder))
    output_file_name = folder_name

# Check if the source folder exists and has .wav or .mp3 files
if not os.path.exists(source_audio_folder):
    print(f"Source folder '{source_audio_folder}' does not exist. Please create the folder and add audio files.")
    exit(1)

audio_files = [f for f in os.listdir(source_audio_folder) if f.endswith(('.wav', '.mp3'))]

if not audio_files:
    print(f"No .wav or .mp3 files found in the source folder '{source_audio_folder}'. Please add audio files.")
    exit(1)

# Apply the desired sorting method
if random_order:
    random.shuffle(audio_files)  # Randomize the list
else:
    audio_files.sort()  # Sort alphabetically

# Initialize an empty AudioSegment to hold the combined audio
combined_audio = AudioSegment.silent(duration=0)  # Start with silence

# Create a list to track start times for the TXT file
audio_start_times = []

# Convert target duration to milliseconds (if defined)
target_duration_ms = target_duration_seconds * 1000 if target_duration_seconds is not None else None

# Process each audio file
current_position = 0  # Track the current position in milliseconds
for audio_file in audio_files:
    # Load the audio file
    audio_path = os.path.join(source_audio_folder, audio_file)
    if audio_file.endswith('.wav'):
        audio = AudioSegment.from_wav(audio_path)
    elif audio_file.endswith('.mp3'):
        audio = AudioSegment.from_mp3(audio_path)

    # Apply fade in and fade out
    audio = audio.fade_in(fade_in_duration).fade_out(fade_out_duration)

    # Check if adding the current audio exceeds the target duration (if target duration is defined)
    if target_duration_ms is not None and current_position + len(audio) > target_duration_ms:
        combined_audio += audio  # Add the last audio even if it exceeds the limit
        start_time_hours = current_position // 3600000
        start_time_minutes = (current_position % 3600000) // 60000
        start_time_seconds = (current_position % 60000) // 1000
        audio_start_times.append(f"{start_time_hours:02}:{start_time_minutes:02}:{start_time_seconds:02} - {audio_file}")
        current_position += len(audio)
        break  # Stop processing further audio files

    # Append the processed audio to the combined audio
    combined_audio += audio

    # Save the start time (convert milliseconds to minutes:seconds format)
    start_time_hours = current_position // 3600000
    start_time_minutes = (current_position % 3600000) // 60000
    start_time_seconds = (current_position % 60000) // 1000
    audio_start_times.append(f"{start_time_hours:02}:{start_time_minutes:02}:{start_time_seconds:02} - {audio_file}")

    # Update the current position
    current_position += len(audio)

# Export the combined audio to a new file
output_audio_path = os.path.join(destination_audio_folder, f"{output_file_name}.{output_format}")
combined_audio.export(output_audio_path, format=output_format)

# Save the list of audio start times to a TXT file
output_txt_path = os.path.join(destination_audio_folder, f"{output_file_name}_audio_list.txt")
with open(output_txt_path, "w") as txt_file:
    txt_file.write("\n".join(audio_start_times))

print(f"Combined audio saved to: {output_audio_path}")
print(f"Audio list saved to: {output_txt_path}")
print(f"Total duration of combined audio: {current_position // 1000} seconds")