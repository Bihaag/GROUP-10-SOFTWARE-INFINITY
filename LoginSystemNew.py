from flask import Flask, request, render_template, redirect, url_for, request, make_response
from flask_sqlalchemy import SQLAlchemy
import os
import sqlite3

currentlocation = os.path.dirname(os.path.abspath(__file__))

##CREATING TABLE(USERS) IN DB
'''import sqlite3
conn = sqlite3.connect('Login.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE users (User_ID INTEGER PRIMARY KEY, Name TEXT, Surname TEXT, Email TEXT, Password TEXT,  User_Type TEXT)')
conn.commit()
conn.close()'''

##CREATING TABLE(JOBS) IN DB
"""import sqlite3
conn = sqlite3.connect('Login.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE jobs (JobId INTEGER PRIMARY KEY, Job_Title TEXT, Job_Description TEXT, Faculty TEXT)')
conn.commit()
conn.close()
"""

##CREATING TABLE(APPLIED JOBS) IN DB
"""import sqlite3
conn = sqlite3.connect('Login.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE appliedjobs (
                AppJob_ID INTEGER PRIMARY KEY,
                User_ID INTEGER,
                JobID INTEGER,
                CV BLOB,
                FOREIGN KEY(User_ID) REFERENCES users(User_ID),
                FOREIGN KEY(JobID) REFERENCES jobs(JobID)
            )''')
conn.commit()
conn.close()"""

##INSERT INTO TABLE (USERS)
"""'''sqlconnection = sqlite3.Connection(currentlocation + "\Login.db")'''
sqlconnection = sqlite3.connect('Login.db')
cursor = sqlconnection.cursor()
'''query1 = "INSERT INTO users (name, password, email, usertype) VALUES(?,?,?)",("Vaish", "123", "vaish@gmail.com", "admin")
cursor.execute(query1)'''
cursor.execute("INSERT INTO users (username, password, email, usertype) VALUES(?,?,?,?)",('Vaish', '123', 'vaish@gmail.com', 'Admin'))
sqlconnection.commit()
sqlconnection.close()"""

##INSERT INTO TABLE (JOBS)
"""sqlconnection = sqlite3.connect('Login.db')
cursor = sqlconnection.cursor()
cursor.execute("INSERT INTO jobs (Job_Title, Job_Description, Faculty) VALUES(?,?,?)",('Data Analyst', 'You will be required to analyse data', 'IT'))
sqlconnection.commit()
sqlconnection.close()"""

##UPDATE TITLE OF JOB IN TABLE(JOBS)
'''sqlconnection = sqlite3.connect('Login.db')
cursor = sqlconnection.cursor()
x = 'C#Developer'
cursor.execute("UPDATE jobs SET Job_Title=? WHERE JobId= 1", (x,))
sqlconnection.commit()
sqlconnection.close()'''

##DELETE SPECIFIC RECORDS
'''sqlconnection = sqlite3.connect('Login.db')
cursor = sqlconnection.cursor()
cursor.execute("DELETE FROM jobs WHERE Job_Title = 'Data Analyst'")
sqlconnection.commit()
sqlconnection.close()'''

##DELETE SPECIFIC RECORDS
'''sqlconnection = sqlite3.connect('Login.db')
cursor = sqlconnection.cursor()
cursor.execute("DELETE FROM users WHERE username = 'Vaish'")
sqlconnection.commit()
sqlconnection.close()'''

##DELETE ALL RECORDS
'''import sqlite3
# Connect to the database
conn = sqlite3.connect('Login.db')
c = conn.cursor()
# Execute the delete command
c.execute('DELETE FROM jobs')
# Commit the changes
conn.commit()
# Close the connection
conn.close()'''

##DELETE ALL RECORDS (APPLIEDJOBS)
'''import sqlite3
conn = sqlite3.connect('Login.db')
c = conn.cursor()
c.execute('DELETE FROM appliedjobs')
conn.commit()
conn.close()'''

##DROP TABLE(USERS)
'''import sqlite3
conn = sqlite3.connect('Login.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS users")
conn.commit()
conn.close()'''

