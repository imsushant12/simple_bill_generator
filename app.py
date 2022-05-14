from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

emails = ['ranjanyadav@gmail.com']
passwords = ['ranjanyadav']

accountNumbers = []
names = []
mobileNumbers = []
unitsConsumed = []


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email in emails and password in passwords:
            return redirect(url_for('generateBill'))

    return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email not in emails:
            emails.append(email)
            passwords.append(password)
            return redirect(url_for('login'))

    return render_template("register.html")


@app.route('/generateBill', methods=['GET', 'POST'])
def generateBill():
    if request.method == "POST":
        accountNumber = request.form["accountNumber"]
        name = request.form["name"]
        mobileNumber = request.form["mobileNumber"]
        units = request.form["units"]

        accountNumbers.append(accountNumber)
        names.append(name)
        mobileNumbers.append(mobileNumber)
        unitsConsumed.append(units)

        return redirect(url_for('bill'))

    return render_template("generateBill.html")


@app.route('/bill')
def bill():
    totalUnits = int(unitsConsumed[len(unitsConsumed) - 1]) * 7
    accountNumber = accountNumbers[len(accountNumbers) - 1]
    mobileNumber = mobileNumbers[len(mobileNumbers) - 1]
    name = names[len(names) - 1]

    details = []
    details.append(accountNumber)
    details.append(name)
    details.append(mobileNumber)
    details.append(totalUnits)

    return render_template("bill.html", details=details)


if __name__ == "__main__":
    app.run(debug=True)
