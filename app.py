"""Flask app for Cupcakes"""
from flask import Flask, jsonify, request, render_template, url_for, redirect

from models import connect_db, db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'passwordistaco123'

with app.app_context():
    connect_db(app)
    db.create_all()

# ------------------- #
# Routes for Cupcake  #
# ------------------- #
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/list')
def list_cupcakes():
    all_cupcakes = Cupcake.query.all()
    return render_template('list.html', cupcakes=all_cupcakes)


# ------------------------- #
# API Endpoints for Cupcake #
# ------------------------- #
@app.route('/api/cupcakes')
def get_all():
    """ List all Cupcakes"""

    # serialize the todos with list comprehension
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes = all_cupcakes)

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    "Create a New Cupcake"

    new_cc = Cupcake(flavor=request.json['flavor'], size=request.json['size'], rating=request.json['rating'], image=request.json['image'])
    db.session.add(new_cc)
    db.session.commit()

    return jsonify(cupcake=new_cc.serialize()), 201

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['GET'])
def get_cupcake(cupcake_id):
    """ List a Cupcake based on ID"""

    # Flask SQL Method
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    """ Update a Cupcake based on ID"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    # Manually Update the Cupcake object 
    #  Precondition: Expect a JSON Payload
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()
    return jsonify(cupcake=cupcake.serialize()), 200

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    """ Delete a Cupcake from the DB """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Cupcake Deleted"), 200




