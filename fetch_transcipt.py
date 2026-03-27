from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from urllib.parse import urlparse, parse_qs

def fetch_transcript(url):
    # Initialize the API
    ytt_api = YouTubeTranscriptApi()
    
    # Extract the video ID from the provided link and fetch the transcript
    raw_transcript = ytt_api.fetch(extract_video_id(url))


    # Format the transcript into plain text and clean it up by removing newlines
    text_formatter = TextFormatter()
    clean_transcript = text_formatter.format_transcript(raw_transcript)
    clean_transcript = clean_transcript.replace('\n', ' ')
    
    #print(clean_transcript)
    return clean_transcript


def extract_video_id(url):
    parsed_url = urlparse(url)
    return parse_qs(parsed_url.query).get('v', [None])[0]