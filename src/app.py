
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
import joblib
#primero vamos a armar el modelo y todas las funciones y luego la pagina

import requests
import pandas as pd
url = "https://api.binance.com/api/v3/exchangeInfo"
data = requests.get(url).json()
# Extraer todos los símbolos disponibles
symbols = [s['symbol'] for s in data['symbols']]
print(symbols[:20])  # mostrar los primeros 20

monedas=[
    "ETHUSDT",  # Ethereum
    "BTCUSDT",  # Bitcoin  
    "BNBUSDT",  # Binance Coin
    "XRPUSDT",  # Ripple
    "SOLUSDT",  # Solana
    "ADAUSDT",  # Cardano
    "LTCUSDT",  # Litecoin
    "DOTUSDT",  # Polkadot
]
############################################
#










tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "📈 prediccion", "⚙️ Modelo"])

with tab1:
    st.write("Aquí va el dashboard")
    #trae una tabla con sus modelos y accuracy
    st
with tab2:
    selected_crypto = st.selectbox("Criptomoneda:", monedas)
    
    df=pd.read_csv("/home/rodrigo/Escritorio/Repositorios/Proyecto_cripto_RH/data/raw/df_cripto/"+(selected_crypto)+"_1h_250days_porcentual.csv")
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




# Cargar modelo
    @st.cache_resource  # para que no se recargue cada vez
    def load_model(selected_cripto=selected_crypto):
        return joblib.load("/home/rodrigo/Escritorio/Repositorios/Proyecto_cripto_RH/models/rand_forest_rf_"+(selected_cripto)+".pkl")

    model = load_model()
    
# Mostrar en Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Mostrar en Streamlit

with tab3:
    st.write("Aquí va el modelo")
    #descripcion del modelo






#ahora la pagina