myapp = Flask(__name__)
myapp.config['uploads'] = '/Users/vaishnavteeluck/Documents/Python/LoginApp_WithDB/Templates/uploads'

@myapp.route("/")
def homepage():
    return render_template("Homepage.html")

@myapp.route("/loggedinapplicant")
def loggedinapplicant():
    return render_template("LoggedInApplicant.html")

@myapp.route("/loggedin")
def loggedin():
    return render_template("LoggedIn.html")

##LOGIN
"""@myapp.route("/", methods = ["POST"])
def checklogin():
    UN = request.form['name']
    PW = request.form['password']
    UT = request.form['user_type']

   
    sqlconnection = sqlite3.connect('Login.db')
    cursor = sqlconnection.cursor()
    query1 = "SELECT Name, Password FROM users WHERE Name = ? AND Password = ? AND User_Type = ?"
    params = (UN, PW, UT)
    
    rows = cursor.execute(query1,params)
    rows = rows.fetchall()
    
    if len(rows) == 1 and UT == "Admin":
        return render_template("LoggedIn.html")
    elif len(rows) == 1 and UT == "Applicant":
        return render_template("LoggedInApplicant.html")
    else:
        '''return redirect("/profilenotfound")'''
        return render_template("ProfileNotFound.html")"""





'''@myapp.route("/", methods=["POST"])
def checklogin():
    UN = request.form["name"]
    PW = request.form["password"]
    UT = request.form["user_type"]

    sqlconnection = sqlite3.connect("Login.db")
    cursor = sqlconnection.cursor()
    query1 = "SELECT User_ID, Name, Password FROM users WHERE Name = ? AND Password = ? AND User_Type = ?"
    params = (UN, PW, UT)

    rows = cursor.execute(query1, params)
    rows = rows.fetchall()

    if len(rows) == 1 and UT == "Admin":
        resp = make_response(render_template("LoggedIn.html"))
        resp.set_cookie("user_id", str(rows[0][0]))
        resp.set_cookie("username", rows[0][1])
        resp.set_cookie("usertype", UT)
        return resp
    elif len(rows) == 1 and UT == "Applicant":
        resp = make_response(render_template("LoggedInApplicant.html"))
        resp.set_cookie("user_id", str(rows[0][0]))
        resp.set_cookie("username", rows[0][1])
        resp.set_cookie("usertype", UT)
        return resp
    else:
        return render_template("ProfileNotFound.html")
'''


@myapp.route("/", methods=["POST"])
def checklogin():
    UN = request.form["name"]
    PW = request.form["password"]
    UT = request.form["user_type"]

    sqlconnection = sqlite3.connect("Login.db")
    cursor = sqlconnection.cursor()
    query1 = "SELECT User_ID, Name, Password FROM users WHERE Name = ? AND Password = ? AND User_Type = ?"
    params = (UN, PW, UT)

    rows = cursor.execute(query1, params)
    rows = rows.fetchall()

    if len(rows) == 1 and UT == "Admin":
        resp = make_response(render_template("LoggedIn.html"))
        resp.set_cookie("user_id", str(rows[0][0]), max_age=3600)
        resp.set_cookie("username", rows[0][1])
        resp.set_cookie("usertype", UT)
        return pass_cookie(resp)
    elif len(rows) == 1 and UT == "Applicant":
        resp = make_response(render_template("LoggedInApplicant.html"))
        resp.set_cookie("user_id", str(rows[0][0]), max_age=3600)
        resp.set_cookie("username", rows[0][1])
        resp.set_cookie("usertype", UT)
        return pass_cookie(resp)
    else:
        return render_template("ProfileNotFound.html")


def pass_cookie(response):
    cookie_value = request.cookies.get("user_id")
    if cookie_value:
        response.set_cookie("user_id", cookie_value, max_age=3600)
        response.set_cookie("username", request.cookies.get("username"))
        response.set_cookie("usertype", request.cookies.get("usertype"))
    return response





