import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns 
import yfinance as yf
import datetime as dt

st.title("Indice Boursiers GAFAM")
with st.expander("Source"):
    st.write("Ces données sur les indices boursiers des GAFAM proviennent du site de trading Yahoo Finance. Elles sont actualisées de façon automatique tous les jours")



#Fonction statistique




#configuration des dates 
End_date = dt.datetime.now()
Start_date = End_date - dt.timedelta(days=365*3)

#Téléchargement
Actions = ['AAPL','MSFT','GOOGL','AMZN','META']
Data = yf.download(Actions, start=Start_date, end=End_date)
st.dataframe(Data)
#st.line_chart(Data)
Close = Data['Close']
Open = Data['Open']
High = Data['High']
Low = Data['Low']
Volume = Data['Volume']
st.line_chart(Close)


#itérer les variables Apple
Apple_colonne = {}
for col in Data.columns:
   if "AAPL" in col:
      Apple_colonne[col] = Data[col]

Data_apple = pd.DataFrame(Apple_colonne)
#st.dataframe(Data_apple)



#itérer les variables Meta
Meta_colonne = {}
for col in Data.columns:
   if "META" in col:
      Meta_colonne[col] = Data[col]

Data_meta = pd.DataFrame(Meta_colonne)



#itérer les variables AMZN
Amzn_colonne = {}
for col in Data.columns:
   if "AMZN" in col:
      Amzn_colonne[col] = Data[col]

Data_amzn = pd.DataFrame(Amzn_colonne)



#itérer les variables GOOGLE
Googl_colonne = {}
for col in Data.columns:
   if "GOOGL" in col:
      Googl_colonne[col] = Data[col]

Data_googl = pd.DataFrame(Googl_colonne)


#itérer les variables MSFT
Msft_colonne = {}
for col in Data.columns:
   if "MSFT" in col:
      Msft_colonne[col] = Data[col]
Data_msft = pd.DataFrame(Msft_colonne)





st.sidebar.subheader("Sélection",divider=True)
with st.sidebar.expander('Analyse boursière'):
   st.write("Faites une sélection d'entreprise à visualiser")
Liste = ['Apple','Microsoft','Meta','Amazon']
Liste_choix = st.sidebar.selectbox("Choisissez une entreprise", options = Liste, index = None, placeholder="Entreprise")

if Liste_choix == "Apple":
   
#application Apple
#declaration des variables
    Apple_close = Data_apple['Close']
    Apple_choix = st.radio("Analysez l'évolution de Apple ",['Ouverture','Fermeture','Volume','Maximum','Minimum'])
    if Apple_choix == "Ouverture":
        if "Close" in Data_apple.columns:
            close_apple = Data_apple['Close']
            st.line_chart(close_apple,color="#FFC759")

    elif Apple_choix == "Fermeture":
        if "Open" in Data_apple.columns:
         Open_apple = Data_apple['Open']
        st.line_chart(Open_apple,color="#FF7B9C")


    elif Apple_choix == "Volume":
        if "Volume" in Data_apple.columns:
            Volume_apple = Data_apple["Volume"]
        st.line_chart(Volume_apple,color="#607196")

    elif Apple_choix == "Maximum":
       if "High" in Data_apple.columns:
          High_apple = Data_apple["High"]
          Maximum_apple = Data_apple["High"]
       st.line_chart(Maximum_apple,color="#BABFD1")

    else:
       if "Low" in Data_apple.columns:
          Low_apple = Data_apple["Low"]
       st.line_chart(Low_apple,color="#E8E9ED")




