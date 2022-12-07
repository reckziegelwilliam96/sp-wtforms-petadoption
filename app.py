from flask import Flask, render_template, redirect, url_for
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = 'secret-adopt-key'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_pets_homepage():
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding"""
    pet = Pet()
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        pet = Pet(
            name=name, 
            species=species, 
            photo_url=photo_url,
            age=age,
            notes=notes,
            available=available
            )
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    
    else:
        return render_template(
            "add-pet-form.html", form=form
        )

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_pet_details(pet_id):
    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)
    return render_template(
        "pet-details.html", pet=pet, form=form
        )

def update_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(url_for('list_pets_homepage'))
    
    else:
        return render_template(
            "home.html", form=form
        )