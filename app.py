from flask import Flask, render_template
import os

# All templates live in /src/…
app = Flask(__name__, template_folder="src")

# --------------------------------------------------------------------
# HOME
# --------------------------------------------------------------------
@app.route("/")
def home():
    return render_template("home.html")

# --------------------------------------------------------------------
# BLOODY‑ORANGE MARTINI  (already working)
# --------------------------------------------------------------------
@app.route("/bloody-orange-martini")
def bloody_orange_martini():
    return render_template("bloody_orange_martini/bloody_orange_martini.html")

@app.route("/bloody-orange-martini/2")
def bloody_orange_martini_2():
    return render_template("bloody_orange_martini/bloody_orange_martini_2.html")

@app.route("/bloody-orange-martini/3")
def bloody_orange_martini_3():
    return render_template("bloody_orange_martini/bloody_orange_martini_3.html")

@app.route("/bloody-orange-martini/4")
def bloody_orange_martini_4():
    return render_template("bloody_orange_martini/bloody_orange_martini_4.html")

@app.route("/bloody-orange-martini/5")
def bloody_orange_martini_5():
    return render_template("bloody_orange_martini/bloody_orange_martini_5.html")

# --------------------------------------------------------------------
# GRAPEFRUIT PALOMA  (NEW 5‑step flow)
# --------------------------------------------------------------------
@app.route("/grapefruit-paloma")
def grapefruit_paloma():
    return render_template("grapefruit_paloma/grapefruit_paloma.html")

@app.route("/grapefruit-paloma/2")
def grapefruit_paloma_2():
    return render_template("grapefruit_paloma/grapefruit_paloma_2.html")

@app.route("/grapefruit-paloma/3")
def grapefruit_paloma_3():
    return render_template("grapefruit_paloma/grapefruit_paloma_3.html")

@app.route("/grapefruit-paloma/4")
def grapefruit_paloma_4():
    return render_template("grapefruit_paloma/grapefruit_paloma_4.html")

@app.route("/grapefruit-paloma/5")
def grapefruit_paloma_5():
    return render_template("grapefruit_paloma/grapefruit_paloma_5.html")

# --------------------------------------------------------------------
# TEQUILA SUNRISE  (still one page + quiz for now)
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# TEQUILA SUNRISE  (NEW 5‑step flow)
# --------------------------------------------------------------------
@app.route("/tequila-sunrise")
def tequila_sunrise():
    return render_template("tequila_sunrise/tequila_sunrise.html")

@app.route("/tequila-sunrise/2")
def tequila_sunrise_2():
    return render_template("tequila_sunrise/tequila_sunrise_2.html")

@app.route("/tequila-sunrise/3")
def tequila_sunrise_3():
    return render_template("tequila_sunrise/tequila_sunrise_3.html")

@app.route("/tequila-sunrise/4")
def tequila_sunrise_4():
    return render_template("tequila_sunrise/tequila_sunrise_4.html")

@app.route("/tequila-sunrise/5")
def tequila_sunrise_5():
    return render_template("tequila_sunrise/tequila_sunrise_5.html")

# --------------------------------------------------------------------
# QUIZZES   (no leading “/” inside render_template!)
# --------------------------------------------------------------------
@app.route("/bloody-orange-martini-quiz")
def bloody_orange_martini_quiz():
    return render_template("bloody_orange_martini/bloody_orange_martini_quiz.html")

@app.route("/tequila-sunrise-quiz")
def tequila_sunrise_quiz():
    return render_template("tequila_sunrise/tequila_sunrise_quiz.html")

@app.route("/grapefruit-paloma-quiz")
def grapefruit_paloma_quiz():
    return render_template("grapefruit_paloma/grapefruit_paloma_quiz.html")


# --------------------------------------------------------------------
# QUIZ MENU
# --------------------------------------------------------------------
@app.route("/quiz")
def quiz_menu():
    return render_template("quiz_menu.html")

# --------------------------------------------------------------------
# RECIPE BOOK
# --------------------------------------------------------------------
@app.route("/recipes")
def recipe_book():
    return render_template("recipe_book.html")


# --------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
