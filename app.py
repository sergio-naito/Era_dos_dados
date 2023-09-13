
import streamlit as st
import style as style
from streamlit_option_menu import option_menu
import app_chat
import app_home


st.set_page_config(  # Alternate names: setup_page, page, layout
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
    initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
    page_title="Chat",  # String or None. Strings get appended with "• Streamlit". 
    page_icon= '',  # String, anything supported by st.image, or None.
)


#carrega os arquivos css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
    
def main():
    
       #esconder botão de menu e marca dágua no rodapé
    style.hidden_menu_and_footer()
        #cabeçalho detalhe superior da página 
    style.headerstyle()
    
    style.div()
    
    pages={
        "ChatGPT":page_chat,
        "Conjunto de dados":page_analise,
        "Home":home
            
        }
    
    with st.sidebar:
            style.sidebarwidth() 
            page = option_menu('Menu', ["Home","ChatGPT"],
                                    icons=['house','bullseye'],
                                    default_index=0, menu_icon="app-indicator",   #orientation='horizontal',
                                ) 

    pages[page]()
   
    
    with st.sidebar.expander('Sobre'):
            # Mostrar versões das bibliotecas
            #st.write(os.popen(f'python --version').read())
            #st.write('Streamlit:', st.__version__)
            #st.write('Pandas:', pd.__version__)
            #st.write('yfinance:', yf.__version__)
            #st.write('plotly:', plotly.__version__)
            #st.write('Fundamentus:', fundamentus.__version__)
            st.write('Feito com Carinho ')
            st.markdown("- Roberto Carlos Ricci") 

def home():
    app_home.home()  
           
def page_chat():
     app_chat.main()  

def page_chatbase():
     app_chatbase.main()  

def page_analise():
     #app_home.home()
     st.write('Feito com Carinho ')
    
if __name__ == "__main__":
    main()