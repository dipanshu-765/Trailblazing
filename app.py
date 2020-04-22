from flask import Flask, render_template, request, session, make_response, redirect, url_for
from Models.Blog import Blog
from Models.User import User
from Models.Post import Post
from Database.Database import Database
app = Flask(__name__)
app.secret_key = "fml"


@app.before_first_request
def initialize_database():
    Database.initialize()
    session['email'] = None


@app.route('/')
def home_template():
    if session['email'] is None:
        return render_template('Home.html')
    else:
        email = session['email']
        user = User.get_by_email(email)
        name = user.name
        return render_template('Profile.html', name=name)


@app.route('/login')
def login_template():
    return render_template('Login.html')


@app.route('/register')
def register_template():
    return render_template('Register.html')


@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']
    if User.login_valid(email=email, password=password):
        User.login(email=email)
        user = User.get_by_email(email)
        username = user.name
        return render_template('Profile2.html', name=username)
    else:
        session['email'] = None
        return render_template('Login.html')


@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']
    name = request.form['name']
    User.register(name=name, password=password, email=email)
    return render_template('Profile.html', email=email)


@app.route('/logout')
def logout():
    session['email'] = None
    return redirect(url_for('home_template'))


@app.route('/blogs/<string:user_id>')
@app.route('/blogs')
def get_user_blogs(user_id=None):
    if user_id is not None:
        temp_user = User.get_by_id(user_id)
        blogs = Blog.get_by_user_id(user_id)
        user_email = session['email']
        user = User.get_by_email(user_email)
        name = user.name
        name2 = temp_user.name
        email = temp_user.email+"'s"
        is_user = False
    else:
        temp_user = User.get_by_email(email=session['email'])                       #Nasty error if no session
        blogs = temp_user.get_blogs()
        email = 'Your'
        name = temp_user.name
        name2 = name
        is_user = True
    return render_template('User_Blogs.html', blogs=blogs, email=email, is_user=is_user, name=name, name2=name2)


@app.route('/posts/<string:blog_name>')
def get_posts(blog_name=None):
    email = session['email']
    user = User.get_by_email(email)
    name = user.name
    user_id = user.get_id()
    blog = Database.find_one(collection='Blogs', query={'username': blog_name})
    blog_id = blog['_id']
    author_id = blog['user_id']
    posts = Post.get_by_blog_id(_id=blog_id)
    return render_template('Blog_Posts.html', posts=posts, blog_title=blog['username'], blog_id=blog_id,
                           author_id=author_id, user_id=user_id, name=name)


@app.route('/blogs/new', methods=['POST', 'GET'])
def create_new_blog():
    #Do something for case in which Blog Name already exists
    if request.method == 'GET':
        return render_template('Create_Blog.html')
    else:
        email = session['email']
        temp_user = User.get_by_email(email)
        description = request.form['description']
        username = request.form['blog_name']
        temp_user.create_blog(username=username, description=description)
        return redirect(url_for('get_user_blogs'))


@app.route('/posts/new/<string:blog_id>', methods=['POST', 'GET'])
def create_new_post(blog_id):
    if request.method == 'GET':
        return render_template('Create_Post.html', blog_id=blog_id)
    else:
        title = request.form['title']
        content = request.form['content']
        blog = Blog.get_by_id(blog_id)
        username = blog.username
        blog.new_post(title=title, content=content)
        return redirect(url_for('get_posts', blog_name=username))


@app.route('/search')
def search():
    email = session['email']
    username = User.get_by_email(email).name
    query = request.args.get('search')
    blogs = Database.find_all('Blogs')
    blog_res = []
    for blog in blogs:
        if query in blog['username']:
            blog_res.append(blog)
    posts = Database.find_all(collection='posts')
    post_res = []
    for post in posts:
        if query in post['title']:
            post_res.append(post)
    return render_template('Search.html', name=username, blogs=blog_res, posts=post_res)


@app.route('/posts/blogs/new')
def redirect1():
    return redirect(url_for('create_new_blog'))


@app.route('/auth/search')
def redirect2():
    return redirect(url_for('search'))


if __name__ == '__main__':
    app.run(port=4990, debug=True)


