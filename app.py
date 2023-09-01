import streamlit as st
import pandas as pd
import datetime

def main():
    st.markdown("# Formulários do Streamlit")
    menu = ["Home","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "Home":
        st.subheader("Formulários & Calculadora de Salário")
        
        # Salary Calculator
        # Combine forms + columns
        resultados = []
        with st.form(key='salaryform'):
            col1,col2 = st.columns([2,1])
            
            with col1:
                amount = st.number_input("Pago em hora (R$):")
                
            with col2:
                hour_per_week = st.number_input("Horas por semana",1,120)
            
            calculo_salario = st.form_submit_button(label='Calcular')
        
            st.write("Trabalhou {} horas".format(amount * hour_per_week))
                
            if calculo_salario: 
                diariamente = [amount * 8]
                semanal = [amount * hour_per_week]
                resultados.append({'Por hora':amount,'Diariamente':diariamente,'Semanal':semanal})
            
        # Exibir todos os resultados acumulados
        with st.expander("Resultados"):
            for i, resultado in enumerate(resultados):
                df = pd.DataFrame([resultado])  # Converter o resultado em um dataframe
                st.write(f"Resultado {i+1}:")
                st.dataframe(df)
                 
        # Metodo 1: Context Manager Approach (with) 
        with st.form(key='form1'):
            firstname = st.text_input("Primeiro Nome")
            lastname = st.text_input("Último nome")
            min_date = datetime.date(1923,1,1)
            max_date = datetime.date.today()
            niver = st.date_input(f"Data de Nascimento",min_value=min_date,max_value=max_date, format="DD/MM/YYYY")
            
            #Importante!
            submit_button = st.form_submit_button(label="Acessar")
        
        # Os resultados podem ser de formulários ou exibidos fora
        if submit_button:
            st.success("Olá {}, você criou uma conta!".format(firstname))
        
        # Método 2:
        form2 = st.form(key='form2')
        username = form2.text_input("Username")
        jobtype = form2.selectbox("Emprego:",["Developer","Data Scientist","Analyst"])
        submit_button2 = form2.form_submit_button("Login")
        
        if submit_button2:
            st.success("Usuário {} logado com sucesso.".format(username))
        
    else:
        st.subheader("About")
        
if __name__ == '__main__':
    main()