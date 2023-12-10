# import os untuk mengakses system database
import os

# import SQL untuk menggunakan bahasa SQL dalam python
from cs50 import SQL
# import tools untuk website
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# mengatur nama aplikasi
app = Flask(__name__)

# dipakai untuk Menghubungkan ke database
db = SQL("sqlite:///birthdays.db")


@app.route("/", methods=["GET", "POST"])
# ketika route "/" dipanggil/diakses, maka fungsi index() dieksekusi
def index():
    # jika request yg dilakukan oleh pengguna adalah post, maka eksekusi kode dalam if
    if request.method == "POST":

        # Access form data / membaca data yang diisilkan pada form
        name = request.form.get("name")# ambil data dari input name
        month = request.form.get("month")# ambil data dari imput month
        day = request.form.get("day")# ambil data dari input day

        # insert data into database, masukkan data name, month, day ke database
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

        # Go back to homepage
        return redirect("/")

    else:

        # ambil seluruh data dari tabel birthdays, simpan di variabel birthdays
        birthdays = db.execute("SELECT * FROM birthdays")    
        print(birthdays)

        # salin isi variabel birthdays ke birthdays, lalu kirim ke index.html
        return render_template("index.html", birthdays=birthdays)

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit_data(id):
  if request.method == "GET":
    bday = db.execute("SELECT * from birthdays WHERE id = ?", id)[0]
    print(bday)
    return render_template("edit.html", bday=bday)
  elif request.method == "POST":
    bday_name = request.form.get("name")
    bday_month = request.form.get("month")
    bday_day = request.form.get("day")
    db.execute('UPDATE birthdays set name = ?, month = ?, day = ? where id = ?', bday_name, bday_month, bday_day, id)
    return redirect("/")
  



