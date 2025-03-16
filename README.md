# Python Music Compiler

This project provides two scripts for compiling `.wav` and `.mp3` music files into seamless audio tracks: `simple_compiler.py` and `weighted_compiler.py`.

- **`simple_compiler.py`**: A basic script that merges all audio files from a folder into a single track with fade-in and fade-out effects.
- **`weighted_compiler.py`**: An enhanced version that ensures fair distribution of music selection using an Excel-based history to control track frequency. This is an ideal solution for small content creators who want to maintain usage records without needing a database.

## Features
### `simple_compiler.py`
- Combines multiple `.wav` and `.mp3` files into a single audio track.
- Automatically applies 3-second fade-in and fade-out effects for smooth transitions.
- Allows setting a maximum duration for the output file to manage its length.
- Generates a text file listing the track names and their start times for easy reference.

### `weighted_compiler.py`
- All features from `simple_compiler.py`, plus:
- Uses an Excel file to track usage history of tracks.
- Implements inverse probability weighting to ensure less frequently used tracks have a higher chance of being selected.
- Allows creators to maintain a simple track history without requiring a database.
- Ideal for small content creators who want fair and controlled music selection over time.
- Requires an Excel file (`usage_history.xlsx`) with the following columns:
  - `music_path`: The file path of the music track.
  - `folder_path`: The directory containing the music file.
  - `n_usage`: The number of times the track has been used.
  - `deleted_renamed`: A flag indicating whether the file was deleted or renamed.

## Getting Started
Follow these steps to get the project up and running:

### Prerequisites
- Python 3.7 or later must be installed on your system.
- The `pydub` library is required for audio processing.

## Dependencies
The following Python packages are required:
- `pydub`: For audio manipulation.
- `ffmpeg`: Required by `pydub` for audio processing. Ensure it is installed and available in your system PATH.

Install `ffmpeg` using your system's package manager. For example:
- On Ubuntu:
  ```bash
  sudo apt install ffmpeg
  ```
- On MacOS (using Homebrew):
  ```bash
  brew install ffmpeg
  ```
- On Windows, download it from [FFmpeg's official website](https://ffmpeg.org/download.html).

### Installation

1. **Clone the Repository**  
   Clone the project repository to your local machine:
   ```bash
   git clone https://github.com/biagolini/PythonMusicCompiler.git
   cd PythonMusicCompiler
   ```

2. **Create the Source Files Directory**  
   Inside the project directory, create a folder named `SourceFiles`:
   ```bash
   mkdir SourceFiles
   ```
   Place all your `.wav` and/or `.mp3` files inside this folder.

3. **Set Up a Virtual Environment**  
   Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

4. **Install Dependencies**  
   Install the required libraries using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running `simple_compiler.py`
```bash
python3 simple_compiler.py
```

The script will:
1. Process all `.wav` and `.mp3` files in the `SourceFiles` folder.
2. Apply fade-in and fade-out effects.
3. Combine the audio files into a single track.
4. Save the compiled track as `OutputFiles/combined_audio.wav`.
5. Generate a text file (`audio_list.txt`) listing the track names and their start times.

### Running `weighted_compiler.py`
```bash
python3 weighted_compiler.py
```

This script follows a more advanced approach by:
1. Reading an Excel file (`usage_history.xlsx`) to track how often each track is used.
2. Using a probability weighting method to prioritize lesser-used tracks.
3. Compiling the selected tracks into a single audio file.
4. Updating the Excel file with the new usage history after processing.

### Example

1. Place `.wav` and/or `.mp3` files in the `SourceFiles` folder:
   ```
   SourceFiles/
   ├── track1.wav
   ├── track2.mp3
   └── track3.wav
   ```

2. Run `simple_compiler.py`:
   ```bash
   python3 simple_compiler.py
   ```
   or run `weighted_compiler.py`:
   ```bash
   python3 weighted_compiler.py
   ```

3. The output will be saved as:
   ```
   OutputFiles/
   ├── combined_audio.wav
   └── audio_list.txt
   ```

   Example content of `audio_list.txt`:
   ```
   0:00 - track1.wav
   3:45 - track2.mp3
   7:15 - track3.wav
   ```

## Contributing

Feel free to submit issues, create pull requests, or fork the repository to help improve the project.

## License and Disclaimer

This project is open-source and available under the MIT License. You are free to copy, modify, and use the project as you wish. However, any responsibility for the use of the code is solely yours. Please use it at your own risk and discretion.

---

Happy creating! 🎶

