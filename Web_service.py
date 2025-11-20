from flask import Flask, render_template, request, redirect, session, url_for, flash 

import os 

from dotenv import load_dotenv 

 

load_dotenv() 

 

app = Flask(__name__) 

app.secret_key = os.getenv("SECRET_KEY") 

 

mesajlar = [] 

SECRET_MESSAGE = os.getenv("SECRET_MESSAGE", "Gizli mesaj yok.") 

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "ders1234")   

 

@app.route("/", methods=["GET", "POST"]) 

def index(): 

    if request.method == "POST": 

        isim = request.form.get("isim") 

        mesaj = request.form.get("mesaj") 

        if isim and mesaj: 

            mesajlar.append({"isim": isim, "mesaj": mesaj}) 

        return redirect(url_for("index")) 

 

    # sadece yetkili görsün: 

    show_secret = session.get("admin", False) 

    return render_template("index.html", mesajlar=mesajlar, secret_message=SECRET_MESSAGE if show_secret else None, is_admin=show_secret) 

 

@app.route("/login", methods=["GET", "POST"]) 

def login(): 

    if request.method == "POST": 

        pwd = request.form.get("password") 

        if pwd and pwd == ADMIN_PASSWORD: 

            session["admin"] = True 

            flash("Başarıyla giriş yapıldı.", "success") 

            return redirect(url_for("index")) 

        else: 

            flash("Hatalı parola.", "danger") 

            return redirect(url_for("login")) 

    return render_template("login.html") 

 

@app.route("/logout") 

def logout(): 

    session.pop("admin", None) 

    flash("Çıkış yapıldı.", "info") 

    return redirect(url_for("index")) 

 

if __name__ == "__main__": 

    app.run(host="0.0.0.0", port=5000) 
