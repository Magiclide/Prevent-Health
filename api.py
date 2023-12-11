import json

import joblib
import numpy as np
import pandas as pd
from azureml.core import Workspace
from azureml.core.authentication import ServicePrincipalAuthentication
from azureml.core.model import Model
from flask import Flask, jsonify, render_template, request, url_for
from flask_wtf import CSRFProtect

from forms import predictsForms
from formsDislipidemia import predictsFormsDis
from formsHipertensao import predictsFormsHip

app = Flask(__name__)
csrf = CSRFProtect(app)  
app.config['SECRET_KEY'] = '1234'


def get_workspace_and_model_path():
   svc_pr = ServicePrincipalAuthentication(
    tenant_id="db63730b-8f3b-41a1-aad1-cfe7379dea09",
    service_principal_id="7694deb8-d90e-4c16-9980-ea394e64e8e4",
    service_principal_password="LgY8Q~cVuvdkTWA_YULDdlsgGsiI4zTb3Gnkmasj")

   ws = Workspace.get(
    name="PreventHealthModel",
    subscription_id="db63730b-8f3b-41a1-aad1-cfe7379dea09",
    resource_group="appsvc_linux_centralusp",
    auth=svc_pr)

   model_path = Model.get_model_path('diabetes', _workspace=ws)
   return model_path



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/diabetes')
def diabetes():
    form = predictsForms();
    return render_template('diabetes2.html',form=form)

@app.route('/hipertensao')
def hipertensao():
    form = predictsFormsHip();
    return render_template('hipertensao.html',form=form)

@app.route('/dislipidemia')
def dislipidemia():
    form = predictsFormsDis();
    return render_template('dislipidemia.html',form=form)        

@app.route('/prever', methods=['POST'])
def prever():
    dados_de_entrada = request.json  
    print(dados_de_entrada);
    resultado = fazer_previsao(dados_de_entrada)
    
    return jsonify({'resultado': resultado.tolist()})


def fazer_previsao(dados_de_entrada):
    model_path=get_workspace_and_model_path()
    input_data = np.array(dados_de_entrada)
    print(input_data)
    if('diabetes' not in dados_de_entrada.columns):
        modelo = joblib.load(model_path)
        previsao = modelo.predict_proba(input_data)
    elif('hipertensao' not in dados_de_entrada.columns):
        modelo = joblib.load('D:\\Desktop\\apiMestrado\\modelFiles\\hipertensao.pkl') 
        previsao = modelo.predict_proba(input_data)
    elif('dislipidemia' not in dados_de_entrada.columns):
        modelo = joblib.load('D:\\Desktop\\apiMestrado\\modelFiles\\dislipidemia.pkl') 
        previsao = modelo.predict_proba(input_data)

    second_value = previsao[0, 0]
    float_str=str(second_value*100)
    integer_part, decimal_part = float_str.split('.')
    first_two_decimal_digits = decimal_part[:2]
    return integer_part, first_two_decimal_digits
"""
def fazer_previsao_hip(dados_de_entrada):
  
    input_data = np.array(dados_de_entrada)
    print(input_data)
    
    modelo = joblib.load('D:\\Desktop\\apiMestrado\\modelFiles\\hipertensao.pkl')  
    
  
    previsao = modelo.predict_proba(input_data)
    

    print(previsao)
    second_value = previsao[0, 0]
    float_str=str(second_value*100)
    integer_part, decimal_part = float_str.split('.')
    first_two_decimal_digits = decimal_part[:2]
    return integer_part, first_two_decimal_digits    
"""
@app.route('/submit_form', methods=['POST'])
def submit_form():
    if('diabetes' not in request.form):
        form = predictsForms(request.form)  

        if form.validate():
                nome = form.nome.data
                genero = form.genero.data
                idade = form.idade.data 
                grau_escolaridade = form.grau_escolaridade.data 
                hipertensao = form.hipertensao.data
                if hipertensao in ["0", "2"]:
                    hipertensao = "0"
                
                dislipidemia = form.dislipidemia.data
                if dislipidemia in ["0", "2"]:
                    dislipidemia = "0"
                
                atividade_fisica = form.atividade_fisica.data 
                peso = form.peso.data 
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

                
                integer_part, first_two_decimal_digits= fazer_previsao(result)
                return render_template('result.html', integer_part=integer_part, first_two_decimal_digits=first_two_decimal_digits,nome=nome,disease='diabetes')
        else:
            errors = form.errors
            return jsonify({"form_errors": errors})

    elif('hipertensao' not in request.form):
        form = predictsFormsHip(request.form)
        if form.validate():
            nome = form.nome.data
            genero = form.genero.data
            idade = form.idade.data 
            grau_escolaridade = form.grau_escolaridade.data 
            diabetes = form.diabetes.data
            if diabetes in ["0", "2"]:
               diabetes = "0"
                
            dislipidemia = form.dislipidemia.data
            if dislipidemia in ["0", "2"]:
                dislipidemia = "0"
                
            atividade_fisica = form.atividade_fisica.data 
            peso = form.peso.data 
            altura = form.altura.data
            alturaMetros=altura/100
            IMC = peso/(alturaMetros*alturaMetros)
            IMC_formatado = round(IMC, 2)
            result =pd.DataFrame([{
                'Gênero': genero,
                'Idade': idade,
                'Grau de escolaridade': grau_escolaridade,
                'Dislipidemia': dislipidemia,
                'diabetes': diabetes,
                'Atividade Física': atividade_fisica,
                'Peso': peso,
                'Altura': altura,
                'IMC': IMC_formatado
    }])

                
            integer_part, first_two_decimal_digits= fazer_previsao(result)
            return render_template('result.html', integer_part=integer_part, first_two_decimal_digits=first_two_decimal_digits,nome=nome,disease='hipertensao')
        else:
            errors = form.errors
            return jsonify({"form_errors": errors})
    elif('dislipidemia' not in request.form):
        form = predictsFormsHip(request.form)
        if form.validate():
            nome = form.nome.data
            genero = form.genero.data
            idade = form.idade.data 
            grau_escolaridade = form.grau_escolaridade.data 
            diabetes = form.diabetes.data
            if diabetes in ["0", "2"]:
               diabetes = "0"
                
            hipertensao = form.hipertensao.data
            if hipertensao in ["0", "2"]:
                hipertensao = "0"
                
            atividade_fisica = form.atividade_fisica.data 
            peso = form.peso.data 
            altura = form.altura.data
            alturaMetros=altura/100
            IMC = peso/(alturaMetros*alturaMetros)
            IMC_formatado = round(IMC, 2)
            result =pd.DataFrame([{
                'Gênero': genero,
                'Idade': idade,
                'Grau de escolaridade': grau_escolaridade,
                'hipertensao': hipertensao,
                'diabetes': diabetes,
                'Atividade Física': atividade_fisica,
                'Peso': peso,
                'Altura': altura,
                'IMC': IMC_formatado
    }])

                
            integer_part, first_two_decimal_digits= fazer_previsao(result)
            return render_template('result.html', integer_part=integer_part, first_two_decimal_digits=first_two_decimal_digits,nome=nome,disease='hipertensao')
        else:
            errors = form.errors
            return jsonify({"form_errors": errors})

        
'''{
  "appId": "7694deb8-d90e-4c16-9980-ea394e64e8e4",
  "displayName": "PreventHealth",
  "password": "LgY8Q~cVuvdkTWA_YULDdlsgGsiI4zTb3Gnkmasj",
  "tenant": "db63730b-8f3b-41a1-aad1-cfe7379dea09"
}'''

