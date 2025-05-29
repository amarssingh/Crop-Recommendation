# 🌾 Crop Recommendation System Using Machine Learning

This project helps farmers choose the most suitable crop based on soil and climate conditions using a machine learning model trained on real-world agricultural data. The model was developed using Python and deployed with **Streamlit** for an easy-to-use web interface. It also supports **multi-language functionality (e.g., Hindi)** to improve accessibility for Indian farmers.

---

## 🚀 Live Demo

👉[ [Click here to try the live app](https://whatcropshouldigrow.streamlit.app/)  ]

---

## 🔍 Features

- ✅ Predicts the best crop to grow based on:
  - Nitrogen (N), Phosphorus (P), Potassium (K)
  - Temperature, Humidity
  - pH value of soil
  - Rainfall
- 🌐 Multi-language support (currently supports **English and Hindi**)
- 🎨 Clean, styled UI with background image and custom CSS
- 📦 Model and scaler saved using Pickle (`model.pkl`, `minmaxscaler.pkl`)
- 💻 Deployed using **Streamlit Cloud** for easy access via web browser

---

## 📁 Project Structure

```bash
├── app.py                # Streamlit app
├── Untitled.ipynb         # Notebook (for reference or code transfer)
├── model.pkl             # Trained machine learning model
├── minmaxscaler.pkl      # MinMaxScaler for input preprocessing
├── crop_recommendation.csv  # Dataset used for training
├── README.md             # This file
├── requirements.txt      # Libraries list
```

---

## 📊 Model Info

Algorithm Used: Random Forest  

Accuracy: Achieved high classification accuracy on test data (0.9954545454545455) 

Trained on real-world dataset with 22 crop labels including:  

Rice, Maize, Jute, Cotton, Coconut, Papaya, Orange, Apple, Muskmelon, Watermelon, Grapes, Mango, Banana, Pomegranate, Lentil, Blackgram, Mungbean, Mothbeans, Pigeonpeas, Kidneybeans, Chickpea, Coffee

---

## 📦 How to Run Locally

**Clone the repository:**  

```bash
git clone https://github.com/amarssingh/Crop-Recommendation-app.git
cd crop-recommendation-app
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Run the Streamlit app:**

```bash
streamlit run app.py
```

---

## 🌍 Multi-language Support

You can choose your preferred language (currently English or Hindi) at the top of the app. Translations are handled through a dictionary-based system, and can easily be extended to more languages in the future.

--- 

## 🛰 Deployment

The project has been deployed using Streamlit Cloud which allows easy access via any modern browser without the need to install anything.

Visit: [https://whatcropshouldigrow.streamlit.app/]

---

## 🙌 Acknowledgements

Dataset Source: Kaggle Crop Recommendation Dataset  

Inspired by the need to help Indian farmers through technology and AI  

---

## 📬 Contact

Developer: Amar Singh
📧 Connect with me on [LinkedIn](https://www.linkedin.com/in/amarssingh-in)

