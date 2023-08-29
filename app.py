from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Loawith od the trained model
model = joblib.load("Heart_Disease_Predictor.joblib")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from the form
        Age = float(request.form['Age'])
        Sex = int(request.form['Sex'])
        ChestPainType = int(request.form['ChestPainType'])
        RestingBP = float(request.form['RestingBP'])
        Cholesterol = int(request.form['Cholesterol'])
        FastingBS = float(request.form['FastingBS'])
        RestingECG = int(request.form['RestingECG'])
        MaxHR = float(request.form['MaxHR'])
        ExerciseAngina = int(request.form['ExerciseAngina'])
        Oldpeak = float(request.form['Oldpeak'])
        ST_Slope = int(request.form['ST_Slope'])
        

        # Make a prediction using the model
        prediction = model.predict([[Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope]])

        # Interpret the prediction
        result = 'heart disease' if prediction[0] == 1 else 'not heart disease'
        
        return render_template('index.html', result=result)
    
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
