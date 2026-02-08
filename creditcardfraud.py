import streamlit as st
import pickle
from PIL import Image

#create a function
def main():
    #to add title (st means streamlit)
    st.title(':red[CREDIT CARD FRAUD DETECTION]')
    #to read image
    image=Image.open(r"C:\Users\user\Desktop\credit card fraud detection\creditcard.jfif")
    st.image(image,width=600)

    #identify the features

    #input features
    amount=st.text_input('amount','Type Here')
    transaction_hour=st.text_input('transaction_hour','Type Here')
    merchant_category=st.radio('merchant_category',['Food','Clothing','Travel','Grocery','Electronics'])
    
    foreign_transaction=st.text_input('foreign_transaction','Type Here') 
    location_mismatch=st.text_input('location_mismatch','Type Here') 
    device_trust_score=st.text_input('device_trust_score','Type Here') 
    velocity_last_24h=st.text_input('velocity_last_24h','Type Here') 
    
   
    #load the stored model and scalar
    model1 = pickle.load(open(r"C:\Users\user\Desktop\credit card fraud detection\credit", "rb"))
    scaler1 = pickle.load(open(r"C:\Users\user\Desktop\credit card fraud detection\scaler", "rb"))
    encode1=pickle.load(open(r"C:\Users\user\Desktop\credit card fraud detection\encode","rb"))


    #to predict we add a button

    pred=st.button('PREDICT')


    #enable button
    

    if pred:
        # Encode categorical feature
        merchant_category_encoded = encode1.transform([merchant_category])[0]

        # Convert inputs to correct numeric types and rebuild feature list
        f = [[
            float(amount),
            int(transaction_hour),
            merchant_category_encoded,
            int(foreign_transaction),
            int(location_mismatch),
            float(device_trust_score),
            int(velocity_last_24h)
        ]]

        # Scale and predict
        prediction = model1.predict(scaler1.transform(f))

        if prediction[0] == 0:
            st.write('LEGITIMATE')
            st.balloons()
        else:
            st.write('FRAUDULENT')

            
main()
            







