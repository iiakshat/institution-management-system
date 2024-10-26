from flask import Flask, render_template, request

app = Flask(__name__)

db = {
    "Resource" : {
        "subject" : ["Maths", "Physics", "Chemistry", "Biology", "English"],
        "summary" : "Lecture Summary for maths...",
        "notes_url" : "https://www.google.com", 
        "likes" : 4,
        "views" : 10,
        "chose" : "Maths"
    },

    "ResourceLLM" : {
        "subject" : ["Maths", "Physics", "Chemistry", "Biology", "English"],
        "summary" : """Brief Communication (BriffComm) is an AI-powered tool that generates summaries of audio and video content in various languages. The model used by students and faculty at Parol University is beneficial for podcast and news channels, as it eliminates the need for manual transcription and produces more accurate summaries.

                        Key Points:

                        1. BriffComm is an AI-powered tool that generates summaries of audio and video content in various languages.
                        2. The model used by students and faculty at Parol University is beneficial for podcast and news channels, as it eliminates the need for manual transcription and produces more accurate summaries.
                        3. The project was made by Kanika Dogra and Rakshat, who are students at Parol University.

                        Decisions Made:

                        1. The use of BriffComm can improve the accuracy and efficiency of news and podcast content creation.
                        2. The tool can be used for various languages and mediums, including audio and video.
                        3. The model used by students and faculty at Parol University is beneficial for podcast and news channels.

                        Action Items:

                        1. Implement BriffComm in news and podcast content creation to improve accuracy and efficiency.
                        2. Use the tool for various languages and mediums, including audio and video.
                        3. Explore the use of BriffComm for faculty and student projects at Parol University.

                        Follow-Up Items:

                        1. Evaluate the performance of BriffComm in different languages and mediums.
                        2. Investigate the potential applications of BriffComm in various industries.
                        3. Consider implementing BriffComm in other universities and organizations.

                        Places Mentioned:

                        1. Parul University - A university where the project was developed and implemented.
                        2. Vadodara - A city in Gujarat, India, where the project was developed.""",
        "notes_url" : "https://www.google.com", 
        "likes" : 4,
        "views" : 10,
        "chose" : "Audio"
    },

    "user" : {
        "name" : "Akshat Sanghvi",
        "id" : "210303105522"
    }
}
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/dashboard', ["GET", "POST"])
def dashboard():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('dashboard.html', Resource=db["Resource"])
    
        file = request.files['file']
        return render_template('dashboard.html', Resource=db["ResourceLLM"])
    return render_template('dashboard.html', Resource=db["Resource"])

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/fees')
def fees():
    return render_template('fees.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
