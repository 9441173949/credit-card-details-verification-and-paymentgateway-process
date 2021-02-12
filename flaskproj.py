from flask import Flask,request,render_template
import random
app = Flask(__name__)

@app.route('/')
def  datacollection():
    return render_template("ProcessPayment.html")

@app.route('/ProcessPayment',methods=['POST','GET'])
def ProcessPayment():
    credit_card_number=request.form["credit_card_number"]
    card_holder_name=request.form["card_holder_name"]
    expiration_date=request.form["expiration_date"]
    security_code=request.form["security_code"]
    Amount=request.form["Amount"]
    count = 0
    if len(credit_card_number) != 16 or credit_card_number.isnumeric() == False:
        count = count + 1

    if  card_holder_name.isalpha() == False:
        count = count + 1

    expiration_date_list = expiration_date.split('-')
    if int(expiration_date_list[0]) < 2021:
        count = count + 1

    if security_code!="":
        if len(security_code) != 3:
            count = count + 1

    if Amount.isdecimal() == False:
        count = count + 1

    if count > 0:
        return '400 bad request'
    else:
        n=random.randrange(1,10)
        if int(Amount) <= 20:
            if n<5:
                return render_template('output.html',info="payment processing using Cheap Payment Gateway press OK to continue")
            else:
                return render_template("busy.html")
        elif 21 < int(Amount) <= 500:
            if n<5:
                return  render_template('output.html',info="payment processing using Expensive Payment Gateway press OK to continue")
            else:
                return render_template("Expensive.html")
        elif int(Amount) > 500:
            if n<5:
                return render_template('output.html',info="payment processing using Premium Payment Gateway press OK to continue")
            else:

                return render_template("Premium.html",info="you have 3 tries left")

@app.route('/complete',methods=['POST','GET'])
def complete():
    return render_template("200OK.html")

@app.route('/Premium',methods=['POST','GET'])
def PremiumTries():
    j=random.randrange(0,4)
    for i in range(1,4):
        if i==j:
            return render_template("Premium.html",info="you have"+" "+str(i+1)+" "+"tries left" )
        else:
            return render_template("200OK.html")


if __name__ == "__main__":
    app.run(debug=True)