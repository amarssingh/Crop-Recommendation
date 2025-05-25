import streamlit as st
import numpy as np
import pickle

page_bg_img = '''
<style>
body {
    background-image: url("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1470&q=80");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

.stApp {
    background-color: rgba(255, 255, 255, 0.4);
    border-radius: 15px;
    padding: 20px 40px 40px 40px;
    box-shadow: 5px 5px 20px rgba(0,0,0,0.3);
}

/* Input labels */
[data-testid="stNumberInput"] > label, 
[data-testid="stNumberInput"] label {
    color: #222222 !important;
    font-weight: 600;
    font-size: 16px;
}

/* Input box text */
div[data-baseweb="input"] input {
    color: #222222 !important;
    background-color: #f9f9f9 !important;
}

/* Placeholder text */
div[data-baseweb="input"] input::placeholder {
    color: #999999 !important;
}

/* Styled description paragraph */
.description-text {
    text-align: center;
    font-size: 18px;
    color: #222222;
    text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.7);
    margin-bottom: 1.5rem;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Load model and scaler
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('minmaxscaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

crop_map = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
    8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
    14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
    19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
}

translations = {
    'en': {
        'title': "🌱 Crop Recommendation System",
        'description': "Provide soil and climate information to get the best crop recommendation.",
        'nitrogen': "Nitrogen (N)",
        'phosphorus': "Phosphorus (P)",
        'potassium': "Potassium (K)",
        'temperature': "Temperature (°C)",
        'humidity': "Humidity (%)",
        'ph': "Soil pH",
        'rainfall': "Rainfall (mm)",
        'predict_button': "Predict Crop",
        'result': "Recommended Crop",
        'unknown_crop': "Unknown Crop",
        'select_language': "Select Language"
    },
    'hi': {
        'title': "🌱 फसल अनुशंसा प्रणाली",
        'description': "सर्वश्रेष्ठ फसल अनुशंसा प्राप्त करने के लिए मिट्टी और जलवायु जानकारी प्रदान करें।",
        'nitrogen': "नाइट्रोजन (N)",
        'phosphorus': "फॉस्फोरस (P)",
        'potassium': "पोटैशियम (K)",
        'temperature': "तापमान (°C)",
        'humidity': "आर्द्रता (%)",
        'ph': "मिट्टी का पीएच",
        'rainfall': "वर्षा (मिमी)",
        'predict_button': "फसल अनुमानित करें",
        'result': "अनुशंसित फसल",
        'unknown_crop': "अज्ञात फसल",
        'select_language': "भाषा चुनें"
    }
}

# Sidebar language selection
lang = st.sidebar.selectbox(
    translations['en']['select_language'],
    options=['English', 'हिन्दी']
)
lang_code = 'hi' if lang == 'हिन्दी' else 'en'

# Title and description with some spacing
st.markdown(f"<h1 style='text-align:center;color:green'>{translations[lang_code]['title']}</h1>", unsafe_allow_html=True)
#st.markdown(f"<p style='text-align:center;font-size:18px'>{translations[lang_code]['description']}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='description-text'>{translations[lang_code]['description']}</p>", unsafe_allow_html=True)

st.write("")  # spacer

# Organize inputs into two columns
col1, col2, col3 = st.columns(3)

with col1:
    N = st.number_input(translations[lang_code]['nitrogen'], 0.0, 140.0, step=1.0)
    P = st.number_input(translations[lang_code]['phosphorus'], 5.0, 145.0, step=1.0)
    K = st.number_input(translations[lang_code]['potassium'], 5.0, 205.0, step=1.0)

with col2:
    temperature = st.number_input(translations[lang_code]['temperature'], 0.0, 50.0)
    humidity = st.number_input(translations[lang_code]['humidity'], 10.0, 100.0)

with col3:
    ph = st.number_input(translations[lang_code]['ph'], 3.5, 9.5)
    rainfall = st.number_input(translations[lang_code]['rainfall'], 20.0, 300.0)

st.write("")  # spacer

# Center the predict button with custom styling
predict_btn = st.button(translations[lang_code]['predict_button'])
if predict_btn:
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    
    crop_name = crop_map.get(prediction[0], translations[lang_code]['unknown_crop'])
    st.markdown(f"""
        <div style='
            background-color: #eaf7ea;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            text-align: center;
            box-shadow: 2px 2px 12px #a1d99a;
            font-size: 24px;
            color: #2f6627;
            font-weight: bold;
        '>
        🌾 {translations[lang_code]['result']}: {crop_name}
        </div>
    """, unsafe_allow_html=True)
