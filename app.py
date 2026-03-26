import json
import sys
from youtube_transcript_api import YouTubeTranscriptApi
import re

def fetch_transcript(link):
    # 1. Initialize the API
    ytt_api = YouTubeTranscriptApi()

    # 2. Fetch the transcript object
    fetched_transcript = ytt_api.fetch(extract_video_id(link))

    # 3. Convert it back to the classic list of dictionaries your script expects
    transcript = fetched_transcript.to_raw_data()
    clean_transcript = " ".join([segment['text'].replace('\n', ' ') for segment in transcript])
    print(clean_transcript)


def extract_video_id(link):
    #Safely extracts the 11-character YouTube video ID from any URL format,
    #ignoring timestamps and extra parameters.
    pattern = r'(?:v=|youtu\.be\/|embed\/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, link)
    
    if match:
        return match.group(1)
    return None
    

def save_transcript():
    print('saving transcipt perchance mmmm?')

def main():
    # Check if the user actually provided the link
    if len(sys.argv) < 2:
        print("Error: Please provide a YouTube link.")
        print("Usage: python3 app.py <youtube_link>")
        sys.exit(1) # Exit the script with an error code

    fetch_transcript(sys.argv[1])
    

if __name__ == "__main__":
    main()