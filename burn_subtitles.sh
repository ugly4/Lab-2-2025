#!/bin/sh
ffmpeg -y -i "$1" -vf "subtitles=$2:force_style='Fontsize=16,PrimaryColour=&Hffffff&,BackColour=&H80000000&,OutlineColour=&H000000&,BorderStyle=4'" -c:a copy "$3"