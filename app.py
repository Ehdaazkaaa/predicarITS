import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model_toyota_knn.pkl')

# Konstanta konversi Euro ke Rupiah
EUR_TO_IDR = 18617.72

# UI
import streamlit as st
st.image("https://static.wixstatic.com/media/261cbb_c1eda2003b1e41e0bfca58af74a3fa06~mv2.jpg/v1/fill/w_1780,h_1335,al_c,q_90/261cbb_c1eda2003b1e41e0bfca58af74a3fa06~mv2.webp", use_column_width=True)
st.title("🚗 Prediksi Harga Mobil Bekas Toyota 🚗")
st.markdown("**Prediksi Harga Mobil Toyota Bekas Anda Dalam Hitungan Detik**")


# Input pengguna
year = st.number_input("Tahun Mobil", min_value=1990, max_value=2025, value=2018)
mileage = st.number_input("Jarak Tempuh (km)", min_value=0, max_value=300000, value=50000)
tax = st.number_input("Pajak (Euro)", min_value=0, max_value=600, value=150)
mpg = st.number_input("Konsumsi BBM (mpg)", min_value=10.0, max_value=100.0, value=40.0)
engineSize = st.number_input("Ukuran Mesin (liter)", min_value=0.5, max_value=6.0, value=1.6, step=0.1)

# Prediksi harga
if st.button("Prediksi Harga"):
    input_df = pd.DataFrame([[year, mileage, tax, mpg, engineSize]],
                            columns=['year', 'mileage', 'tax', 'mpg', 'engineSize'])

    # Prediksi harga dalam Euro
    prediction_euro = model.predict(input_df)[0]

    # Konversi ke Rupiah
    prediction_rupiah = prediction_euro * EUR_TO_IDR
    tax_rupiah = tax * EUR_TO_IDR

    st.markdown(f"💶 Pajak Mobil: Rp {tax_rupiah:,.2f}")
    st.success(f"💰 Estimasi Harga Mobil Bekas: Rp {prediction_rupiah:,.2f}")
