
import streamlit as st
import joblib

def main():
    st.title('Test')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Health Insurance Price Predictor </h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    #model= joblib.load('model_joblib_rf')
    model= joblib.load('model_joblib_dt')
    age= st.slider('Enter Your Age',18,100)
    s1= st.selectbox('Sex',('Male','Female'))
    
    if s1=='Male':
        sex=1
    else:
        sex=0
    
    bmi= st.number_input("Enter your BMI Value")
    
    children=st.slider('Enter the No. of Children',0,10)
    smoker=st.selectbox('Smoker',('yes','no'))
    
    if smoker=='yes':
        boolSmoker=1
    else:
        boolSmoker=0
    
    region= st.slider('Enter your region',1,4)
    
    if st.button('Predict'):
        pred=model.predict([[age,sex,bmi,children,boolSmoker,region]])
        
        st.success('Your Insurance Cost is {}'.format(round(pred[0],2)))
    
if __name__ == '__main__' :
    main()