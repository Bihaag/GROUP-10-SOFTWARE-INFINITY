from flask import Flask, request, render_template, redirect, url_for, request, make_response, session, send_from_directory, abort
from flask_sqlalchemy import SQLAlchemy
import os
import sqlite3

currentlocation = os.path.dirname(os.path.abspath(__file__))

##CREATING TABLE(USERS) IN DB
"""import sqlite3
conn = sqlite3.connect('Login.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE users (User_ID INTEGER PRIMARY KEY, Name TEXT, Surname TEXT, Email TEXT,Cell_Num CHAR(10), Password TEXT,  User_Type TEXT)')
conn.commit()
conn.close()"""

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
                JobId INTEGER,
                CV BLOB, Status Bool,
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
"""sqlconnection = sqlite3.connect('Login.db')
cursor = sqlconnection.cursor()
cursor.execute("DELETE FROM users WHERE Name = 'Bihaag'")
sqlconnection.commit()
sqlconnection.close()"""

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
"""import sqlite3
conn = sqlite3.connect('Login.db')
c = conn.cursor()
c.execute('DELETE FROM appliedjobs')
conn.commit()
conn.close()"""

##DROP TABLE(USERS)
"""import sqlite3
conn = sqlite3.connect('Login.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS users")
conn.commit()
conn.close()"""

##DROP TABLE(APPLIED JOBS)
"""import sqlite3
conn = sqlite3.connect('Login.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS appliedjobs")
conn.commit()
conn.close()"""

myapp = Flask(__name__)
myapp.config['uploads'] = 'C:/Users/AMD/Desktop/PBDEPROJ-Main/Python/Python/LoginApp_WithDB/Templates/uploads'
myapp.secret_key = 'my_secret_key'


##RENDERING TEMPLATES
@myapp.route("/")
def homepage():
    return render_template("Homepage.html")

@myapp.route("/loggedinapplicant")
def loggedinapplicant():
    return render_template("LoggedInApplicant.html")

@myapp.route("/loggedin")
def loggedin():
    return render_template("LoggedIn.html")

@myapp.route("/updatesuccess")
def updatesuccess():
    return render_template("UpdateSuccess.html")

@myapp.route("/jobappsuccess")
def jobappsuccess():
    return render_template("JobApplicationSuccess.html")

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
        Cnum = request.form['cell_num']
        dPW = request.form['password']
        Uusertype = request.form['user_type']
        
       
        sqlconnection = sqlite3.connect('Login.db')
        cursor = sqlconnection.cursor()
        query1 = "INSERT INTO users (Name, Surname, Email,Cell_Num, Password, User_Type) VALUES(?, ?, ?, ?,?, ?)"
        values = (dUN, dSN, Uemail,Cnum, dPW, Uusertype)
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

## VIEW JOBS DATABASE
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

##DELETE JOB

@myapp.route('/deleteJob', methods=['POST'])
def delete_job():
    if request.method == 'POST':
        # Get the job ID from the form data
        job_id = request.form['job_id']

        # Connect to the jobs database
        conn = sqlite3.connect('Login.db')
        c = conn.cursor()

        # Delete the job record with the given ID
        c.execute("DELETE FROM jobs WHERE JobId=?", (job_id,))
        conn.commit()

        # Redirect back to the job list
        return redirect('/selectedFile')






##APPLY FOR JOB
## VIEW  JOBS DATABASE
@myapp.route('/availablejobs')
def Applicantindex():
    conn = sqlite3.connect('Login.db')
    cursor = conn.cursor()
    cursor.execute('SELECT JobId, Job_Title, Job_Description, Faculty FROM jobs')
    jobs = cursor.fetchall()
    conn.close()
    return render_template('AvailableJobs.html', jobs=jobs)


##Apply FOR JOB
@myapp.route('/availablejobs', methods=['GET', 'POST'])
def select_job_apply(): 
    # Retrieve the value of the 'user_id' cookie
    '''user_id = request.cookies.get('user_id')
    select_id = request.args.get('select_job')
    print(select_id)'''

    if request.method == 'POST':
        # Get the selected ID value from the form data
        """select_id = request.form['select_id']"""
        select_id = request.args.get('select_id')
        """print(select_id)"""

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
        """return redirect('/apply?jobid={}'.format(select_id))"""
        return redirect(url_for('applyjob', jobid=select_id))



    else:
        return "Error: Invalid request method."




##SUBMIT APPLICATION FOR JOB
import sqlite3
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

