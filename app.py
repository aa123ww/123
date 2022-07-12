from flask import Flask,render_template
from flask_script import Manager
from settings import DevelopmentConfig

app = Flask(__name__)
manager = Manager(app)

app.config.from_object(DevelopmentConfig)

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/Introduction.html')
def Introduction():
    return render_template('Introduction.html')



@app.route('/Prediction-Model.html')
def PredictionModel():
    return render_template('Prediction-Model.html')


@app.route('/Data-Exploration.html')
def DataExplorationn():
    return render_template('Data-Exploration.html')


@app.route('/Evaluation-and--Conclusion.html')
def EvaluationandConclusion():
    return render_template('Evaluation-and--Conclusion.html')


@app.route('/Data-Preparation.html')
def DataPreparation():
    return render_template('Data-Preparation.html')





if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
