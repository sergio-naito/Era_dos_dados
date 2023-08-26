import streamlit as st



def home():
    
    st.title('Bem Vindo a Era dos Dados')

    col1, col2, col3 = st.columns([0.7,1,0.7])
    #col2.image('./imagen/analisequant_logo-removebg.png')

    st.markdown("<h2 style='text-align: center; color: rgb(74, 113, 152);'> Aplicativo de inteligência Artificial </h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: rgb(74, 113, 152)'>Bot ChatGPT Desenvolvido durante Treinamento A Era Do Cientista de Dados</h4>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: rgb(74, 113, 152)'></h5>", unsafe_allow_html=True)
    
    st.markdown("<h4 style='text-align: center; color: rgb(74, 113, 152)'><p> Quer saber mais ?  click no link  <a style='color:back;text-align:center;' href='https://cientistadedadosnapratica.com.br/aula1' target='_blank'>A Era dos Dados</a> </p></h4>", unsafe_allow_html=True)
    
    st.markdown("***")
    
    
    col1, col2, col3, col4, col5  = st.columns([0.1,1,0.01,1,0.1])
    #col2.image('chatGPT.jpg')
    