import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
import re

# Set page config
st.set_page_config(
    page_title="Dia 8",
    page_icon="🚲",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1E88E5;
        margin-bottom: 2rem;
    }
    .story-container {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .assistant-response {
        background-color: #e3f2fd;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1E88E5;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize the context from context.py
@st.cache_data
def load_context():
    with open('context.py', 'r', encoding='utf-8') as file:
        content = file.read()
        # Extract the context string
        start = content.find('"""') + 3
        end = content.rfind('"""')
        return content[start:end]

# Configure Gemini AI
def configure_gemini():
    try:
        # Try to get API key from Streamlit secrets
        api_key = st.secrets.get("GOOGLE_AI_API_KEY")
        if not api_key:
            # Fallback to environment variable
            api_key = os.getenv("GOOGLE_AI_API_KEY")
        
        if api_key:
            genai.configure(api_key=api_key)
            return True
        else:
            st.error("❌ Google AI API Key não encontrada. Configure a chave em secrets.toml ou como variável de ambiente.")
            return False
    except Exception as e:
        st.error(f"❌ Erro ao configurar Gemini AI: {str(e)}")
        return False

# Create the AI assistant
def create_assistant(context):
    """Create a Gemini AI assistant with the specific context about December 8th"""
    
    persona = """Você é um assistente especialista em contar a história romântica e aventureira 
    do dia 8 de dezembro de 2019, quando Steffano e Helena tiveram seu primeiro encontro especial 
    no Recife. Você é carismático, nostálgico e tem um jeito envolvente de narrar histórias."""
    
    task = """Sua tarefa é explicar, narrar e responder perguntas sobre os eventos que aconteceram 
    no dia 8 de dezembro de 2019 entre Steffano e Helena. Você deve ser informativo, mas também 
    emotivo e cativante ao contar a história."""
    
    format_instructions = """Responda sempre em português brasileiro, de forma clara e envolvente. 
    Use emojis quando apropriado para tornar a narrativa mais viva. Organize suas respostas de 
    forma estruturada quando necessário, mas mantenha um tom caloroso e pessoal."""
    
    full_prompt = f"""
    {persona}
    
    {task}
    
    CONTEXTO DA HISTÓRIA:
    {context}
    
    {format_instructions}
    
    Responda à seguinte pergunta sobre o dia 8 de dezembro de 2019:
    """
    
    return full_prompt

def convert_markdown_images_to_streamlit(text):
    """Convert markdown images ![alt](url) to st.image() calls"""
    # Pattern to match markdown images: ![alt text](image_url)
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    
    def replace_image(match):
        alt_text = match.group(1)
        image_url = match.group(2)
        # Return a placeholder that we'll handle separately
        return f"__STREAMLIT_IMAGE__{image_url}__{alt_text}__"
    
    return re.sub(pattern, replace_image, text)

def display_content_with_images(content):
    """Display content and handle embedded images"""
    # Convert markdown images to placeholders
    processed_content = convert_markdown_images_to_streamlit(content)
    
    # Split by image placeholders
    parts = re.split(r'__STREAMLIT_IMAGE__([^_]+)__([^_]*)__', processed_content)
    
    for i in range(0, len(parts), 3):
        # Regular text part
        if parts[i].strip():
            st.markdown(parts[i])
        
        # Check if there's an image following
        if i + 1 < len(parts) and i + 2 < len(parts):
            image_url = parts[i + 1]
            caption = parts[i + 2]
            try:
                st.image(image_url, caption=caption if caption else None)
            except Exception as e:
                st.error(f"Erro ao carregar imagem: {image_url}")

# Main app
def main():
    # Header
    st.markdown('<h1 class="main-header">🚲 Dia 8</h1>', unsafe_allow_html=True)
    
    # Configure Gemini
    if not configure_gemini():
        st.stop()
    
    # Load context
    context = load_context()
    
    # Chat interface
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("🤖 Pergunte ao Assistente sobre o Dia 8"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate AI response
        with st.chat_message("assistant"):
            with st.spinner("Pensando na resposta..."):
                try:
                    model = genai.GenerativeModel('gemini-2.5-flash-preview-04-17')
                    full_prompt = create_assistant(context) + prompt
                    response = model.generate_content(full_prompt)
                    
                    if response.text:
                        display_content_with_images(response.text)
                        # Add assistant response to chat history
                        st.session_state.messages.append({"role": "assistant", "content": response.text})
                    else:
                        st.error("Desculpe, não consegui gerar uma resposta. Tente novamente.")
                except Exception as e:
                    st.error(f"Erro ao gerar resposta: {str(e)}")

if __name__ == "__main__":
    main()