@myapp.route('/apply', methods=['GET', 'POST'])
def applyjob():
    if request.method == 'POST':
        # Retrieve the job ID from the request arguments
        jobid = request.args.get('jobid')
        '''jobid = request.form.get('jobid')'''
        print("Job ID (POST):", jobid)
        

        # Retrieve the user ID from the cookie
        user_id = request.cookies.get('user_id')
        status = False
        
        # Check if a file was uploaded
        if 'cv' not in request.files:
            return "Error: No CV file attached"
        
        # Save the uploaded PDF file to the server
        file = request.files['cv']
        if file.filename == '':
            return "Error: No selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(myapp.config['uploads'], filename))
        else:
            return "Error: File type not allowed"
        
        # Add the application to the database
        conn = sqlite3.connect('Login.db')
        c = conn.cursor()
        c.execute("INSERT INTO AppliedJobs (User_ID, JobId, CV, Status) VALUES (?, ?, ?, ?)",
          ( user_id, jobid, filename, status))
        print(f"Inserted values: {jobid}, {user_id}, {filename}, {status}")
        conn.commit()
        conn.close()
        
        # Redirect the user to the success page
        return redirect('/jobappsuccess')
    else:
        # Retrieve the selected job ID
        jobid = request.args.get('jobid')
        print("Job ID (GET):", jobid)

        # Retrieve the job details from the database
        conn = sqlite3.connect('Login.db')
        c = conn.cursor()
        c.execute("SELECT * FROM jobs WHERE JobId=?", (jobid,))
        job_details = c.fetchone()
        conn.close()
        
        print("Job ID in form submission:", jobid)

        # Display the job application form to the user
        return render_template('Apply.html', job=job_details, jobid=jobid)





def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'pdf', 'txt', 'doc', 'docx'}


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

@myapp.route('/logout', methods=['POST'])
def logout():
    # Clear the session cookie
    session.clear()

    # Clear the user_id, username, and usertype cookies
    resp = make_response(redirect('/'))
    resp.delete_cookie('user_id')
    resp.delete_cookie('username')
    resp.delete_cookie('usertype')

    return resp

##VIEW INACTIVE APPLICATIONS
@myapp.route('/inactiveapplications', methods=['GET', 'POST'])
def Inactiveapplications():
    conn = sqlite3.connect('Login.db')
    cursor = conn.cursor()
    '''cursor.execute('SELECT User_ID, JobId, CV, Status FROM appliedjobs')'''
    cursor.execute('SELECT appliedjobs.AppJob_ID, appliedjobs.User_ID, users.Name, users.Surname, users.Email, users.Cell_Num, jobs.Job_Title, appliedjobs.CV, appliedjobs.Status FROM appliedjobs INNER JOIN users ON appliedjobs.User_ID = users.User_ID INNER JOIN jobs ON appliedjobs.JobId = jobs.JobId WHERE appliedjobs.Status = 1')
    jobs = cursor.fetchall()
    conn.close()
    return render_template('InactiveApplications.html', jobs=jobs)

##VIEW ACTIVE APPLICATIONS
@myapp.route('/applications', methods=['GET', 'POST'])
def applications():
    conn = sqlite3.connect('Login.db')
    cursor = conn.cursor()
    '''cursor.execute('SELECT User_ID, JobId, CV, Status FROM appliedjobs')'''
    cursor.execute('SELECT appliedjobs.AppJob_ID, appliedjobs.User_ID, users.Name, users.Surname, users.Email, users.Cell_Num, jobs.Job_Title, appliedjobs.CV, appliedjobs.Status FROM appliedjobs INNER JOIN users ON appliedjobs.User_ID = users.User_ID INNER JOIN jobs ON appliedjobs.JobId = jobs.JobId WHERE appliedjobs.Status = 0')
    jobs = cursor.fetchall()
    conn.close()
    return render_template('Applications.html', jobs=jobs)


@myapp.route('/applications', methods=['GET', 'POST'])
def select_application(): 
    
    if request.method == 'POST':
        # Get the selected ID value from the form data
        select_app = request.form['select_app']
        
        conn = sqlite3.connect('Login.db')
        c = conn.cursor()

        # Execute the SELECT statement using the selected ID value
        c.execute("SELECT * FROM appliedjobs WHERE AppJob_ID=?", (select_app,))

        # Fetch the selected record
        select_record = c.fetchone()

        # Close the database connection
        conn.close()

        # Return the selected record
        '''return render_template('Apply.html', job=select_record, selected_job=select_id)'''
        return redirect('/applicationview?jobid={}'.format(select_app))


    else:
        return "Error: Invalid request method."




'''@myapp.route('/applicationview')
def appview():
    return render_template("ApplicationView.html")

'''

