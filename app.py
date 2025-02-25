import streamlit as st

def avaliar_fratura():
    st.subheader("Avaliação de Fratura Facial - Stewart(2020), Carvalho et al(2019)")
    
    with st.expander("Wisconsin Criteria"):
        criterios = {
            "Degrau ósseo ou instabilidade": st.checkbox("Degrau ósseo ou instabilidade"),
            "Equimose periorbital": st.checkbox("Equimose periorbital"),
            "GCS < 14": st.checkbox("Escala de Coma de Glasgow < 14"),
            "Má oclusão": st.checkbox("Má oclusão"),
            "Ausência dentária": st.checkbox("Ausência dentária")
        }
    
    if st.button("Calcular Resultado"):
        positivos = sum(criterios.values())
        recomendacao = "✅ Tomografia Recomendada
        Referências: Stewart(2020), Carvalho et al(2019)" 
        if positivos > 0 else "❌ Nenhuma indicação clara de TC
         Referências: Stewart(2020), Carvalho et al(2019)"
        
        st.markdown(f"**📊 Critérios preenchidos:** {positivos}/5")
        st.markdown(f"**🔍 {recomendacao}**")

def avaliar_infeccao():
    st.subheader("Avaliação de Infecção Odontogênica")
    
    with st.expander("Critérios de Alto Risco"):
        alto_risco = {
            "Disfagia/Odinofagia": st.checkbox("Disfagia/Odinofagia"),
            "Elevação do assoalho da boca": st.checkbox("Elevação do assoalho da boca"),
            "Trismo < 25mm": st.checkbox("Trismo (<25 mm)"),
            "Perda da definição do bordo inferior da mandíbula": st.checkbox("Perda da definição do bordo inferior da mandíbula"),
            "Infecção submandibular": st.checkbox("Infecção submandibular"),
            "Infecção pterigomandibular": st.checkbox("Infecção pterigomandibular"),
            "Infecção faríngea lateral": st.checkbox("Infecção faríngea lateral")
        }
    
    with st.expander("Critérios de Risco Moderado"):
        moderado_risco = {
            "Linfadenopatia cervical": st.checkbox("Linfadenopatia cervical"),
            "Taquicardia": st.checkbox("Taquicardia"),
            "Edema facial progressivo": st.checkbox("Edema facial progressivo")
        }
    
    with st.expander("Critérios de Baixo Risco"):
        baixo_risco = {
            "Infecção no espaço bucal": st.checkbox("Infecção no espaço bucal"),
            "Infecção vestibular isolada": st.checkbox("Infecção vestibular isolada")
        }

    if st.button("Calcular Resultado"):
        if any(alto_risco.values()):
            resultado = "🔥 Tomografia recomendada: Critérios de alto risco presentes.
            Referências: Weyh et al (2019), Christensen et al (2018), Saggese (2019) "
        elif sum(moderado_risco.values()) > 1:
            resultado = "⚠️ Considerar Tomografia: Dois ou mais critérios de risco moderado presentes.
            Referências:Weyh et al (2019), Christensen et al (2018), Saggese (2019)"
        else:
            resultado = "✅ Nenhuma indicação clara de TC. Monitorar evolução.
            Referências:Weyh et al (2019), Christensen et al (2018), Saggese (2019)"
        
        st.markdown(f"**🔍 {resultado}**")

# Interface Streamlit
st.title("🏥 Avaliação de Tomografia")
st.write("Escolha a avaliação desejada:")

opcao = st.radio("", ["Fratura Facial", "Infecção Odontogênica"])

if opcao == "Fratura Facial":
    avaliar_fratura()
elif opcao == "Infecção Odontogênica":
    avaliar_infeccao()
