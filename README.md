https://www.youtube.com/watch?v=wCcg2lqyZOg
# HeartDiseasePredictorApp
my first machine learning app,

#Heart Disease Prediction App:  

The app predicts whether with given indicators if a person has a heart disease or not.  

##Data Collection:  

THE data is picked from kaggle.  

#Attribute Information
1.	Age: age of the patient [years]
2.	Sex: sex of the patient [M: Male, F: Female]
3.	ChestPainType: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
4.	RestingBP: resting blood pressure [mm Hg]
5.	Cholesterol: serum cholesterol [mm/dl]
6.	FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]
7.	RestingECG: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria]
8.	MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]
9.	ExerciseAngina: exercise-induced angina [Y: Yes, N: No]
10.	Oldpeak: oldpeak = ST [Numeric value measured in depression]
11.	ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]
12.	HeartDisease: output class [1: heart disease, 0: Normal]

#Pre Process:  

Pandas, numpy, matplotlib and scikitlearn are used to pre process the data.  

#Model Training:  

Model is trained with RandomForestClassifier. And classify situation as “heart disease” or “not heart disease”  

#Deployment:  

model is deployed with flask frame work.Open web browser and go to http://127.0.0.1:5000/ to access Heart Disease Prediction App.  

#Further Scope:  

Model can be upgraded as it could return prediction in percentage. 




