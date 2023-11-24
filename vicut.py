#
#script to cut video for whatsapp status
#@jdP

import subprocess
import datetime
import sys

# python3 vicut.py input_file output_file
if len(sys.argv) < 3:
    print("Please provide video location and out put file name")
    sys.exit()

video_loc = sys.argv[1]
output_file_name = sys.argv[2]

vid_cut_dur = 30 # in seconds

output = subprocess.check_output(f"ffprobe -v error -select_streams \
                                 v:0 -show_entries stream=duration \
                                 -of default=noprint_wrappers=1:nokey=1 \
                                 {str(video_loc)}", shell=True)
total_secs = int(float(output))
posible_cut = total_secs / vid_cut_dur
full_cut = int(posible_cut)
odd_cut = posible_cut > full_cut

total_cut = full_cut + 1 if odd_cut else full_cut
for c in range(total_cut):
    seconds = c * vid_cut_dur
    start_time = str(datetime.timedelta(seconds=seconds))
    cut_dur = str(datetime.timedelta(seconds=vid_cut_dur))
    output_file = f"{output_file_name}{c}.mp4"
    subprocess.run(['ffmpeg', 
                    '-ss', 
                    str(start_time),
                    '-accurate_seek',
                    '-i',
                    str(video_loc),
                    '-t',
                    str(vid_cut_dur),
                    '-c:v',
                    'libx264',
                    '-c:a',
                    'aac',
                    str(output_file)])

print("\n\nVideo cutting complete")