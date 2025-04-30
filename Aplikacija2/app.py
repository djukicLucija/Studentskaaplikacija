from flask import Flask, render_template,request,redirect,url_for,session
from werkzeug.utils import secure_filename
import os 
import json
import cv2
from ultralytics import YOLO

app=Flask(__name__)
app.secret_key='supersecretkey'
UPLOAD_FOLDER='static/uploads'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER,exist_ok=True)

USERS={
    'admin':{'password':'admin','role':'admin'},
    'user':{'password':'user','role':'user'}
}
model=YOLO('yolov8n.pt')

def run_inference(image_path):
    results=model(image_path)
    img=results[0].plot()
    classes=results[0].names
    detected=set([classes[int(c)] for c in results[0].boxes.cls])
    with open("class_descriptions.json","r") as f:
        descs=json.load(f)
    descriptions={cls:descs.get(cls,"Nema dostupnog opisa") for cls in detected}
    return img, descriptions

@app.route('/',methods=["GET","POST"])

def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    if session.get('role')=='admin':
        return redirect (url_for('admin'))
    if request.method=="POST":
        file=request.files['image']
        if file:
            filename=secure_filename(file.filename)
            path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            img,descs=run_inference(path)
            result_path=os.path.join(app.config['UPLOAD_FOLDER'],'result.jpg')
            cv2.imwrite(result_path,img)
            return render_template('index.html'image='uploads/results.jpg',descriptions=descs)
        return render_template('index.html',role=session.get('role'))
@app.route('/admin',methods=['GET','POST'])

def admin():
    if 'username' not in session:
        return redirect(url_for('login'))
    if session.get('role')!='admin':
        return redirect(url_for('index'))
    with open('class_descriptions.json',"r") as f:
        descs=json.load(f)
    if request.method=='POST':
        for key in list(descs.keys()):
            if key in request.form:
                descs[key]=request.form[key]
        with open("class_descriptions.json", "w") as f:
            json.dumps(descs,f,indent=4)
            return redirect(url_for('admin'))
    return render_template('admin.html',description=descs)
    

    