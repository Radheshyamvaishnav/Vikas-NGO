from flask import Flask, request, render_template
import json
import os

import smtplib
from email.message import EmailMessage


app = Flask(__name__)

file = os.path.join(app.static_folder, 'data.json')

#"{{ url_for('static',filename='')}}"

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.form.get('subbtn') == 'Register':
               # Code for registration page
                email = request.form['email']
                password = request.form['password']
                userr = request.form['name']

                userdata = {
                    "username":userr,
                    "email": email,
                    "password":password
                }

                Email_Address = "vikas.singh12332141@gmail.com"
                Email_Password = "vikassinghips3star"

                msg = EmailMessage()
                msg['Subject'] = "Congrats !! from Vikas NGO EK Saath Subka Vikas"
                msg['From'] = Email_Address
                msg['To'] = email
                ping = 'Congrats Chacha' + userr + "!! \n You have been selected as Volunteer of Vikas NGO \n Please Stay Tuned for future events on our website. If you want to be volunteer of the event listed on website then call us @ +91 8087789896. \n\n Thanks and Regards,\n MLA Vikas Singh \n Parshad Aakash Chavan \n Nallasopra \n\n And yeh One Last Thing \' Abki Baar MOdi Sarkar\' "
                msg.set_content(ping)

                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

                    smtp.login(Email_Address, Email_Password)

                    
                    smtp.send_message(msg)

                
  
  
                # function to add to JSON
                def write_json(data, filename=file):
                    with open(filename,'w') as f:
                        json.dump(data, f, indent=4)
                    
                    
                with open(file) as json_file:
                    data = json.load(json_file)
                    
                    temp = data['volunteer_details']
                
                    # python object to be appended
                    y = userdata
                
                    # appending data to emp_details 
                    temp.append(y)
                    
                write_json(data)





                
                userkanaam = 'Welcome To Vikas NGO',userr
                return render_template('index.html', user=userkanaam)
            
    return render_template('index.html')






if __name__ == "__main__":
    app.run(debug = True)