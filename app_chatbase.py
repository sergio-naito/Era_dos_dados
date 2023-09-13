# Importação dos módulos e classes necessários
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import ChatMessage
import streamlit as st

#from dotenv import load_dotenv 
import streamlit.components.v1 as stc

#load_dotenv()
#openai_api_key = os.environ.get("key_api")


# Define uma classe de callback personalizada que estende a classe BaseCallbackHandler
class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    # Este método é chamado sempre que um novo token é gerado pelo modelo de linguagem
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)
        
        
HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">A Era Do Cientista de Dados</h1>
    </div>
    """

def main():

    stc.html(HTML_BANNER)

    # Cria uma barra lateral na aplicação Streamlit para inserir a chave da API da OpenAI
    with st.sidebar:
        openai_api_key = st.text_input("Adicione a Chave da API da OpenAI", type="password")
        

    # Se a chave "messages" não estiver presente no estado da sessão, inicializa com uma mensagem padrão do assistente
    if "messages" not in st.session_state:
        st.session_state["messages"] = [ChatMessage(role="assistant", content="Bem vindo? Como posso ajudar?")]
    
    # Exibe as mensagens do chat armazenadas no estado da sessão
    for msg in st.session_state.messages:
        st.chat_message(msg.role).write(msg.content)

    # Verifica se o usuário inseriu uma nova mensagem
    if prompt := st.chat_input():
        # Adiciona a mensagem do usuário ao estado da sessão
       
        st.session_state.messages.append(ChatMessage(role="user", content=prompt))
        st.chat_message("user").write(prompt)

        # Se a chave da API da OpenAI não foi fornecida, exibe uma mensagem informativa e interrompe
        if not openai_api_key:
            st.info("Gentileza, adicione sua chave da API da OpenAI para continuar.")
            st.stop()

        # Gera uma resposta usando o modelo de linguagem e exibe como mensagem do assistente
        with st.chat_message("assistant"):
            # Cria uma instância de StreamHandler para lidar com atualizações em tempo real da resposta do assistente
            stream_handler = StreamHandler(st.empty())
            
            # Inicializa o modelo ChatOpenAI com a chave da API fornecida e o modo de streaming
            llm = ChatOpenAI(openai_api_key=openai_api_key, streaming=True, callbacks=[stream_handler])
            
            # Gera uma resposta usando o modelo de linguagem e adiciona ao estado da sessão
            response = llm(st.session_state.messages)
            st.session_state.messages.append(ChatMessage(role="assistant", content=response.content))

    st.write('teste de inclusão do chatbase')