#Microsoft
elif Liste_choix == "Microsoft":
   Microsoft_choix = st.radio("Les options",['Ouverture','Fermeture','Volume','Maximum','Minimum'])

   #ouverture
   if Microsoft_choix == "Ouverture":
      if "Open" in Data_msft.columns:
         Ouverture_msft = Data_msft['Open']
      st.line_chart(Ouverture_msft,color="#ffffff")

   elif Microsoft_choix == "Fermeture":
      if "Close" in Data_msft.columns:
         Fermeture_msft = Data_msft['Close']
      st.line_chart(Fermeture_msft,color="#929982")

   elif Microsoft_choix == "Volume":
      if "Volume" in Data_msft.columns:
         Fermeture_msft = Data_msft['Volume']
      st.line_chart(Fermeture_msft,color="#EDCBB1")


   elif Microsoft_choix == "Maximum":
      if "High" in Data_msft.columns:
         Maximum_msft = Data_msft['High']
      st.line_chart(Maximum_msft,color="#B7245C")

   else:
      if 'Low' in Data_msft.columns:
         Minimum_msft = Data_msft['Low']
      st.line_chart(Minimum_msft,color="#B7245C")
      


#Meta
if Liste_choix == "Meta":
    Meta_choix = st.radio("Analysez l'évolution de Meta",['Ouverture','Fermeture','Volume','Maximum','Minimum'])

    #ouverture
    if Meta_choix == "Ouverture":
       if "Open" in Data_meta.columns:
          Ouverture_meta = Data_meta['Open']
          st.line_chart(Ouverture_meta,color="#D3BDB0")

    #Fermeture
    elif Meta_choix == "Fermeture":
       if "Close" in Data_meta.columns:
          Fermeture_meta = Data_meta['Close']
          st.line_chart(Fermeture_meta, color="#C1AE9F")

          #Volume
    elif Meta_choix == "Volume":
       if "Volume" in Data_meta.columns:
          Volume_meta = Data_meta['Volume']
          st.line_chart(Volume_meta,color="#89937C")

    elif Meta_choix == "Maximum":
       if "High" in Data_meta.columns:
          Maximum_meta = Data_meta['High']
          st.line_chart(Maximum_meta,color="#715B64")


    else:
       if "Low" in Data_meta.columns:
          Minimum_meta = Data_meta['Low']
          st.line_chart(Minimum_meta,color="#69385C")


#insertion du calendrier

with st.sidebar.expander("Sélection de dates"):
   st.info("Définissez une plage de dates avec le calendrier ci-dessous pour effectuer votre analyse")
Calendrier  = st.sidebar.date_input("Définissez une plage de dates", value=(Start_date,End_date))
# A améliorer
if len(Calendrier) == 2 and Calendrier[0] < Calendrier[1]:
   Choix_calendrier = st.sidebar.radio("Options",['Ouverture','Fermeture','Volume','Maximum','Minimum'])
   if Choix_calendrier == "Ouverture":
      st.subheader('Analyse comparative : Ouverture')
      st.info('Ce graphique est une analyse comparative des entreprises à la fermeture en fonction de la plage de date définie')
      Data_open = Data["Open"]
      st.line_chart(Data_open)
   
   #fermeture
   elif Choix_calendrier == "Fermeture":
      st.subheader('Analyse comparative : fermeture')
      st.info("Ce graphique est une analyse comparative des entreprises à l'ouverture en fonction de la plage de date définie")
      Data_close = Data["Close"]
      st.line_chart(Data_close)

   #Volume
   elif Choix_calendrier == "Volume":
      st.subheader('Analyse comparative : les volumes de stocks')
      st.info("Ce graphique est une analyse comparative des volumes disponibles en fonction de la plage de date définie")
      Data_volume = Data["Volume"]
      st.line_chart(Data_volume)

   #Maximum
   elif Choix_calendrier == "Maximum":
      st.subheader('Analyse comparative : le stock journalier le plus élevé')
      st.info("Ce graphique est une analyse comparative de niveau de stock le plus élevé en fonction de la plage de date définie")
      Data_max = Data["High"]
      st.line_chart(Data_max)

   #minimum
   elif Choix_calendrier == "Minimum":
      st.subheader('Analyse comparative : le stock journalier le plus faible')
      st.info("Ce graphique est une analyse comparative de niveau de stock le plus faible en fonction de la plage de date définie")
      Data_min = Data["Low"]
      st.line_chart(Data_min)
else:
   st.sidebar.info("Veuillez sélectionner une plage de dates 📅")

#les graphs de comparaison 







