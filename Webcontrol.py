from flask import  Flask,render_template,request
import time
app = Flask(__name__)#Webapp
ShowValueServo1 = None # ตัวเเปลค่าที่เเสดงว่า Servo อยู่มุมเท่าไหร่
ShowValueServo2 = None
ShowValueServo3 = None
ShowValueServo4 = None
time.sleep(3)#delay 3 วินาที
@app.route('/', methods=['POST', 'GET'])
def CS():
    Author = "Gram"
    if request.method == "POST":
        global ShowValueServo1,ShowValueServo2,ShowValueServo3,ShowValueServo4 # Global value
        import ControlServo # เอามาจากอีกไฟล์
        A = ControlServo.Servo()
        if request.form['submit']=='1/0': #เมื่อกดปุ่มจะทำ
            A.LA0()
            ShowValueServo1 = 0
        elif request.form['submit']=='1/20':
            A.LA20()
            ShowValueServo1 = 20
        elif request.form['submit']=='1/40':
            A.LA40()
            ShowValueServo1 = 40
        elif request.form['submit']=='1/60':
            A.LA60()
            ShowValueServo1 = 60
        elif request.form['submit']=='1/80':
            A.LA80()
            ShowValueServo1 = 80
        elif request.form['submit']=='1/100':
            A.LA100()
            ShowValueServo1 = 100
        elif request.form['submit']=='1/120':
            A.LA120()
            ShowValueServo1 = 120
        elif request.form['submit']=='1/140':
            A.LA140()
            ShowValueServo1 = 140
        elif request.form['submit']=='1/160':
            A.LA160()
            ShowValueServo1 = 160
        elif request.form['submit']=='1/180':
            A.LA180()
            ShowValueServo1 = 180
        elif request.form['submit']=='2/0':
            A.LB0()
            ShowValueServo2 = 0
        elif request.form['submit']=='2/20':
            A.LB20()
            ShowValueServo2 = 20
        elif request.form['submit']=='2/40':
            A.LB40()
            ShowValueServo2 = 40
        elif request.form['submit']=='2/60':
            A.LB60()
            ShowValueServo2 = 60
        elif request.form['submit']=='2/80':
            A.LB80()
            ShowValueServo2 = 80
        elif request.form['submit']=='3/0':
            A.LC0()
            ShowValueServo3 = 0
        elif request.form['submit']=='3/20':
            A.LC20()
            ShowValueServo3 = 20
        elif request.form['submit']=='3/40':
            A.LC40()
            ShowValueServo3 = 40
        elif request.form['submit']=='3/60':
            A.LC60()
            ShowValueServo3 = 60
        elif request.form['submit']=='3/80':
            A.LC80()
            ShowValueServo3 = 80
        elif request.form['submit']=='4/120':
            A.LD120()
        elif request.form['submit']=='4/180':
            A.LD180()
        elif request.form['submit']=='5/0':
            A.LE0()
            ShowValueServo4 = 0
        elif request.form['submit']=='5/20':
            A.LE20()
            ShowValueServo4 = 20
        elif request.form['submit']=='5/40':
            A.LE40()
            ShowValueServo4 = 40
        elif request.form['submit']=='5/60':
            A.LE60()
            ShowValueServo4 = 60
        elif request.form['submit']=='5/80':
            A.LE80()
            ShowValueServo4 = 80
        elif request.form['submit']=='5/100':
            A.LE100()
            ShowValueServo4 = 100
        elif request.form['submit']=='5/120':
            A.LE120()
            ShowValueServo4 = 120
        elif request.form['submit']=='5/140':
            A.LE140()
            ShowValueServo4 = 140
        elif request.form['submit']=='5/160':
            A.LE160()
            ShowValueServo4 = 160
        elif request.form['submit']=='5/180':
            A.LE180()
            ShowValueServo4 = 180

        elif request.form['submit']=='123':
            A.LA80()
            A.LB0()
            A.LC80()
            ShowValueServo1 = 80
            ShowValueServo2 = 0
            ShowValueServo3 = 80




    return render_template('index.html', Author=Author, XAX = ShowValueServo1, XAA = ShowValueServo2, XAB = ShowValueServo3, XAD = ShowValueServo4)
if __name__ == "__main__":
    app.run(debug=True)
