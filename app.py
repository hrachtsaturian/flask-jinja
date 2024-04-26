from flask import Flask, request, render_template
from stories import Story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "madlibs"

debug = DebugToolbarExtension(app)

@app.route('/')
def show_form():
    return render_template('form.html')

@app.route('/story')
def show_story():
    place = request.args.get('place', '')
    adjective = request.args.get('adjective', '')
    noun = request.args.get('noun', '')
    verb = request.args.get('verb', '')
    plural_noun = request.args.get('plural_noun', '')
    story_instance = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    )
    ans = {"verb": verb, "noun": noun, "place": place, "adjective": adjective, "plural_noun": plural_noun}
    story = story_instance.generate(ans)
    return render_template('story.html', story=story)