import sys
from fetch_transcipt import fetch_transcript
from generate_quiz import generate_quiz
from give_quiz import give_quiz




    

def main():
    # Check if the user actually provided the link
    if len(sys.argv) < 2:
        print("Error: Please provide a YouTube link.")
        print("Usage: python3 app.py <youtube_link>")
        sys.exit(1) # Exit the script with an error code

    #fetch_transcript(sys.argv[1])
    #generate_quiz(fetch_transcript(sys.argv[1]))

    give_quiz(generate_quiz(fetch_transcript(sys.argv[1])))

    

if __name__ == "__main__":
    main()
