#  Smart Crop Recommendation System using Machine Learning

This project leverages machine learning to recommend the most suitable crop based on soil and environmental conditions. It is built to support precision agriculture, especially for Indian farmers, helping them make informed crop selection decisions to maximize yield and sustainability.

##  Features

- Predicts the best crop using real-time input
- Ensemble of Naïve Bayes and Random Forest classifiers
- High accuracy (96.5%) using majority voting
- Supports agricultural decision-making with minimal technical expertise

##  How It Works

1. **Input Parameters**:
   - Nitrogen (N)
   - Phosphorus (P)
   - Potassium (K)
   - Temperature
   - Humidity
   - pH
   - Rainfall

2. **Machine Learning Models**:
   - Trained Naïve Bayes and Random Forest classifiers
   - Combined using a voting mechanism for improved accuracy

3. **Prediction**:
   - Takes user input
   - Returns the best crop to grow under current conditions

##  Model Accuracy

| Model            | Accuracy |
|------------------|----------|
| Naïve Bayes      | ~86%     |
| Random Forest    | ~95%     |
| Ensemble Voting  | **96.5%**  |

##  Installation

```bash
git clone https://github.com/yourusername/crop-recommendation-ml.git
cd crop-recommendation-ml
pip install -r requirements.txt
python app.py
```

## Dependencies:
   - Python 3.x
   - scikit-learn
   - pandas
   - numpy
   - Flask (for web deployment)
	 

## Use Case
Ideal for:

- Farmers seeking guidance on crop planning
- Agricultural advisors
- Agri-tech startups promoting smart farming

## Future Improvements
- Integration with real-time weather APIs
- Mobile app version
- Support for regional languages

## Acknowledgements
I sincerely thank the agricultural research community, dedicated farmers, and supporting organizations for their invaluable insights, data, and domain expertise, all of which greatly contributed to the development of this Crop Recommendation System.