##REGISTER
@myapp.route("/register", methods = ["GET", "POST"])
def registerpage():
    if request.method == "POST":
        dUN = request.form['name']
        dSN = request.form['surname']
        Uemail = request.form['email']
        dPW = request.form['password']
        Uusertype = request.form['user_type']
        
       
        sqlconnection = sqlite3.connect('Login.db')
        cursor = sqlconnection.cursor()
        query1 = "INSERT INTO users (Name, Surname, Email, Password, User_Type) VALUES(?, ?, ?, ?,?)"
        values = (dUN, dSN, Uemail, dPW, Uusertype)
        cursor.execute(query1,values)
        sqlconnection.commit()
        '''return redirect("/")'''
        return render_template("SuccessfulRegistration.html")
    return render_template("Register.html")

##ADD JOB
@myapp.route("/addjob", methods = ["GET", "POST"])
def addjob():
    if request.method == "POST":
        jTitle = request.form['jobtitle']
        jDes = request.form['jobdescription']
        fAc = request.form['faculty']
    

        sqlconnection = sqlite3.connect('Login.db')
        cursor = sqlconnection.cursor()
    
        query1 = "INSERT INTO jobs (Job_Title, Job_Description, Faculty) VALUES(?, ?, ?)"
        values = (jTitle, jDes, fAc)
        cursor.execute(query1,values)
        sqlconnection.commit()
        '''return redirect("/")'''
        return render_template("SuccessfulJobAdded.html")
    return render_template("AddJob.html")

## VIEW DATABASE
'''@myapp.route('/availablejobs')'''
@myapp.route('/selectedFile')
def index():
    conn = sqlite3.connect('Login.db')
    cursor = conn.cursor()
    cursor.execute('SELECT JobId, Job_Title, Job_Description, Faculty FROM jobs')
    jobs = cursor.fetchall()
    conn.close()
    return render_template('selectedFile.html', jobs=jobs)
'''return render_template('AvailableJobs.html', jobs=jobs)
'''

'''##SELECT RECORD - TO EDIT JOBS
import sqlite3

@myapp.route('/selectedFile', methods=['GET', 'POST'])
def select_record_from_database():
    if request.method == 'POST':
        # Get the selected ID value from the form data
        selected_id = request.form['selected_job']
        
        conn = sqlite3.connect('Login.db')
        c = conn.cursor()

        # Execute the SELECT statement using the selected ID value
        c.execute("SELECT * FROM jobs WHERE JobId=?", (selected_id,))

        # Fetch the selected record
        selected_record = c.fetchone()

        # Close the database connection
        conn.close()

        # Return the selected record
        return render_template('UpdateJob.html', job=selected_record, selected_job=selected_id)

    else:
        return "Error: Invalid request method."


##Update Record
@myapp.route('/updateJob', methods=['POST'])
def update_job():
    try:
        # Get the form data
        job_Id = request.form['JobId']
        job_title = request.form['Job_Title']
        job_description = request.form['Job_Description']
        faculty = request.form['Faculty']

        # Connect to the database
        conn = sqlite3.connect('Login.db')
        c = conn.cursor()

        # Execute the UPDATE statement to update the job record
        c.execute("UPDATE jobs SET Job_Title=?, Job_Description=?, Faculty=? WHERE JobId=?", (job_title, job_description, faculty, job_Id,))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Redirect to the jobs page
        return redirect('/selectedFile')

    except Exception as e:
        print(e)
        return "Error: Could not update job record."
'''


##SELECT RECORD
@myapp.route('/selectedFile', methods=['POST'])
def select_job():
    if request.method == 'POST':
        # Get the selected job id from the form data
        selected_job = request.form['selected_job']

        # Connect to the jobs database
        conn = sqlite3.connect('Login.db')
        c = conn.cursor()

        # Retrieve the selected job record
        c.execute("SELECT * FROM jobs WHERE JobId=?", (selected_job,))
        job = c.fetchone()

        # Render the job edit form
        return render_template('UpdateJob.html', job=job)

