import json

import joblib
import numpy as np
import pandas as pd
from flask import Flask, jsonify, render_template, request, url_for
from flask_wtf import CSRFProtect

from forms import predictsForms

app = Flask(__name__)
csrf = CSRFProtect(app)  
app.config['SECRET_KEY'] = '1234'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/diabetes')
def diabetes():
    return render_template('diabetes.html')

@app.route('/prever', methods=['POST'])
def prever():
    dados_de_entrada = request.json  # Obter dados de entrada da requisição POST
    print(dados_de_entrada);
    resultado = fazer_previsao(dados_de_entrada)
    
    return jsonify({'resultado': resultado.tolist()})

@app.route('/home2')
def home2():
    form = predictsForms();
    
    return render_template('teste2.html',form=form)

@app.route('/teste')
def teste():
    return render_template('teste.html')

def fazer_previsao(dados_de_entrada, nome):
    print("Seu nome: ",nome);
    input_data = np.array(dados_de_entrada)
    print(input_data)
    # Carregar o modelo treinado
    modelo = joblib.load('D:\\Desktop\\apiMestrado\\modelFiles\\diabetes.pkl')  # Se estiver usando scikit-learn
    
    # Fazer previsões usando o modelo
    previsao = modelo.predict_proba(input_data)
    print(previsao)

# Apply the threshold to the predicted probabilities
    second_value = previsao[0, 0]
    float_str=str(second_value*100)
    integer_part, decimal_part = float_str.split('.')
    first_two_decimal_digits = decimal_part[:2]
    print(f" Voce tem: {integer_part}.{first_two_decimal_digits} %  de chance de ser um fudido")
    

@app.route('/submit_form', methods=['POST'])
def submit_form():
    form = predictsForms(request.form)  # Create an instance of your form class

    if form.validate():
            nome = form.nome.data
            genero = form.genero.data
            idade = form.idade.data  # Convert to float
            grau_escolaridade = form.grau_escolaridade.data  # Convert to float
            hipertensao = form.hipertensao.data
            if hipertensao in ["0", "2"]:
                hipertensao = "0"
            #hipertensao = hipertensao  # Convert to float
            dislipidemia = form.dislipidemia.data
            if dislipidemia in ["0", "2"]:
                 dislipidemia = "0"
            #dislipidemia = dislipidemia  # Convert to float
            atividade_fisica = form.atividade_fisica.data  # Convert to float
            peso = form.peso.data # Convert to float
            altura = form.altura.data
            alturaMetros=altura/100
            IMC = peso/(alturaMetros*alturaMetros)
            IMC_formatado = round(IMC, 2)
            result =pd.DataFrame([{
                'Gênero': genero,
                'Idade': idade,
                'Grau de escolaridade': grau_escolaridade,
                'Dislipidemia': dislipidemia,
                'Hipertensão': hipertensao,
                'Atividade Física': atividade_fisica,
                'Peso': peso,
                'Altura': altura,
                'IMC': IMC_formatado
   }])

            
            result2= fazer_previsao(result ,nome);
            return result.to_html();
    else:
        errors = form.errors
        return jsonify({"form_errors": errors})
