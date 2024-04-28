from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_pymongo import PyMongo
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kyalokimeu0@gmail.com'
app.config['MAIL_PASSWORD'] = 'Alcatraz12!'
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"  # Replace with your MongoDB URI

mongo_client = MongoClient('mongodb+srv://root_brian:ASdh25NQFaFfqE65@clusterfoodhackathon.y7ojbmg.mongodb.net/?retryWrites=true&w=majority&appName=ClusterFoodHackathon')

db = mongo_client.get_database('food_donation_db')  # Specify the name of your database

users_collection = db['users']  """Specify the name of the collection"""

mail = Mail(app)


@app.route('/')
def index():
    return 'Welcome to the Food Donation Platform!'


@app.route('/signup')
def sign_up():
    return render_template('sign_up.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')


@app.route('/donor_dashboard')
def donor_dahsboard():
    return render_template('donor_dashboard.hmtl')


@app.route('/recipient_dashboard')
def recipient_dashboard():
    return render_template('recipient_dashboard.html')


"""Authentication and Authorization Endpoints"""


@app.route('/api/auth/register', methods=['POST'])
def register():
    """Get registration data from request body"""
    data = request.json

    """ Check if required fields are present in the request"""
    required_fields = ['username', 'password', 'email']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    """ Check if username or email already exists in the database"""
    existing_user = users_collection.find_one({'$or': [{'username': data['username']}, {'email': data['email']}]})
    if existing_user:
        return jsonify({'error': 'Username or email already exists'}), 409

    """ Create new user document"""
    new_user = {
        'username': data['username'],
        'password': data['password'],  # In practice, hash the password before storing it
        'email': data['email'],
        'role': 'donor',  # Assuming new users are registered as donors by default
        'profile': {},  # Additional profile information can be added here
        'history': []  # Initialize empty history
    }

    """ Insert new user document into the database"""
    users_collection.insert_one(new_user)

    """ Send email to the registered user """
    msg = Message('Welcome to Food Donation Platform', recipients=[data['email']])
    msg.body = 'Thank you for registering with Food Donation Platform!'
    mail.send(msg)

    return jsonify({'message': 'User registered successfully'}), 201


@app.route('/api/auth/login', methods=['POST'])
def login():
    """ Implement user login logic"""
    data = request.json

    """ Check if required fields are present in the request"""
    required_fields = ['username', 'password']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    """ Check if user with given username exists in the database"""
    user = users_collection.find_one({'username': data['username']})
    if user:
        """ Check if password matches the stored password"""
        if user['password'] == data['password']:  # In practice, compare hashed passwords
            """ Return success message and user data"""
            response_data = {
                'message': 'User login successful',
                'user': {
                    'id': str(user['_id']),
                    'username': user['username'],
                    'email': user['email'],
                    'role': user['role']
                }
            }
            return jsonify(response_data), 200
        else:
            return jsonify({'error': 'Incorrect password'}), 401
    else:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'message': 'User login endpoint'})


@app.route('/api/auth/logout', methods=['POST'])
def logout():
    """ Implement user logout logic"""
    return jsonify({'message': 'User logout endpoint'})


""" Current User Profile Endpoint"""


@app.route('/api/auth/me', methods=['GET'])
def me():
    """ Implement current user profile fetching logic"""
    """ Get the authentication token from the request headers"""
    token = request.headers.get('Authorization')

    """ Authenticate the user using the token"""
    user = authenticate(token)

    if user:
        """ Return the user's profile information if authenticated"""
        return jsonify(user)
    else:
        """ Return an error message if authentication fails"""
        return jsonify({'error': 'Authentication failed'}), 401
    return jsonify({'message': 'Current user profile endpoint'})


""" Donors Endpoints"""


@app.route('/api/donors', methods=['GET'])
def get_donors():
    """ Implement fetching all donors logic"""
    return jsonify({'message': 'Get all donors endpoint'})


@app.route('/api/donors/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def donor(id):
    """ Implement logic for specific donor profile (GET, PUT, DELETE)"""
    return jsonify({'message': f'Donor {id} endpoint'})


@app.route('/api/donors/<int:id>/donations', methods=['GET'])
def get_donations_by_donor(id):
    """ Implement fetching donations by a specific donor logic"""
    return jsonify({'message': f'Donations by donor {id} endpoint'})


@app.route('/api/donations', methods=['POST'])
def create_donation():
    """ Implement logic for creating a new donation listing"""
    return jsonify({'message': 'Create donation endpoint'})


@app.route('/api/donations/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def donation(id):
    """ Implement logic for specific donation listing (GET, PUT, DELETE)"""
    return jsonify({'message': f'Donation {id} endpoint'})


""" Recipients Endpoints"""
""" Implement recipient endpoints similarly to donors endpoints"""

""" Admins Endpoints"""
""" Implement admin endpoints similarly to donors endpoints"""

""" Communication Endpoints"""
""" Implement communication endpoints similarly to donors endpoints"""

"""Additional Endpoints"""


@app.route('/api/search', methods=['GET'])
def search():
    """ Implement search for donation listings based on various criteria"""
    return jsonify({'message': 'Search donation listings endpoint'})


@app.route('/api/history', methods=['GET'])
def history():
    """ Implement fetch donation history for donors and recipients"""
    return jsonify({'message': 'Fetch donation history endpoint'})


if __name__ == '__main__':
    app.run(debug=True)
