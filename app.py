
from flask import Flask, request, render_template, redirect, flash
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = 'whysosecret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

MOVIES = {'Amadeus', 'Chicken Run', 'Dances with Wolves'}


@app.route('/')
def home_page():
    ''' Show home page '''
    # html = '''
    # <html>
    #     <body>
    #         <h1> Home Page </h1>
    #         <p> Welcome to flask app V1 </p>
    #         <a href='/hello'> Go to Hello Page </a>
    #     </body>
    # </html>
   # '''
    return render_template('home.html')

@app.route('/old-home-page')
def redirect_home():
    ''' redirect to new home page '''
    flash('That page has moved. This is our new page')
    return redirect('/')

@app.route('/movies')
def show_all_movies():
    '''Show list of all movies '''
    return render_template('movies.html', movies=MOVIES)

@app.route('/movies/new', methods=["POST"])
def add_movie():
    title = request.form['title']
    # Add to pretend DB
    if title in MOVIES:
        flash("movie already exists", 'error')
    else:
        MOVIES.add(title)
        flash("Created your movie", 'success')
    # MOVIES.add(title)
    # return render_template('movies.html', movies=MOVIES)
    # flash('You got flashed')
    return redirect('/movies')


@app.route('/form')
def show_form():
    return render_template('form.html')

@app.route('/form-2')
def show_form_2():
    return render_template('form_2.html')

COMPLIMENTS = [ 'cool', 'clever', 'tenacious', 'awesome', 'pythonic' ]

@app.route('/greet')
def get_greeting():
    username = request.args['username']
    nice_thing = choice(COMPLIMENTS)
    return render_template('greet.html', username=username, compliment=nice_thing )

@app.route('/greet-2')
def get_greeting_2():
    username = request.args['username']
    wants = request.args.get('wants_compliments')
    nice_things = sample(COMPLIMENTS,3)
    return render_template('greet_2.html', username=username, wants_compliments=wants, compliments=nice_things)


@app.route('/lucky')
def luck_number():
    num = randint(1,10)
    return render_template('lucky.html', lucky_num=num, msg='You are lucky!')

@app.route('/spell/<word>')
def spell_word(word):
    caps_word = word.upper()
    return render_template('spell_word.html', word=caps_word)

@app.route('/hello')
def say_hello():
    # html = """
    # <html>
    #     <body>
    #         <h1>Hello!</h1>
    #         <p>This is page hello</p>
    #     </body>
    # </html>
    # """
    # return html
    # return 'Hello there'

    ''' Shows hello page '''
    return render_template('hello.html')

@app.route('/goodbye')
def say_bye():
    return 'Good bye' 
    
@app.route('/search')
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1> Search Results for: {term} <p> Sorting by: {sort} </p>"

# @app.route('/post', methods=["POST"])
# def post_demo():
#     return 'post posted yo'
    
# @app.route('/post', methods=["GET"])
# def get_demo():
#     return 'get gotted yo'

@app.route('/add-comment')
def add_comment_form():
    return """
    <form method='POST'>
    <h1> Add comment </h1>
    <input type='text' placeholder='comment' name='comment'/>
    <input type='text' placeholder='username' name='username'/>
    <button>Submit</button>
    </form>
    """

@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment = request.form['comment']
    username = request.form['username']
    # print(request.form)
    return f"""
    <h1> Saved Your Comment</h1>
    <ul>
        <li> Username: {username}</li>
        <li> Comment: {comment}</li>
    </ul>
    """

@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f"<h1>Browsing the {subreddit} Subreddit</h1>"

@app.route('/r/<subreddit>/comments/<int:post_id>')
def show_comments(subreddit, post_id):
    return f"<h1>Viewing Comments for post with id: {post_id} from the {subreddit} Subreddit</h1>"

POSTS = {
    1: " I like Chicken Tenders ",
    2: "I hate mayo",
    3: " double rainbow yay",
    4: "yolo omg (kill me)"
}

@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS[id]
    return f"<p> {post}</p>"

#  http://toys.com/shop/spinning-top?color=red
#  /shop/<product>/<color>

# /r/askreddit/search/?q=chickens&restrict_sr=1
# /r/<subreddit>/search