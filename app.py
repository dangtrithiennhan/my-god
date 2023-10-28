from flask import Flask, render_template, url_for


import oracledb

def generate_page_list():
    pages = [
        {"name": "Site Details", "url": url_for('index')
         },
        {"name": "Environment", "url": url_for('index1')
         }
    ]
    return pages

def get_database_connection():
	dbc=oracledb.connect(
     	user="thiennhan",
     	password="KrishLinh123!",
     	dsn="kvtq93bgoyg8wtqx_low",
     	config_dir="Wallet",
     	wallet_location="Wallet",
     	wallet_password="KrishLinh123!")
	return dbc
  
app = Flask(__name__)
print('Starting..')
print('Checking database connection')
con = get_database_connection()
print('Database connected!')
@app.route('/')
def index():
    #con = get_database_connection()
    cur=con.cursor()
    posts = cur.execute('SELECT * from dual').fetchall()
    cur.close()
    pages=generate_page_list()
    return render_template('index.html', posts=posts, pages=pages)

@app.route('/index1.html')
def index1():
    #con = get_database_connection()
    cur=con.cursor()
    #classes = cur.execute('SELECT c.center_name, v.volunteer_name, a.* from god_volunteers v, god_vol_attendance a, god_centers c where a.volunteer_id = v.volunteer_id and a.center_id = c.center_id order by a.attendance_date desc').fetchall()
    classes=cur.execute('SELECT volunteer_id from god_volunteers').fetchall()
    cur.close()
    pages=generate_page_list()
    return render_template('index1.html', classes=classes, pages=pages)

@app.route("/students.html", methods=['GET'])
def students():
    con = get_database_connection()
    cur=con.cursor()
    #classes = cur.execute('SELECT v.volunteer_name, a.* from god_volunteers v, god_vol_attendance a where a.volunteer_id = v.volunteer_id order by a.attendance_date desc').fetchall()
    classes=cur.execute('SELECT volunteer_id from god_volunteers').fetchall()
    cur.close()
    return render_template('students.html', classes=classes)
