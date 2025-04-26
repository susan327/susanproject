from flask import Flask, render_template

app = Flask(__name__)

# トップページ
@app.route("/")
def index():
    return render_template("index.html")

# 各サービスページ
@app.route("/hp-renew")
def hp_renew():
    return render_template("hp_renew.html")

@app.route("/simple-hp")
def simple_hp():
    return render_template("simple_hp.html")

@app.route("/ai-summary")
def ai_summary():
    return render_template("ai_summary.html")

@app.route("/form-auto")
def form_auto():
    return render_template("form_auto.html")

@app.route("/hp-transfer")
def hp_transfer():
    return render_template("hp_transfer.html")

@app.route("/logo-create")
def logo_create():
    return render_template("logo_create.html")

@app.route("/mini-app")
def mini_app():
    return render_template("mini_app.html")


# アプリ起動設定
if __name__ == "__main__":
    app.run(debug=True)
