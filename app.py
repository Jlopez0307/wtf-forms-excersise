from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)
app.app_context().push()
# 
app.config['SECRET_KEY'] = 'cats'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Halo03117!@localhost:5432/pet_adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
connect_db(app)
# db.create_all()

@app.route('/')
def home_page():
    pets = Pet.query.all()
    return render_template('adoption_home.html', pets = pets)

@app.route('/add', methods =["GET", "POST"])
def add_pet():
    
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data.lower()

        photo = form.photo_url.data
        if photo == '':
            if species == 'cat':
                photo = 'https://t4.ftcdn.net/jpg/02/25/25/81/360_F_225258132_kKs9Ib4S2EbjkL8V2YqqYRNbITeOPQIz.jpg'
            elif species == 'dog':
                photo = 'https://i.pinimg.com/736x/bd/d4/0c/bdd40c190ad2e650a5f54c7548fb1fb2.jpg'
            elif species == 'porcupine':
                photo = 'https://as1.ftcdn.net/v2/jpg/02/51/00/22/1000_F_251002279_3GZcbKwv9YknaRbfNQjDaubyyWN7WuMP.jpg'
        
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name = name, species = species, photo_url = photo, age = age, notes = notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form = form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def pet_details(pet_id):
    form = EditPetForm()
    pet = Pet.query.get(pet_id)

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        if photo_url == '':
            if pet.species == 'cat':
                pet.photo_url = 'https://t4.ftcdn.net/jpg/02/25/25/81/360_F_225258132_kKs9Ib4S2EbjkL8V2YqqYRNbITeOPQIz.jpg'
            elif pet.species == 'dog':
                pet.photo_url = 'https://i.pinimg.com/736x/bd/d4/0c/bdd40c190ad2e650a5f54c7548fb1fb2.jpg'
            elif pet.species == 'porcupine':
                pet.photo_url = 'https://as1.ftcdn.net/v2/jpg/02/51/00/22/1000_F_251002279_3GZcbKwv9YknaRbfNQjDaubyyWN7WuMP.jpg'
            else:
                pet.photo_url = photo_url
        pet.notes = notes
        pet.available = available
        db.session.commit()
        return redirect(f'/{pet_id}')
    else:
        pet = Pet.query.get(pet_id)
        return render_template('pet_details.html', pet = pet, form = form)
