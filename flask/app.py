from flask import Flask, render_template,request
import numpy as np
import pickle 
app  = Flask(__name__)
model=pickle.load(open("bank.pkl",'rb'))

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/login', methods = ["POST"])
def login():
    age=request.form["age"]
    j = request.form["j"]
    if j=="admin":
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12=1,0,0,0,0,0,0,0,0,0,0,0
    if j=="technician":
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12=0,0,0,0,0,0,0,0,0,1,0,0
    if j=="services":
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12=0,0,0,0,0,0,0,1,0,0,0,0
    if j=="management":
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12=0,0,0,0,1,0,0,0,0,0,0,0
    if j=="retired":
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12=0,0,0,0,0,1,0,0,0,0,0,0    
    if j=="blue-collar":
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12=0,1,0,0,0,0,0,0,0,0,0,0    
    if j=="unemployed":
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12=0,0,0,0,0,0,0,0,0,0,1,0    
    if j=="entrepreneur":
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12=0,0,1,0,0,0,0,0,0,0,0,0   
    if j=="housemaid":
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12=0,0,0,1,0,0,0,0,0,0,0,0   
    if j=="unknown":
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12=0,0,0,0,0,0,0,0,0,0,0,1   
    if j=="self-employed":
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12=0,0,0,0,0,0,1,0,0,0,0,0   
    if j=="student":
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12=0,0,0,0,0,0,0,0,1,0,0,0       
    ms=request.form["ms"]
    if ms=="married":
        ms1,ms2,ms3=0,1,0
    if ms=="single":
        ms1,ms2,ms3=0,0,1
    if ms=="divorced":
        ms1,ms2,ms3=1,0,0          
    edu = request.form["edu"]
    if edu=="secondary":
        edu1,edu2,edu3,edu4=0,1,0,0
    if edu=="tertiary":
        edu1,edu2,edu3,edu4=0,0,1,0
    if edu=="primary":
        edu1,edu2,edu3,edu4=1,0,0,0  
    if edu=="unknown":
        edu1,edu2,edu3,edu4=0,0,0,1    
    de = request.form["de"]  
    if de=="yes":
        de1=1
    if de=="no":
        de1=0     
    balance = request.form["balance"]
    h = request.form["h"]
    if h=="no":
        h1=0
    if h=="yes":
        h1=1
    ln = request.form["ln"]
    if ln=="no":
        ln1=0
    if ln=="yes":
        ln1=1 
    con = request.form["con"]
    if con=="unknown":
        con1,con2,con3=0,0,1
    if con=="cellular":
        con1,con2,con3=1,0,0
    if con=="telephone":
        con1,con2,con3=0,1,0    
    dob = request.form["dob"]
    mon = request.form["mon"]
    if mon=="January":
        mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11,mon12=0,0,0,0,1,0,0,0,0,0,0,0
    if mon=="February":
        mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11,mon12=0,0,0,1,0,0,0,0,0,0,0,0
    if mon=="March":
        mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11,mon12=0,0,0,0,0,0,0,1,0,0,0,0
    if mon=="April":
        mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11,mon12=1,0,0,0,0,0,0,0,0,0,0,0
    if mon=="May":
        mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11,mon12=0,0,0,0,0,0,0,0,1,0,0,0    
    if mon=="June":
        mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11,mon12=0,0,0,0,0,0,1,0,0,0,0,0    
    if mon=="July":
        mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11,mon12=0,0,0,0,0,1,0,0,0,0,0,0    
    if mon=="August":
        mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11,mon12=0,1,0,0,0,0,0,0,0,0,0,0   
    if mon=="September":
        mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11,mon12=0,0,0,0,0,0,0,0,0,0,0,1
    if mon=="October":
        mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11,mon12=0,0,0,0,0,0,0,0,0,0,1,0   
    if mon=="November":
        mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11,mon12=0,0,0,0,0,0,0,0,0,1,0,0  
    if mon=="December":
        mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11,mon12=0,0,1,0,0,0,0,0,0,0,0,0           
    duration = request.form["duration"]
    campaign = request.form["campaign"]
    pdays = request.form["pdays"]
    previous = request.form["previous"]
    p = request.form["p"]
    if p=="unknown":
        p1,p2,p3,p4=0,0,0,1
    if  p=="other":
        p1,p2,p3,p4=0,1,0,0
    if p=="failure":
        p1,p2,p3,p4=1,0,0,0
    if p=="success":
        p1,p2,p3,p4=0,1,0,0


    total = [[age,j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,ms1,ms2,ms3,edu1,edu2,edu3,edu4,de1,balance,h1,ln1,con1,con2,con3,dob,mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11,mon12,duration,campaign,pdays,previous,p1,p2,p3,p4]]
    
    ans=model.predict(total)
    print(ans)
    index = ['Yes','No']
    text = "Outcome : " + str(index[ans[0]])
    print(text)
    return render_template('index.html',label=text)
   

if __name__=='__main__':
    app.run(debug = True)
