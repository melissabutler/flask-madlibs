from flask import Flask, request, render_template

from flask_debugtoolbar import DebugToolbarExtension

from stories import story

app = Flask(__name__)

print('hello')

app.debug = True

app.config['SECRET_KEY'] = 'catbutts'

toolbar =  DebugToolbarExtension(app)

@app.route('/')
def root_page():
    """Shows home page"""
    prompts = story.prompts
    return render_template("root.html", prompts=prompts)

@app.route('/story')
def story_page():
    """Shows finished story after input"""
    text = story.generate(request.args)
    return render_template("story.html", text=text)