'''@myapp.route('/applicationview')
def appview():
    # Get the job ID from the URL query parameters
    job_id = request.args.get('select_app')
    print(job_id)

    # Connect to the database and retrieve the job status
    conn = sqlite3.connect('Login.db')
    c = conn.cursor()
    c.execute("SELECT Status FROM appliedjobs WHERE AppJob_ID=?", (job_id,))
    job_status = c.fetchone()
    print(job_status)
    conn.close()

    # Render the template with the job status and ID
    return render_template('ApplicationView.html', job_id=job_id, job_status=job_status)
'''

@myapp.route('/applicationview')
def appview():
    # Get the job ID from the URL query parameters
    appjob_id = request.args.get('select_app')
    print(appjob_id)

    # Connect to the database and retrieve the job status
    conn = sqlite3.connect('Login.db')
    c = conn.cursor()
    c.execute("SELECT Status FROM appliedjobs WHERE AppJob_ID=?", (appjob_id,))
    job_status = c.fetchone()
    print(job_status)
    conn.close()

    # Render the template with the job status and ID
    return render_template('ApplicationView.html', job_id=appjob_id, job_status=job_status)


"""@myapp.route('/updatestatus', methods=['POST'])
def updatestatus():
    # Get the job ID from the form submission
    appjob_id = request.form.get('appjob_id')
    print(appjob_id)

    # Get the new status value from the form submission
    new_status = request.form.get('status')
    print(new_status)

    # Connect to the database and update the job status
    conn = sqlite3.connect('Login.db')
    c = conn.cursor()
    c.execute("UPDATE appliedjobs SET Status=? WHERE AppJob_ID=?", (new_status, appjob_id))
    conn.commit()
    conn.close()

    # Redirect to the applications page
    '''return redirect('/applications')'''
    return render_template('Applications.html')"""

import smtplib
from email.mime.text import MIMEText

@myapp.route('/updatestatus', methods=['POST'])
def updatestatus():
    # Get the job ID from the form submission
    appjob_id = request.form.get('appjob_id')
    print(appjob_id)

    # Get the new status value from the form submission
    new_status = request.form.get('status')
    print(new_status)

    # Connect to the database and update the job status
    conn = sqlite3.connect('Login.db')
    c = conn.cursor()
    c.execute("UPDATE appliedjobs SET Status=? WHERE AppJob_ID=?", (new_status, appjob_id))
    conn.commit()
    conn.close()

    # Send email if status is 0 or 1
    if new_status == '0':
        send_email("Application rejected", "Your application has been rejected.")
    elif new_status == '1':
        send_email("Application accepted", "Your application has been accepted.")

    # Redirect to the applications page
    '''return redirect('/applications')'''
    return render_template('UpdateSuccess.html')



"""def send_email(subject, message):
    # Set up email parameters
    sender_email = "teeluckvaish@gmail.com"
    receiver_email = "vaish.cars@gmail.com"
    app_password = "nqrlnffcudjrqvdf"

    # Create message object and set parameters
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email using SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)
"""

import sqlite3
import smtplib
from email.mime.text import MIMEText

def send_email(subject, message):
    # Set up email parameters
    sender_email = "teeluckvaish@gmail.com"
    app_password = "nqrlnffcudjrqvdf"

    appjob_id = request.form.get('appjob_id')
    print("App Job ID:",appjob_id)
    # Retrieve receiver email from user table in database
    conn = sqlite3.connect('Login.db')
    c = conn.cursor()
    c.execute("""SELECT users.Email
                  FROM users
                  JOIN appliedjobs ON users.User_ID = appliedjobs.User_ID
                  WHERE appliedjobs.AppJob_ID = ?""", (appjob_id,))
    result = c.fetchone()
    if result:
        receiver_email = result[0]
    else:
        print(f"No user found with ID {appjob_id}")
        return

    # Create message object and set parameters
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email using SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

    print(f"Email sent to {receiver_email}")

##UPDATE ADMIN PROFILE

@myapp.route('/updateadminprofile', methods=['GET', 'POST'])
def update_admin():
    # get the User_ID from the cookie
    user_id = request.cookies.get('user_id')

    # connect to the database
    conn = sqlite3.connect('Login.db')
    c = conn.cursor()

    if request.method == 'POST':
        # get the updated user data from the HTML form
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        cell_num = request.form['cell_num']

        # update the user's record
        c.execute("UPDATE users SET Name = ?, Surname = ?, Email = ?, Cell_Num = ? WHERE User_ID = ?", 
                  (name, surname, email,cell_num, user_id))

        # commit the changes to the database
        conn.commit()

        # close the database connection
        conn.close()

        # redirect to the user's profile page
        return redirect('/loggedin')

    # if the request method is GET, display the HTML form for updating user data
    else:
        # get the user's current data from the database
        c.execute("SELECT name, surname, email, cell_num FROM users WHERE User_ID = ?", (user_id,))
        user_data = c.fetchone()

        # close the database connection
        conn.close()

        # render the HTML form with the user's current data pre-populated
        return render_template('updateadminprofile.html', user_data=user_data)


