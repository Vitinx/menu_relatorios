import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Relatórios Wyntech", layout="wide")

# Dicionário com os relatórios disponíveis
relatorios = {
    "Dashboard SLA": "https://app.powerbi.com/reportEmbed?reportId=caed6072-da16-40e0-ac50-ce254ceafb14&autoAuth=true&ctid=afeff2ce-6c03-41a8-b6fd-da922bf0c5ec",
    "Dashboard Combustível": "https://app.powerbi.com/reportEmbed?reportId=22780b5a-a09d-41b0-ae53-12cbcec70add&autoAuth=true&ctid=afeff2ce-6c03-41a8-b6fd-da922bf0c5ec",
    "Dashboard Faturamento Positivo": "https://app.powerbi.com/reportEmbed?reportId=af1f8943-33cb-4830-b85b-fc4bf3048a8b&autoAuth=true&ctid=afeff2ce-6c03-41a8-b6fd-da922bf0c5ec"
}

# Adicionando a opção inicial "Selecione um relatório"
opcoes_menu = ["Selecione um relatório"] + list(relatorios.keys())

# Criando o menu lateral
escolha = st.sidebar.selectbox("Escolha um relatório:", opcoes_menu)

# Atualiza o título conforme a escolha
if escolha == "Selecione um relatório":
    st.title("📊 Relatórios Wyntech")
    st.write("Selecione um relatório no menu lateral para visualizar.")
else:
    st.title(f"📊 {escolha}")
    # Exibir o relatório correspondente
    st.markdown(
        f'<iframe title="{escolha}" width="100%" height="800" src="{relatorios[escolha]}" frameborder="0" allowFullScreen="true"></iframe>',
        unsafe_allow_html=True
    )