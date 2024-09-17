from flask import Flask ,render_template,request
import pickle


app=Flask(__name__)


with open('RFC_crop.pkl','rb')as f:
    model1 = pickle.load(f)

@app.route('/') #it is use to routing path

def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')


@app.route('/result',methods=['POST','GET'])
def result():
    nitrogen=int(request.form.get('unitrogen'))
    phosphorus = float(request.form.get('uphosphorus'))
    potassium =float(request.form.get('upotassium'))
    temparature = float(request.form.get('utemp'))
    humidity = int(request.form.get('uhumidity'))
    ph = int(request.form.get('uph'))
    rainfall = int(request.form.get('urain'))
    

    input= [[nitrogen,phosphorus,potassium,temparature,humidity,ph,rainfall]]
    predict = model1.predict(input)
    print(predict)


    if predict == [0]:
        result= "apple"
    elif predict == [1]:
        result= "banana"
    elif predict == [2]:
        result= "blackgram"
    elif predict == [3]:
        result= "chickpea"
    elif predict == [4]:
        result= "coconut"
    elif predict == [5]:
        result= "coffee"
    elif predict == [6]:
        result= "cotton"
    elif predict == [7]:
        result= "grapes"
    elif predict == [8]:
        result= "jute"
    elif predict == [9]:
        result= "kidneybeans"
    elif predict == [10]:
        result= "lentil"
    elif predict == [11]:
        result= "maize"
    elif predict == [12]:
        result= "mango"
    elif predict == [13]:
        result= "mothbeans"
    elif predict == [14]:
        result= "mungbean"
    elif predict == [15]:
        result= "muskmelon"
    elif predict == [16]:
        result= "orange"
    elif predict == [17]:
        result= "papaya"
    elif predict == [18]:
        result= "pigeonpeas"
    elif predict == [19]:
        result= "pomegranate"
    elif predict == [20]:
        result= "rice"
    elif predict == [21]:
        result= "watermelon"
    else: 
        result="unknown crops"
    
    return render_template('result.html',res=result)

    



    
if __name__ == '__main__':

    app.run(debug=True)