import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donor, Donation

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY').encode()


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
        try:
            donor = Donor.select().where(Donor.name == request.form['name']).get()
        except Donor.DoesNotExist:
            donor = Donor(name=request.form['name'])
            donor.save()

        donation = request.form['donation']
        new_donation = Donation(value=donation, donor=donor)
        new_donation.save()
        return redirect(url_for('home'))

    return render_template('newdonation.jinja2')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

