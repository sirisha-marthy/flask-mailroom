import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donor, Donation

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/newdonation', methods=["GET", "POST"])
def new_donation():
    if request.method == "POST":
        #user = User.select().where(User.name == request.form['name']).get()
        donor = Donor.select().where(Donor.name == request.form['name']).get()
        print("donor is {}".format(donor))
        donation = request.form['donation']
        donation = Donation(value=donation, donor=donor)
        donation.save()
        return redirect(url_for('all'))
    else:
        return render_template('newdonation.jinja2')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

