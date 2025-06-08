import streamlit as st

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Quicksand&display=swap" rel="stylesheet">
    <style>
        .stApp {
            color: #4B0082;
            font-family: 'Quicksand', sans-serif;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center; /* Centraliza todo o texto diretamente no container principal */
            width: 100%;
        }

        .extrato-line {
            text-align: center;
            margin-bottom: 5px; /* Espaçamento entre as linhas do extrato */
        }

        .stNumberInput label {
            display: block;
            text-align: center;
            width: 100%;
        }

        .stNumberInput {
            width: 300px;
            margin: auto;
        }

        div.stButton > button {
            display: flex;
            margin-left: auto;
            margin-right: auto;
            background-color: #A678F2;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 10px;
            width: 200px;
            height: 40px;
            margin-top: 10px;
            transition: 0.3s;
        }

        div.stButton > button:hover {
            background-color: #8B5FBF;
            cursor: pointer;
        }
        
        .stSidebar {
            background-color: #E6E6FA;
        }
    </style>
""", unsafe_allow_html=True)


if "saldo" not in st.session_state:
    st.session_state.saldo = 0.0
    st.session_state.extrato = ""
    st.session_state.quantidade_saques = 0

    st.session_state.operacao_selecionada = None

LIMITE_SAQUE = 500
LIMITE_SAQUES_DIARIOS = 3


col1, col2, col3 = st.columns([0.5, 6, 0.5])
with col2:
    st.title("💸 Sistema Bancário V1 💸")
    st.subheader("Seja bem vindo(a) ao nosso Banco! 💜")

st.sidebar.title("✨ Menu de Operações ✨")
operacao_selecionada = st.sidebar.radio(
    "Escolha a operação desejada:",
    ["Depósito", "Saque", "Extrato"],
    index=None,
    key="sidebar_radio"
)

if operacao_selecionada:
    st.session_state.operacao_selecionada = operacao_selecionada

main_col1, main_col2, main_col3 = st.columns([1, 4, 1])

if st.session_state.operacao_selecionada:
    with main_col2:
        if st.session_state.operacao_selecionada == "Depósito":
            st.header("💰 Depósito")
            valor = st.number_input("Digite o valor do depósito:", min_value=0.01, step=0.01, key="deposito_valor")
            if st.button("Depositar", key="btn_depositar"):
                st.session_state.saldo += valor
                st.session_state.extrato += f"💰 Depósito: R$ {valor:.2f}\n"
                st.success(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

        elif st.session_state.operacao_selecionada == "Saque":
            st.header("🏧 Saque")
            valor = st.number_input("Digite o valor do saque:", min_value=0.01, step=0.01, key="saque_valor")
            if st.button("Sacar", key="btn_sacar"):
                if valor > st.session_state.saldo:
                    st.error("Saldo insuficiente.")
                elif valor > LIMITE_SAQUE:
                    st.error(f"Valor excede o limite de R$ {LIMITE_SAQUE:.2f}.")
                elif st.session_state.quantidade_saques >= LIMITE_SAQUES_DIARIOS:
                    st.error("Limite de 3 saques diários atingido.")
                else:
                    st.session_state.saldo -= valor
                    st.session_state.extrato += f"🏧 Saque: R$ {valor:.2f}\n"
                    st.session_state.quantidade_saques += 1
                    st.success(f"Saque de R$ {valor:.2f} realizado com sucesso!")

        elif st.session_state.operacao_selecionada == "Extrato":
            st.header("📋 Extrato")
            if st.session_state.extrato:
                for line in st.session_state.extrato.split('\n'):
                    if line.strip():
                        st.markdown(f'<div class="extrato-line">{line}</div>', unsafe_allow_html=True)
            else:
                st.info("Nenhuma movimentação registrada.")
            
            st.divider()

            st.markdown(f'<div class="extrato-line">Saldo atual: R$ {st.session_state.saldo:.2f}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="extrato-line">Saques hoje: {st.session_state.quantidade_saques} / {LIMITE_SAQUES_DIARIOS}</div>', unsafe_allow_html=True)

else:
    with main_col2:
        st.markdown("Acesse o **Menu de Operações** na barra lateral para utilizar as funções de Depósito, Saque e Extrato.")

st.markdown("---")
st.caption("2025 - Desenvolvido por Beatriz Celestino / Desafio de Projeto: Sistema Bancário (Bootcamp Suzano Python Developer).")