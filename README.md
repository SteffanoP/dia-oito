# 🚲 O Dia 8 de Dezembro de 2019 ❤️

Uma aplicação Streamlit que conta a história especial do dia 8 de dezembro de 2019, quando Steffano e Helena tiveram um encontro inesquecível no Recife. A aplicação usa IA do Google Gemini para responder perguntas sobre essa aventura romântica.

## 📖 Sobre

Esta aplicação utiliza um assistente de IA treinado especificamente para contar a história do dia 8 de dezembro de 2019. O assistente pode responder perguntas sobre:

- 🚲 A aventura de bicicleta do Marco Zero até Boa Viagem
- 🍹 Os sucos especiais do Gelatto's
- 🚗 A luta épica com o fusca no Parque Dona Lindu
- 🏖️ O banho de mar em Piedade e Boa Viagem
- ❤️ Como começou uma grande história de amor

## 🛠️ Tecnologias Utilizadas

- **Streamlit** - Interface web interativa
- **Google Gemini AI** - Assistente inteligente
- **Python** - Linguagem de programação
- **PIL (Pillow)** - Processamento de imagens

## 🚀 Como Executar Localmente

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/dia-oito.git
cd dia-oito
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure a API Key do Google AI
1. Obtenha uma API key do Google AI Studio: https://makersuite.google.com/app/apikey
2. Edite o arquivo `.streamlit/secrets.toml`:
```toml
GOOGLE_AI_API_KEY = "sua-api-key-aqui"
```

### 4. Execute a aplicação
```bash
streamlit run streamlit_app.py
```

## 🌐 Deploy no Streamlit Community Cloud

### 1. Preparação
1. Faça um fork deste repositório
2. Certifique-se de que todos os arquivos estão commitados (exceto secrets.toml)

### 2. Deploy
1. Acesse [share.streamlit.io](https://share.streamlit.io)
2. Conecte sua conta GitHub
3. Selecione o repositório `dia-oito`
4. Defina o arquivo principal como `streamlit_app.py`

### 3. Configure os Secrets
1. No painel do Streamlit Cloud, vá em "Secrets"
2. Adicione a seguinte configuração:
```toml
GOOGLE_AI_API_KEY = "sua-api-key-do-google-ai"
```

## 📁 Estrutura do Projeto

```
dia-oito/
├── streamlit_app.py          # Aplicação principal
├── context.py                # Contexto da história
├── requirements.txt          # Dependências Python
├── .streamlit/
│   └── secrets.toml         # Configurações secretas (local)
├── data/
│   └── img/
│       ├── luta-fusca.jpg   # Foto da luta com o fusca
│       └── igrejinha-piedade.jpg  # Foto na igrejinha
└── README.md                # Este arquivo
```

## 🎯 Funcionalidades

### Chat Interativo
- Faça perguntas sobre qualquer aspecto do dia 8 de dezembro
- Assistente especializado na história com persona definida
- Respostas em português brasileiro com emojis

### Galeria de Fotos
- Visualize as fotos históricas do dia
- Luta épica com o fusca no Parque Dona Lindu
- Foto na igrejinha de Piedade

### Cronologia Interativa
- Timeline completa dos eventos do dia
- Horários e locais visitados
- Sabores e experiências especiais

## 🤖 Engenharia de Prompt

O assistente utiliza uma estrutura de prompt bem definida:

- **Persona**: Assistente carismático, nostálgico e envolvente
- **Task**: Explicar e narrar os eventos do dia 8 de dezembro de 2019
- **Context**: História completa fornecida do arquivo context.py
- **Format**: Respostas em português brasileiro, estruturadas e emotivas

## 🔐 Segurança

- API keys são gerenciadas através do sistema de secrets do Streamlit
- Arquivo secrets.toml está no .gitignore para evitar commits acidentais
- Suporte tanto para secrets do Streamlit quanto variáveis de ambiente

## 📝 Exemplos de Perguntas

- "O que aconteceu no Gelatto's?"
- "Conta sobre a luta com o fusca"
- "Como foi o banho de mar em Piedade?"
- "Que horas eles se encontraram?"
- "Por que essa data é especial?"

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é uma história pessoal e está compartilhado para fins educacionais e demonstrativos.

---

*"Ali então começou de fato uma grande história de amor..."* ❤️