##UPDATE USER PROFILE
@myapp.route('/updateuserprofile', methods=['GET', 'POST'])
def update_user():
    # get the User_ID from the cookie
    user_id = request.cookies.get('user_id')

    # connect to the database
    conn = sqlite3.connect('Login.db')
    c = conn.cursor()

    if request.method == 'POST':
        # get the updated user data from the HTML form
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        cell_num = request.form['cell_num']

        # update the user's record
        c.execute("UPDATE users SET Name = ?, Surname = ?, Email = ?, Cell_Num = ? WHERE User_ID = ?", 
                  (name, surname, email,cell_num, user_id))

        # commit the changes to the database
        conn.commit()

        # close the database connection
        conn.close()

        # redirect to the user's profile page
        return redirect('/loggedinapplicant')

    # if the request method is GET, display the HTML form for updating user data
    else:
        # get the user's current data from the database
        c.execute("SELECT name, surname, email, cell_num FROM users WHERE User_ID = ?", (user_id,))
        user_data = c.fetchone()

        # close the database connection
        conn.close()

        # render the HTML form with the user's current data pre-populated
        return render_template('updateuserprofile.html', user_data=user_data)



##VIEW JOB APPLICATION STATUS

@myapp.route('/jobstatus')
def display_job_status():
    # Connect to the Login.db database
    user_id = request.cookies.get('user_id')
    print("UserID", user_id)
    conn = sqlite3.connect('Login.db')
    c = conn.cursor()

    # Retrieve the appliedJob record from the appliedjobs table for the given user_id
    c.execute('SELECT appliedjobs.AppJob_ID, jobs.JobId, jobs.Job_Title, appliedjobs.Status FROM appliedjobs JOIN jobs ON appliedjobs.JobId = jobs.JobId WHERE appliedjobs.User_ID = ?;', (user_id,))
    '''c.execute('SELECT AppJob_ID, Status FROM appliedjobs  WHERE User_ID = ?;', (user_id,))'''

    applied_jobs = c.fetchall()

    # Create a list of dictionaries to hold the appliedJob records
    job_list = []
    for row in applied_jobs:
        job_dict = {}
        job_dict['appjob_id'] = row[0]
        job_dict['job_id'] = row[1]
        job_dict['job_title'] = row[2]
        job_dict['status'] = "Pending" if row[3] == 0 else "Accepted"
        job_list.append(job_dict)

    # Debugging statements
    print("Applied Jobs:", applied_jobs)
    print("Job List:", job_list)

    # Close the database connection
    conn.close()

    # Render the template with the appliedJob records
    return render_template('jobstatus.html', jobs=job_list)

##GOOGLE API CODE
"""AIzaSyCetlNWp-FhPUoELs7RpJReUO6UHJeEelM"""


import googlemaps
import json
from datetime import datetime


@myapp.route('/directions', methods=['GET', 'POST'])
def display_directions():
    # Connect to the Login.db database
    user_id = request.cookies.get('user_id')
    print("UserID", user_id)
    conn = sqlite3.connect('Login.db')
    c = conn.cursor()

    # Retrieve the status of the job from the appjobs table for the given user_id
    c.execute('SELECT Status FROM appliedjobs WHERE User_ID = ?;', (user_id,))
    status = c.fetchone()
    print("Status", status)

    # Close the database connection
    conn.close()

    # Check if the status is 1 (i.e. job has been accepted)
    if status[0] == 1:
        if request.method == 'POST':
            # Use Google Maps API to display map with directions to given address
            gmaps = googlemaps.Client(key='AIzaSyCetlNWp-FhPUoELs7RpJReUO6UHJeEelM')
            now = datetime.now()
            # Get the current location from the form data
            current_location = request.form.get('current_location')
            # Get the directions to the destination address
            directions_result = gmaps.directions(current_location,
                                                  "7 Ritson Rd, Musgrave, Berea, 4001",
                                                  mode="driving",
                                                  departure_time=now)
            # Render the template with the map and directions
            return render_template('Directions.html', directions=json.dumps(directions_result))
        else:
            # Render the form to enter the current location
            return render_template('Directions.html')
    else:
        return render_template('DirectionsNotAvailable.html')


##DOWNLOAD PDF DOCS
@myapp.route('/download_cv/<filename>')
def download_cv(filename):
    return send_from_directory(myapp.config['uploads'], filename)
    
if __name__ == "__main__":
   myapp.run(port=8083, debug=True)
