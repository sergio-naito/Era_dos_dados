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

    ##s Cria uma barra lateral na aplicação Streamlit para inserir a chave da API da OpenAI
    ##swith st.sidebar:
    ##s    openai_api_key = st.text_input("Adicione a Chave da API da OpenAI", type="password")
        

    ##s Se a chave "messages" não estiver presente no estado da sessão, inicializa com uma mensagem padrão do assistente
    ##sif "messages" not in st.session_state:
    ##s    st.session_state["messages"] = [ChatMessage(role="assistant", content="Bem vindo? Como posso ajudar?")]
    ##s
    ##s Exibe as mensagens do chat armazenadas no estado da sessão
    ##sfor msg in st.session_state.messages:
    ##s    st.chat_message(msg.role).write(msg.content)

    ##s Verifica se o usuário inseriu uma nova mensagem
    ##sif prompt := st.chat_input():
    ##s    # Adiciona a mensagem do usuário ao estado da sessão
       
    ##s    st.session_state.messages.append(ChatMessage(role="user", content=prompt))
    ##s    st.chat_message("user").write(prompt)

    ##s    # Se a chave da API da OpenAI não foi fornecida, exibe uma mensagem informativa e interrompe
    ##s    if not openai_api_key:
    ##s        st.info("Gentileza, adicione sua chave da API da OpenAI para continuar.")
    ##s        st.stop()

    ##s    # Gera uma resposta usando o modelo de linguagem e exibe como mensagem do assistente
    ##s    with st.chat_message("assistant"):
    ##s        # Cria uma instância de StreamHandler para lidar com atualizações em tempo real da resposta do assistente
    ##s        stream_handler = StreamHandler(st.empty())
    ##s        
    ##s        # Inicializa o modelo ChatOpenAI com a chave da API fornecida e o modo de streaming
    ##s        llm = ChatOpenAI(openai_api_key=openai_api_key, streaming=True, callbacks=[stream_handler])
    ##s        
    ##s        # Gera uma resposta usando o modelo de linguagem e adiciona ao estado da sessão
    ##s        response = llm(st.session_state.messages)
    ##s        st.session_state.messages.append(ChatMessage(role="assistant", content=response.content))

    st.write('teste de inclusão do chatbase')