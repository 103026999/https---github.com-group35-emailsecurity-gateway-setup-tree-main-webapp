from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    pieChartData = {'Task' : 'Total emails', 'Allowed' : 234, 'Blocked' : 153, 'Quarantine' : 86}
    barChartData = {'Task' : 'Threats found', 'Virus' : 57, 'Spam' : 56, 'Phishing' : 40}
    #print(data)
    return render_template('index.html', pieChartData=pieChartData, barChartData=barChartData)

@app.route('/emails')
def emails():
    return render_template('emails.html')

@app.route('/logs')
def logs():
    return render_template('logs.html')

if __name__ == "__main__":
    app.run(debug=True)