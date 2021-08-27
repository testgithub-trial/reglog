from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy, Model

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = r'sqlite:////Users/Sudharsan/Downloads/OfflineBanking_flask-master/OfflineBanking_flask-master/gcp_webpage/GCP.db'
##C:\Users\Sudharsan\Downloads\OfflineBanking_flask-master\Offline_Banking\runner\db_module
db = SQLAlchemy(app)

app.secret_key = 'hello'


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    #$$$$$$$$$$$$$
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))


class vm_details(db.Model):
    vm_id = db.Column(db.Integer, primary_key=True)
    created_by= db.Column(db.String(80))#username
    vm_name = db.Column(db.String(80))#vm name
    zone = db.Column(db.String(80))
    machine_type = db.Column(db.String(80))
    OS_image  = db.Column(db.String(80))
    ###$$$$$$$$$$$$acc_email = db.Column(db.String(120))

    ##$$$$$$$$$$$$balance = db.Column(db.Integer)

class vpc_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_by= db.Column(db.String(80))#username

    vpc_name = db.Column(db.String(80))#vpcname
    region = db.Column(db.String(120))

    subnetname = db.Column(db.String(80))
    region = db.Column(db.String(80))
    subnetname0 = db.Column(db.String(80))
    region0 = db.Column(db.String(80))
    subnetname00 = db.Column(db.String(80))
    region00 = db.Column(db.String(80))
    
    
    
   #$$$$$ main_money_balance = db.Column(db.Integer)

    # balance_id = db.Column(db.Integer, db.ForeignKey('balance.id'),nullable=False)
    # balance = db.Column(db.Integer)


# @app.route("/")
# def delete():
# vm_details.query.filter_by(balance=500).delete()
#     db.session.commit()
#     return render_template("index.html")

globalvariable = []


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        
        
        uname = request.form["uname"]
        passw = request.form["passw"]
        session['uname'] = uname
        print('session---' * 10)
        print(session['uname'])
        globalvariable.append(uname)

        login = user.query.filter_by(username=uname, password=passw).first()
        print('#--' * 20)
        print(login)
        print('#--' * 20)
        if login is not None:
            # jj = user.query.filter_by(username=session['uname'])
            #
            # ss = jj.one().email
            # vv = jj.one().username
            #
            # show_balance = vpc_details.query.filter_by(created_by=session['uname']).first()
            #
            #
            #
            # ba = show_balance.main_money_balance


            # return redirect(url_for("showdetails"))
            return 'logged in'

            #return render_template('homepage.html', globalvariable=globalvariable, vv=vv, ss=ss,ba=ba)
        else:
            alert = 'Check Username & Password'
            return 'wrong password'
            #return render_template("loginpage.html", alert=alert)
    return render_template("loginpage.html")


@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        lastname = request.form['lname']
        #&&&&&&&&&&&&&&&phonenumber = request.form['phonenumber']
        mail = request.form['mail']
        passw = request.form['passw']
        #$$$$$$$$$$balance = 1000
        # alreadyexesist = user.query.filter_by(mail=mail).first()$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        alreadyexesist = user.query.filter_by(email=mail).first()
        if alreadyexesist is not None:
            message = 'Sorry! Email already EXIST'
            return render_template("register.html", message=message)
        else:
            register = user(username=uname, lname=lastname, email=mail, password=passw)
            # REGISTER FOR BALANCE vm_details
            # REGISTER FOR BALANCE vm_details
            db.session.add(register)
            db.session.commit()

            return redirect(url_for("login"))
        # return render_template ("loginpage.html")
    return render_template("register.html")

