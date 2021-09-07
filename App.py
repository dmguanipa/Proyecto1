import streamlit as st
import pandas as pd 
import lasio
st.title("Aplicacion para Registros de Pozos")
st.sidebar.title("Menu")
opciones_inicio=st.sidebar.radio("Seleccione una opcion",["Inicio",'Datos','Calculos'])

archivo_las=lasio.read('LGAE-040.las')
df=archivo_las.df()

if opciones_inicio=="Inicio":
	st.write("Ingreso al Inicio")
	st.write(df)

if opciones_inicio=="Datos":
	st.write("Ingreso al Datos")
	barra_deslizadora=st.slider('Seleccione un Valor',1,100,30)
	st.write("El valor seleccionado es",barra_deslizadora)
	ingreso_numero=st.number_input("Ingrese un valor",min_value=1.00,max_value=1000.00,value=300.00)
if opciones_inicio=="Calculos":
	st.write("Ingreso al Calculos")
	seleccion=st.selectbox('Seleecione una opcion',[1,2,3,'A'])
	check1=st.checkbox("Activar")
	#if check=True:
		#st.write('Check activo')
archivo_subido=st.sidebar.file_uploader("Cargar archivo excel",type=['.xls','xlsx'])

if archivo_subido is not None:
	df2=pd.read_excel(archivo_subido)
	st.write(df2)
	
