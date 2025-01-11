# Python Music Compiler

This project is a simple yet powerful tool for compiling `.wav` and `.mp3` music files into a single track, designed to help creators produce seamless background music for YouTube videos. By automatically applying fade-in and fade-out effects, this project creates a polished audio track ready for use.

## Features
- Combine multiple `.wav` and `.mp3` files into a single audio track.
- Automatically applies 3-second fade-in and fade-out effects for smooth transitions.
- Allows setting a maximum duration for the output file to manage its length.
- Generates a text file listing the track names and their start times for easy reference or inclusion in video descriptions.
- Exports the final audio as `combined_audio.wav`.

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

### Usage

Run the project with the following command:
```bash
python3 main.py
```

The script will:
1. Process all `.wav` and `.mp3` files in the `SourceFiles` folder.
2. Apply fade-in and fade-out effects.
3. Combine the audio files into a single track.
4. Save the compiled track as `OutputFiles/combined_audio.wav`.
5. Generate a text file (`audio_list.txt`) listing the names of the tracks and their start times in the format `minutes:seconds - filename`.

### Notes
- The `audio_list.txt` file can be used to easily create video descriptions for YouTube, listing the music tracks and their starting times.
- If you wish to ensure all tracks are included regardless of their combined duration, set the `target_duration_seconds` parameter to `None` in the script.

### Example

1. Place `.wav` and/or `.mp3` files in the `SourceFiles` folder:
   ```
   SourceFiles/
   ├── track1.wav
   ├── track2.mp3
   └── track3.wav
   ```

2. Run the script:
   ```bash
   python3 main.py
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

