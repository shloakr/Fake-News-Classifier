from flask import Flask, render_template, url_for, request
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.model_selection import train_test_split 


app = Flask(__name__,template_folder='template')

@app.route('/')
def home():
    return render_template('home.html')

df=pd.read_csv('train1.csv')
x_train,x_test,y_train,y_test=train_test_split(df['text'], df['label'], test_size=0.25, random_state=7, shuffle=True)
tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.75)
vec_train=tfidf_vectorizer.fit_transform(x_train.values.astype('U'))
vec_test=tfidf_vectorizer.transform( x_test.values.astype('U'))
#PassiveAggressiveClassifier
pac=PassiveAggressiveClassifier(max_iter=50, C=0.5)
pac.fit(vec_train,y_train)
    
@app.route('/predict', methods=['POST'])
def predict(): 

    if request.method == 'POST':
        comment=request.form["comment"]
        #data = [comment]
        vec_new = tfidf_vectorizer.transform([comment])
        y_pred_new = pac.predict(vec_new)
    return render_template('result.html', prediction= y_pred_new[0])

    # def classify(input_text):
    #     vec_new = tfidf_vectorizer.transform([input_text])
    #     y_pred_new = pac.predict(vec_new)
    #     return y_pred_new[0]
    # return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
    #app.run(debug=True)