#
# #####################################################################################
# @app.route("/<username>")  # , methods=["GET", "POST"])
# def show_user(username):
#     vmhistory = vm_details.query.filter(vm_details.created_by.endswith(session['uname'])).all()
#     print('EEEE--' * 10)
#     #vmhistorylll = vm_details.query.filter(vm_details.created_by.endswith(session['uname'])).all()
#     trans = []
#     keyvalue1 = []
#
#
#
#
#     # print(u.acc_email)
#     print('EEEEE--' * 10)
#     for k in vmhistory:
#         print(k.acc_email)
#         print("-"*20)
#         CountryCodeDict1 = {k.created_by: [k.acc_email,k.credit,k.debit,k.balance]}
#         count = { "Name :": k.created_by,
#                   "Email :" :k.acc_email,
#                   "Credit :" :k.credit,
#                   "Debit :" : k.debit,
#                   "Balance" : k.balance
#
#         }
#         keyvalue1.append(count)
#         trans.append(CountryCodeDict1)
#
#
#
#         print("-" * 50)
#         trans.append(k.acc_email)
#         trans.append(k.created_by)
#         print(k.created_by)
#         trans.append(k.balance)
#         print(k.balance)
#
#
#
#     return render_template('show_user.html',len = len(trans), trans = trans,CountryCodeDict1=CountryCodeDict1,
#                            leen =len(keyvalue1), keyvalue1=keyvalue1
#                            )
#
#
# @app.route("/showdetails", methods=["GET", "POST"])
# def showdetails():
#     if request.method == 'POST':
#         username = request.form['USERNAME']
#         print(username)
#         acc = user.query.filter_by(username=username)
#         created_by = acc.one().username
#
#         = acc.one().email
#         acc_numb = acc.one().phonenumber
#         balance = 1000
#         print(created_by)
#         print(acc_email)
#         print(acc_numb)
#         print(type(acc_numb))
#
#
#         # showdetails = vm_details(acc_numb=acc_numb, created_by=created_by, acc_email=acc_email,
#         #                           balance=balance)
#         # db.session.add(showdetails)
#         # db.session.commit()
#         # print(acc, created_by, acc_email, acc_numb, balance)
#         return render_template('show_user.html', acc=acc, created_by=created_by, acc_email=acc_email,
#                                acc_numb=acc_numb,
#                                balance=balance)
#
#     return render_template('homepage.html')
#
#
# @app.route('/withdrawal', methods=['GET', 'POST'])
# def withdrawal():
#     if request.method == 'POST':
#         withdrawal = request.form['WITHDRAWAL']
#
#         jj = withdrawal
#
#         # jj = vm_details.query.filter_by(acc_email='sudharsanpilot@gmail.com')
#         jjj = vpc_details.query.filter_by(created_by=session['uname'])
#         print(session['uname'])
#         # print(jj.one().balance)
#         oldbalance = jjj.one().main_money_balance
#         print(oldbalance)
#         if int(withdrawal) > int(oldbalance) :
#             message = "Sorry "+ str(withdrawal)+" out of balance, Your Account Balance is = "+ str(oldbalance)
#             return render_template('withdrawal.html', message=message)
#         else:
#             print('#--' * 20)
#             print(withdrawal)
#             Newbalance = int(oldbalance) - int(withdrawal)
#             print(Newbalance)
#             print('#--' * 20)
#             acc = user.query.filter_by(username=session['uname'])
#             created_by = acc.one().username
#             acc_email = acc.one().email
#             acc_numb = acc.one().phonenumber
#
#             withdrawal = vm_details(acc_numb=acc_numb, created_by=created_by, acc_email=acc_email,
#                                      balance=Newbalance, debit="debit")
#             db.session.add(withdrawal)
#             db.session.commit()
#             updatee = vpc_details.query.filter_by(created_by=session['uname']).first()
#             updatee.main_money_balance = Newbalance
#             db.session.commit()
#             message = "Successfully "+ str(jj) +" withdrawal"
#             show_balance = vpc_details.query.filter_by(created_by=session['uname']).first()
#
#             ba = show_balance.main_money_balance
#
#             return render_template('withdrawal.html', message=message,ba=ba)
#
#
#     return render_template('homepage.html')
#
#
# @app.route('/deposit', methods=['GET', 'POST'])
# def deposit():
#     if request.method == 'POST':
#         deposit = request.form['DEPOSIT']
#         # jj = vm_details.query.filter_by(acc_email='sudharsanpilot@gmail.com')
#         jjj = vpc_details.query.filter_by(created_by=session['uname'])
#         print(session['uname'])
#         # print(jj.one().balance)
#         oldbalance = jjj.one().main_money_balance
#         print(oldbalance)
#         amo = deposit
#
#         print('#--' * 20)
#         print(deposit)
#         Newbalance = int(oldbalance) + int(deposit)
#         print(Newbalance)
#         print('#--' * 20)
#         acc = user.query.filter_by(username=session['uname'])
#         created_by = acc.one().username
#         acc_email = acc.one().email
#         acc_numb = acc.one().phonenumber
#
#         deposit = vm_details(acc_numb=acc_numb, created_by=created_by, acc_email=acc_email,
#                               balance=Newbalance,credit="credit")
#         db.session.add(deposit)
#         db.session.commit()
#         updatee = vpc_details.query.filter_by(created_by=session['uname']).first()
#         updatee.main_money_balance = Newbalance
#         db.session.commit()
#         show_balance = vpc_details.query.filter_by(created_by=session['uname']).first()
#
#         ba = show_balance.main_money_balance
#
#         return render_template('deposit.html',ba=ba,amo=amo)
#     return render_template('homepage.html')
#
@app.route("/allhistroy")
def allhistroy():
    vmhistory = vm_details.query.filter(vm_details.created_by.endswith(session['uname'])).all()

    # vmhistory = vm_details.query.filter(vm_details.created_by.endswith(session['uname'])).all()

    
    print('EEEE--' * 10)
    # vmhistorylll = vm_details.query.filter(vm_details.created_by.endswith(session['uname'])).all()
    trans = []
    keyvalue1 = []


    # print(u.acc_email)
    print('EEEEE--' * 10)
    for k in vmhistory:
        print(k.created_by)
        print("-" * 20)
        count = {"vm_name :": k.vm_name,
                 "zone :": k.zone,
                 "machine_type :": k.machine_type,
                 "OS_image": k.OS_image

                 }

        keyvalue1.append(count)
        print("-" * 50)
        #trans.append(k.acc_email)
        trans.append(k.created_by)
        print(k.created_by)

    vpchistory = vpc_details.query.filter(vpc_details.created_by.endswith(session['uname'])).all()
    keyvalue2 = []
    for v in vpchistory:
        # print(v.acc_email)
        print("-" * 20)
        count = {"vpc_name :": v.vpc_name,
                 "subnetname1 :":v.subnetname,
                 "region1 :": v.region,
                 "subnetname2": v.subnetname0,
                 "region2": v.region0,
                 "subnetname3": v.subnetname00,
                 "region3": v.region00
                 }
        keyvalue2.append(count)
    out = tuple(keyvalue1)
    print(out)

    return render_template('allhistroy.html',leen=len(keyvalue1), keyvalue1=keyvalue1,vpclen=len(keyvalue2),keyvalue2=keyvalue2)



