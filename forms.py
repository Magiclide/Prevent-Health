from flask_wtf import FlaskForm
from wtforms import (IntegerField, SelectField, StringField, SubmitField,FloatField,
                     validators)
from wtforms.validators import DataRequired, Length


class predictsForms(FlaskForm):
    nome=StringField('nome',validators=[DataRequired("Por favor digite o nome")])
    genero=SelectField('genero', choices=[("0", "Masculino"), ("1", "Feminino")],validators=[DataRequired("Por favor selecione uma opção")])
    idade=IntegerField('idade',validators=[DataRequired("Por favor digite uma idade"),validators.NumberRange(min=0,max=130,message="Idade invalida")])
    grau_escolaridade=SelectField('grau_escolaridade',choices=[("0", "Sem estudo"), ("1", "Ensino fundamental completo"),("2", "Ensino médio completo"),("3", "Ensino superior completo"),("4", "Mestrado completo"),("5", "Doutorado completo")],validators=[DataRequired("Por favor selecione uma opção")])
    hipertensao=SelectField('hipertensao', choices=[("0", "Possuo"), ("1", "Não Possuo"),("2", "Não sei")], validators=[DataRequired("Por favor selecione uma opção")])
    dislipidemia=SelectField('dislipidemia', choices=[("0", "Possuo"), ("1", "Não Possuo"),("0", "Não sei")], validators=[DataRequired("Por favor selecione uma opção")])
    atividade_fisica=SelectField('atividade_fisica', choices=[("0", "Zero"), ("1", "Uma"),("2", "Duas"),("3", "Tres"),("4", "Quatro"),("5", "Cinco"),("6", "Seis"),("7", "Sete")],validators=[DataRequired("Por favor selecione uma opção")])
    peso=FloatField('peso',validators=[DataRequired("Por favor digite um peso"),validators.NumberRange(min=0,max=400,message="Peso Invalido")])
    altura=IntegerField('altura',validators=[DataRequired("Por favor digite uma altura"),validators.NumberRange(min=50,max=250,message="Altura Invalida")])
    





