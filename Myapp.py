from flask import Flask,render_template,request
import pickle

app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('form.html')

@app.route('/predict',methods=['POST'])
def get_result():
    poly=pickle.load(open('Poly.pkl','rb'))
    model = pickle.load(open('model.pkl', 'rb'))
    query=[[float(request.form['text2'])]]
    x_query=poly.transform(query)
    sal=model.predict(x_query)
    #use model.predict to predict salary
    return 'Dear'+request.form["text1"]+'your predicted salary after'+request.form["text2"]+'Expeience is:'+str(sal)
if  __name__=='__main__':
    app.run(debug=True)