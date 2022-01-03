from flask import Flask, render_template
import requests
app = Flask(__name__)
api_url = 'https://api.npoint.io/ed99320662742443cc5b'
response = requests.get(url=api_url)
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", blogs=all_posts)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    for posts in all_posts:
        if posts["id"] == post_id:
            return render_template('post.html', title=posts["title"], subtitle=posts["subtitle"], body=posts["body"])


if __name__ == "__main__":
    app.run(debug=True)