##UPDATE RECORD
@myapp.route('/updateJob', methods=['POST'])
def update_job():
    if request.method == 'POST':
        # Get the job details from the form data
        job_id = request.form['job_id']
        job_title = request.form['job_title']
        job_desc = request.form['job_desc']
        faculty = request.form['faculty']

        # Connect to the jobs database
        conn = sqlite3.connect('Login.db')
        c = conn.cursor()

        # Update the job record with the new details
        c.execute("UPDATE jobs SET Job_Title=?, Job_Description=?, Faculty=? WHERE JobId=?", (job_title, job_desc, faculty, job_id))
        conn.commit()

        # Redirect back to the job list
        return redirect('/selectedFile')

##APPLY FOR JOB



## VIEW DATABASE
@myapp.route('/availablejobs')
def Applicantindex():
    conn = sqlite3.connect('Login.db')
    cursor = conn.cursor()
    cursor.execute('SELECT JobId, Job_Title, Job_Description, Faculty FROM jobs')
    jobs = cursor.fetchall()
    conn.close()
    return render_template('AvailableJobs.html', jobs=jobs)

##Apply 

@myapp.route('/availablejobs', methods=['GET', 'POST'])
def select_job_apply(): 
    # Retrieve the value of the 'user_id' cookie
    user_id = request.cookies.get('user_id')

    if request.method == 'POST':
        # Get the selected ID value from the form data
        select_id = request.form['select_job']
        
        conn = sqlite3.connect('Login.db')
        c = conn.cursor()

        # Execute the SELECT statement using the selected ID value
        c.execute("SELECT * FROM jobs WHERE JobId=?", (select_id,))

        # Fetch the selected record
        select_record = c.fetchone()

        # Close the database connection
        conn.close()

        # Return the selected record
        '''return render_template('Apply.html', job=select_record, selected_job=select_id)'''
        return render_template('Apply.html', job=select_record, selected_job=select_id, jobid=select_id)


    else:
        return "Error: Invalid request method."



##Update Record
'''@myapp.route('/applyjob', methods=['POST'])
def apply_job():
    try:
        # Get the form data
        job_Id = request.form['JobId']
        job_title = request.form['Job_Title']
        job_description = request.form['Job_Description']
        faculty = request.form['Faculty']

        # Connect to the database
        conn = sqlite3.connect('Login.db')
        c = conn.cursor()

        # Execute the UPDATE statement to update the job record
        c.execute("UPDATE jobs SET Job_Title=?, Job_Description=?, Faculty=? WHERE JobId=?", (job_title, job_description, faculty, job_Id,))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Redirect to the jobs page
        return redirect('/selectedFile')

    except Exception as e:
        print(e)
        return "Error: Could not update job record."
    '''





import sqlite3
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

@myapp.route('/apply', methods=['GET', 'POST'])
def applyjob():
    if request.method == 'POST':
        # Get the selected job ID and user ID
        job_id = request.form['job_id']
        user_id = request.cookies.get('user_id')
        
        # Save the uploaded PDF file to the server
        '''file = request.files['cv']
        filename = secure_filename(file.filename)
        file.save('uploads/' + filename)'''
        
        file = request.files['cv']
        filename = secure_filename(file.filename)
        file.save(os.path.join(myapp.config['uploads'], filename))

        # Add the application to the database
        conn = sqlite3.connect('Login.db')
        c = conn.cursor()
        c.execute("INSERT INTO AppliedJobs (JobId, User_ID, CV) VALUES (?, ?, ?)",
                  (job_id, user_id, filename))
        conn.commit()
        conn.close()
        
        # Redirect the user to the success page
        '''return redirect(url_for('/availablejobs'))'''
        return redirect('/availablejobs')
    else:
        return "Error: Invalid request method."

##LOGOUT AND CLEAR COOKIES
from flask import make_response

def clear_cookies():
    # Create an empty response object
    resp = make_response()

    # Iterate over all the cookies in the request
    for cookie_name in request.cookies:
        resp.delete_cookie(resp)

    # Return the response object
    return resp

@myapp.route('/logout')
def logout():
    # Clear all cookies
    clear_cookies()

    # Redirect the user to the login page
    return redirect('/login')








if __name__ == "__main__":
   myapp.run(port=8083, debug=True)
