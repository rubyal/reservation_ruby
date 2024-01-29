import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
@st.cache
def load_data():
    return pd.read_csv("hotel_bookings.csv")

# Autenticación
def authentication():
    username = st.text_input("Nombre de usuario:")
    password = st.text_input("Contraseña:", type="password")
    return username, password

def main():
    st.title("Aplicación de Cancelaciones Hoteleras")

    # Autenticación
    username, password = authentication()

    if username == "lileth" and password == "contraseña_admin":
        st.sidebar.title("Dashboard de Administrador")
        df = load_data()

        st.write("## Estadísticas Globales")
        st.write(f"Total de Reservas: {len(df)}")
        st.write(f"Total de Cancelaciones: {len(df[df['is_canceled'] == 1])}")

        # Gráfico de barras de cancelaciones por mes
        st.write("## Cancelaciones por Mes")
        cancelaciones_por_mes = df[df['is_canceled'] == 1].groupby('arrival_date_month')['is_canceled'].count()
        st.bar_chart(cancelaciones_por_mes)

    elif username == "carlos" and password == "contraseña_usuario":
        st.sidebar.title("Dashboard de Usuario")
        df = load_data()

        st.write("## Estadísticas para City Hotel")
        city_hotel_df = df[df['hotel'] == "City Hotel"]
        st.write(f"Total de Reservas en City Hotel: {len(city_hotel_df)}")
        st.write(f"Total de Cancelaciones en City Hotel: {len(city_hotel_df[city_hotel_df['is_canceled'] == 1])}")

        # Gráfico de barras de cancelaciones por año
        st.write("## Cancelaciones por Año en City Hotel")
        city_hotel_cancelaciones_por_año = city_hotel_df[city_hotel_df['is_canceled'] == 1].groupby('arrival_date_year')['is_canceled'].count()
        st.bar_chart(city_hotel_cancelaciones_por_año)

    else:
        st.error("Nombre de usuario o contraseña incorrectos.")

if __name__ == "__main__":
    main()
