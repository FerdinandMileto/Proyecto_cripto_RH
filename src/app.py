
import streamlit as st
import numpy as np
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,root_mean_squared_error
import plotly.express as px
import plotly.graph_objects as go
#primero vamos a armar el modelo y todas las funciones y luego la pagina

import requests
import pandas as pd
url = "https://api.binance.com/api/v3/exchangeInfo"
data = requests.get(url).json()
# Extraer todos los símbolos disponibles
symbols = [s['symbol'] for s in data['symbols']]
print(symbols[:20])  # mostrar los primeros 20

monedas=[]
for i in symbols:
    if i[4:]=="USDT":
        monedas.append(i[:4])
############################################
#










tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "📈 prediccion", "⚙️ Modelo"])

with tab1:
    st.write("Aquí va el dashboard")
    #trae una tabla con sus modelos y accuracy
    st
with tab2:
    selected_crypto = st.selectbox("Criptomoneda:", monedas)
    
    df=pd.read_csv("/home/rodrigo/Escritorio/Repositorios/Proyecto_cripto_RH/data/raw/df_cripto/"+(selected_crypto)+"USDT_1h_250days.csv")
    #aqui va una elecion de que moneda se quiere predeciir junto con su modelo 
    grafico=pd.DataFrame({"fecha":df["open_time"],"precio":df["close"]})
    #grafico=grafico.set_index("fecha")
    y_min = grafico["precio"].min()
    y_max = grafico["precio"].max()
    margen = (y_max - y_min) * 0.05  # margen 5%

    # Crear figura
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=grafico["fecha"], y=grafico["precio"], mode="lines", name="Precio"))

    # Ajustar layout con eje Y centrado
    fig.update_layout(
        yaxis=dict(range=[y_min - margen, y_max + margen]),
        xaxis_title="Fecha",
        yaxis_title="Precio",
        title=f"Ultimos 250 dias de {selected_crypto}"
    )

# Mostrar en Streamlit
st.plotly_chart(fig, use_container_width=True)

# Mostrar en Streamlit

with tab3:
    st.write("Aquí va el modelo")
    #descripcion del modelo






#ahora la pagina


