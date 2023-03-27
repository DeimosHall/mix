#!/bin/python3

import os
import sys

if len(sys.argv) != 3:
    print("Two input arguments are required: the video file and the audio file.")
    sys.exit(1)

video_file = sys.argv[1]
audio_file = sys.argv[2]

video_name, video_ext = os.path.splitext(video_file)

output_file = f"{video_name}.mp4"

# Define the ffmpeg command to join the video and audio and output to the specified file
ffmpeg_cmd = f"ffmpeg -i '{video_file}' -i '{audio_file}' -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -strict experimental '{output_file}'"

exit_code = os.system(ffmpeg_cmd)

# Check if the ffmpeg command was executed successfully
if exit_code != 0:
    print("An error occurred while executing the ffmpeg command.")
    sys.exit(1)

print(f"Video and audio have been successfully joined and saved to {output_file}.")

delete_files = input("Do you want to delete the original video and audio files? (y/n): ")

if delete_files.lower() == "y":
    os.remove(video_file)
    os.remove(audio_file)

    print("The original video and audio files have been successfully deleted.")
