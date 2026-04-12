import sys
from fetch_transcipt import fetch_transcript
from generate_quiz import generate_quiz
from give_quiz import give_quiz




    

# def main():
#     # Check if the user actually provided the link
#     if len(sys.argv) < 2:
#         print("Error: Please provide a YouTube link.")
#         print("Usage: python3 app.py <youtube_link>")
#         sys.exit(1) # Exit the script with an error code

#     #fetch_transcript(sys.argv[1])
#     #generate_quiz(fetch_transcript(sys.argv[1]))

#     quiz_answer_key = generate_quiz(fetch_transcript(sys.argv[1]))
#     #print(quiz_answer_key.model_dump_json(indent=4))
#     give_quiz(quiz_answer_key)

    

# if __name__ == "__main__":
#     main()





from flask import Flask, redirect , url_for, render_template, request, session, flash
import requests
import redis
import json



# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

#Time to live value for redis cache
CACHE_TTL = 1800 # 30 minutes

response = r.ping()
print("my rrrrrresponse:", response)





app = Flask(__name__)
app.secret_key = "uwu"

@app.route("/", methods=["POST", "GET"])
@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        # Get the user's video link from the form
        users_video = request.form["video_url"]


        # Validate the video link by trying to fetch it
        try:
            requests.get(users_video)
        except:
            flash("The provided video link is not valid or the video is not public. Please try again.") 
            return render_template("index.html")



        session["link"] = users_video
        return redirect(url_for("quiz"))
    else:
        return render_template("index.html")
    

@app.route("/quiz", methods=["POST", "GET"])
def quiz():
    if "link" not in session:
        return redirect(url_for("home"))
    else:
        #redis
        raw_quiz = r.get(session["link"])

        if raw_quiz is None:
            response = generate_quiz(fetch_transcript(session["link"]))
            quiz = json.loads(response)

            r.set(session["link"], json.dumps(quiz))
        else:
            quiz = json.loads(raw_quiz)



        # quiz = generate_quiz(fetch_transcript(session["link"]))
        # quiz_data = session["link"]


        # Convert to a Python dictionary
        # data = json.loads(quiz)

        return render_template("quiz.html", quiz_data=quiz)

    



if __name__ == "__main__":
    app.run(debug=True)




