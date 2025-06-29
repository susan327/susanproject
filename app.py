from flask import Flask, render_template

app = Flask(__name__)

# トップページ
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")

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

@app.route("/services/ai-support")
def ai_support():
    return render_template("ai_support.html")

@app.route("/vision")
def vision():
    return render_template("vision.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")







# アプリ起動設定（ローカル用）
if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
