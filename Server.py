from flask import Flask, render_template,request,redirect
import csv
app = Flask(__name__,template_folder='templates')

print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt','a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file=database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv','a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        spamwriter = csv.writer(database2, delimiter=',',
                                quotechar='|', newline='', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "did not save to database. Try Again"
    else:
        return 'form submitted hooray'


if __name__ == '__main__':
    app.run()
