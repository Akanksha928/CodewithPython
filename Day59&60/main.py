from flask import Flask, render_template, request
import requests
import smtplib
my_email = "testforcode12@gmail.com"
email_password = "testforcode12@#"
app = Flask(__name__)
response = requests.get("https://api.npoint.io/0cc3f75992a274dd6dbf")
posts = response.json()


@app.route('/')
def get_all_posts():
    return render_template("index.html", data=posts)


@app.route('/about')
def get_about_page():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def get_contact_page():
    data = request.form
    if request.method == 'POST':
        name = data["name"]
        email = data["email"]
        number = data["number"]
        message = data["message"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=email_password)
            connection.sendmail(from_addr=my_email, to_addrs="akanksha.xo@gmail.com",
                                msg=f"Subject: Somebody sent you a message. \n\nName: {name} \nEmail: {email} \nPhone Number: {number}\nMessage: {message}" )
        return render_template("contact.html", message_sent=True)
    else:
        return render_template("contact.html", message_sent=False)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    for blog in posts:
        if blog["id"] == post_id:
            return render_template('post.html', title=blog["title"], subtitle=blog["subtitle"], body=blog["body"], url=blog["image_url"], publish_date=blog["date"])

#
# @app.route("/form-entry")
# def receive_data():
#     return f"Successfully sent message!"


if __name__ == "__main__":
    app.run(debug=True)
