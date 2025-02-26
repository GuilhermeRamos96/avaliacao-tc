import streamlit as st

def avaliar_fratura():
    st.subheader("Avaliação de Fratura Facial")
    
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
        if positivos > 0:
            recomendacao = """✅ Tomografia Recomendada  
            
            **Referências:**  
            1- STEWART, Christopher N. et al. Validation of the “Wisconsin Criteria” for Obtaining Dedicated Facial Imaging and Its Financial Impact at a Level 1 Trauma Center. Craniomaxillofacial Trauma & Reconstruction, v. 13, n. 1, p. 4-8, mar. 2020. http://dx.doi.org/10.1177/1943387520910020.  
            2- HARRINGTON, Amanda W. et al. External Validation of University of Wisconsin's Clinical Criteria for Obtaining Maxillofacial Computed Tomography in Trauma. Journal Of Craniofacial Surgery, v. 29, n. 2, p. 1-4, mar. 2018. http://dx.doi.org/10.1097/scs.0000000000004240."""
        else:
            recomendacao = """❌ Nenhuma indicação clara de TC  
            
            **Referências:**  
            1- STEWART, Christopher N. et al. Validation of the “Wisconsin Criteria” for Obtaining Dedicated Facial Imaging and Its Financial Impact at a Level 1 Trauma Center. Craniomaxillofacial Trauma & Reconstruction, v. 13, n. 1, p. 4-8, mar. 2020. http://dx.doi.org/10.1177/1943387520910020.  
            2- HARRINGTON, Amanda W. et al. External Validation of University of Wisconsin's Clinical Criteria for Obtaining Maxillofacial Computed Tomography in Trauma. Journal Of Craniofacial Surgery, v. 29, n. 2, p. 1-4, mar. 2018. http://dx.doi.org/10.1097/scs.0000000000004240."""
        
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
            "Edema facial progressivo": st.checkbox("Edema facial progressivo"),
            "Leucocitose": st.checkbox("Leucocitose")
        }
    
    with st.expander("Critérios de Baixo Risco"):
        baixo_risco = {
            "Infecção no espaço bucal": st.checkbox("Infecção no espaço bucal"),
            "Infecção vestibular isolada": st.checkbox("Infecção vestibular isolada")
        }

    if st.button("Calcular Resultado"):
        if any(alto_risco.values()):
            resultado = """🔥 Tomografia recomendada: Critérios de alto risco presentes.  
            
            **Referências:**  
            1- WEYH, Ashleigh et al. Overutilization of Computed Tomography for Odontogenic Infections. Journal Of Oral And Maxillofacial Surgery, v. 77, n. 3, p. 528-535, mar. 2019. http://dx.doi.org/10.1016/j.joms.2018.10.025.  
            2- CHRISTENSEN, Brian J. et al. Evidence-Based Clinical Criteria for Computed Tomography Imaging in Odontogenic Infections. Journal Of Oral And Maxillofacial Surgery, v. 77, n. 2, p. 299-306, fev. 2019. http://dx.doi.org/10.1016/j.joms.2018.09.022."""
        elif sum(moderado_risco.values()) > 1:
            resultado = """⚠️ Considerar Tomografia: Dois ou mais critérios de risco moderado presentes.  
            
            **Referências:**  
            1- WEYH, Ashleigh et al. Overutilization of Computed Tomography for Odontogenic Infections. Journal Of Oral And Maxillofacial Surgery, v. 77, n. 3, p. 528-535, mar. 2019. http://dx.doi.org/10.1016/j.joms.2018.10.025.  
            2- CHRISTENSEN, Brian J. et al. Evidence-Based Clinical Criteria for Computed Tomography Imaging in Odontogenic Infections. Journal Of Oral And Maxillofacial Surgery, v. 77, n. 2, p. 299-306, fev. 2019. http://dx.doi.org/10.1016/j.joms.2018.09.022."""
        else:
            resultado = """✅ Nenhuma indicação clara de TC. Monitorar evolução.
            
            **Referências:**  
            1- WEYH, Ashleigh et al. Overutilization of Computed Tomography for Odontogenic Infections. Journal Of Oral And Maxillofacial Surgery, v. 77, n. 3, p. 528-535, mar. 2019. http://dx.doi.org/10.1016/j.joms.2018.10.025.  
            2- CHRISTENSEN, Brian J. et al. Evidence-Based Clinical Criteria for Computed Tomography Imaging in Odontogenic Infections. Journal Of Oral And Maxillofacial Surgery, v. 77, n. 2, p. 299-306, fev. 2019. http://dx.doi.org/10.1016/j.joms.2018.09.022."""
        
        st.markdown(f"**🔍 {resultado}**")

# Interface Streamlit
st.title("🏥 **Avaliação da Necessidade de Tomografia**")
st.write("💡 *A decisão final deve ser do especialista.*")
st.write("👨‍⚕️ **Escolha a avaliação desejada:**")

opcao = st.radio("", ["Fratura Facial", "Infecção Odontogênica"])

if opcao == "Fratura Facial":
    avaliar_fratura()
elif opcao == "Infecção Odontogênica":
    avaliar_infeccao()