@app.route("/vmupdate", methods=["GET", "POST"])
def vmupdate():
    created_by = 'sudhar'  # username
    vm_name = 'vmmm'  # vm name
    zone = 'zz'
    machine_type = 'mmm'
    OS_image = 'kkk'
    alreadyexesist = vm_details.query.filter_by(vm_name=vm_name).first()
    if alreadyexesist is not None:
        message = 'Sorry! VM NAME already EXIST'
        return 'vm name their'
            #return render_template("register.html", message=message)
    else:
        vmregister = vm_details(created_by=created_by, vm_name=vm_name, zone=zone, machine_type=machine_type,OS_image=OS_image)
        # REGISTER FOR BALANCE vm_details
        # REGISTER FOR BALANCE vm_details
        db.session.add(vmregister)
        db.session.commit()
        return 'updated'

            #return redirect(url_for("login"))
        # return render_template ("loginpage.html")
    #return render_template("register.html")
@app.route("/vpcupdate", methods=["GET", "POST"])
def vpcupdate():
    created_by = 'sudhar' # username

    vpc_name = 'vpc name'  # vpcname
    subnetname = 'ffff'
    region = 'kkk'
    subnetname0 = 'pppp'
    region0 = 'lllll'
    subnetname00 = 'kkkkk'
    region00 = 'llll'
    alreadyexesist = vm_details.query.filter_by(vpc_name=vpc_name).first()
    if alreadyexesist is not None:
        message = 'Sorry! VPC NAME already EXIST'
        return 'vpc name their'
            #return render_template("register.html", message=message)
    else:
        vpcregister = vpc_details(created_by=created_by, vpc_name=vpc_name, subnetname=subnetname,region=region,
                                  subnetname0=subnetname0,region0=region0,subnetname00=subnetname00,region00=region00)
        # REGISTER FOR BALANCE vm_details
        # REGISTER FOR BALANCE vm_details
        db.session.add(vpcregister)
        db.session.commit()
        return 'updated'







#
#
# @app.route("/returnpage")
# def returnpage():
#     jj = user.query.filter_by(username=session['uname'])
#     ss = jj.one().email
#     vv = jj.one().username
#     ll = jj.one().phonenumber
#     show_balance = vpc_details.query.filter_by(created_by=session['uname']).first()
#
#     ba = show_balance.main_money_balance
#
#
#     return render_template('homepage.html', vv=vv, ss=ss, ll=ll,ba=ba)
#
# @app.route("/features")
# def features():
#     jj = user.query.filter_by(username=session['uname'])
#     ss = jj.one().email
#     vv = jj.one().username
#     ll = jj.one().phonenumber
#
#
#     return render_template('features.html', vv=vv, ss=ss, ll=ll)
#
#
#
#
#
#

@app.route("/logout")
def logout():
    session.pop("uname", None)
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=5038)
