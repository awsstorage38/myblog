from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__, template_folder='C:\\Users\\Akshith\\Desktop\\myblog\\templates')

# Function to create a database connection
def create_connection():
    return sqlite3.connect('C:\\Users\\Akshith\\Desktop\\myblog\\Database\\myblog.db')  # Replace with your database name

# Route for login page
@app.route('/')
def login():
    return render_template('login.html')

#Route to dashboard.html
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')  # Render the dashboard template


# Route to handle login form submission
@app.route('/login', methods=['POST'])
def login_submit():
   # if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM login WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:

            # Successful login
            #return "Login successful"
           return redirect(url_for('dashboard'))  # Redirects to the 'dashboard' route
            #return render_template('dashboard.html')
        else:
            return "Failed login either user doesn't exist or wrong password used. Please try again"
            #print("Invalid credentials")
            return render_template('login.html') #, error='Invalid credentials')

'''
       # if username in user and user[username] == password:

        if user:
            # Successful login, redirect to a new page
            print("Successful login")
            return redirect(url_for('dashboard'))  # Redirects to the 'dashboard' route
        else:
            print("wrong username & pwd.. try again")

            # Failed login, show an error message or render login page again
            return render_template('login.html', error='Invalid credentials')
    else:
        # Show the login page
        return render_template('login.html')
    '''

# Function to insert data into the database
def insert_data(conn, username, password):
    insert_sql = f"INSERT INTO login (username, password) VALUES (?, ?)"
    try:
        cursor = conn.cursor()
        cursor.execute(insert_sql, (username, password))
        conn.commit()
        print("Data inserted successfully")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")


# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    
    conn = create_connection()
    if conn is not None:
       # create_table(conn)
        insert_data(conn, username, password)
        conn.close()
        return "Data inserted successfully"
    else:
        return "Error: Unable to connect to the database"

if __name__ == '__main__':
    app.run(debug=True)
