from flask import Flask, render_template, url_for
import csv
import json
from models.email import Email
from models.log import Log

app = Flask(__name__)

def csvToEmailList(csvFilePath):
    #create list to store email objects
    emailList = []
 
    #open csv file and read in email data
    with open(csvFilePath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            emailList.append(Email(row[0], row[1], row[2],row[3],row[4]))
    
        #print(emailList)
        return emailList
    
def csvToLogList(csvFilePath):
    #create list to store log objects
    logList = []

    #open csv file and read in log data
    with open(csvFilePath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            logList.append(Log(row[0], row[1], row[2],row[3],row[4],row[5],row[6]))

        #print(emailList)
        return logList

@app.route('/')
def index():
    pieChartData = {'Task' : 'Total emails', 'Allowed' : 234, 'Blocked' : 153, 'Quarantine' : 86}
    barChartData = {'Task' : 'Threats found', 'Virus' : 57, 'Spam' : 56, 'Phishing' : 40}
    #print(data)
    
    return render_template('index.html', pieChartData = pieChartData, barChartData = barChartData)

@app.route('/emails')
def emails():
    headings = ("ID","From","To","Subject","Body")
    emailData = csvToEmailList('data/emails.csv')
    return render_template('emails.html',emailData = emailData,headings = headings)

@app.route('/logs')
def logs():
    headings = ("ID","Date","Time","From","To","Subject","Action")
    logData = csvToLogList('data/logs.csv')
    return render_template('logs.html', logData = logData, headings = headings)

if __name__ == "__main__":
    app.run(debug=True)
