
import streamlit as st
import joblib

def main():
    # Set page config to wide layout and give it a title
    st.set_page_config(layout="wide", page_title="Health Insurance Price Predictor")
    
    # Define custom CSS styles
    css = """
    <style>
    body {
        background-color: #1E1F20;
        color: #FFFFFF;
    }
    .header {
        background-color: #336699;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    .header h2 {
        color: #FFFFFF;
        font-family: Arial, sans-serif;
    }

    .success-message {
        font-weight: bold;
        font-size: 18px;
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Health Insurance Price Predictor </h2>
    </div>
    """
    # Apply custom CSS styles
    st.markdown(css, unsafe_allow_html=True)
    
    # Header section
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Model loading
    # model = joblib.load('model_joblib_rf')
    model = joblib.load('model_joblib_dt')
    
    # Input section
    st.sidebar.title("Your Details")
    age = st.sidebar.slider('Age', 0, 100)
    sex = st.sidebar.selectbox('Sex', ('Male', 'Female'))
    bmi = st.sidebar.number_input('BMI', value=25.0, step=1.00)
    children = st.sidebar.slider('Number of Children', 0, 10)
    smoker = st.sidebar.selectbox('Smoker', ('No', 'Yes'))
    region = st.sidebar.selectbox('Region', ('Northwest', 'Southwest', 'Southeast', 'Northeast'))
    
    # Convert input values
    sex = 1 if sex == 'Male' else 0
    boolSmoker = 1 if smoker == 'Yes' else 0
    region_mapping = {'Northwest': 0, 'Southwest': 1, 'Southeast': 2, 'Northeast': 3}
    region_code = region_mapping[region]
    
    # Make prediction
    if st.sidebar.button('Predict'):
        pred = model.predict([[age, sex, bmi, children, boolSmoker, region_code]])
        st.markdown("<div class='prediction'><h3>Your Insurance Cost</h3><h2>${:.2f}</h2></div>".format(pred[0]), unsafe_allow_html=True)
        st.markdown("<div class='success-message'>Thank you for using our service!</div>", unsafe_allow_html=True)
    
if __name__ == '__main__':
    main()
