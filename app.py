from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def input_get():
    return render_template("login.html")

@app.route("/", methods=["POST"])
def login_post():
    user = request.form['user_name']
    return render_template("mypage.html", user=user)

@app.route("/guest", methods=["POST"])
def guest_login():
    return render_template("guest.html")

if __name__ == "__main__":
    app.run(port=4000, debug=True)
