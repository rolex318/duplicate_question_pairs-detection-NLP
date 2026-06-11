import streamlit as st
import helper
import pickle

# Load the pre-trained model
model = pickle.load(open('model.pkl', 'rb'))

# Custom CSS for better visual experience
st.markdown(
    """
    <style>
    /* Main background and font */
    .stApp {
        background-color: #f5f7fa;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Header styling */
    h1 {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 30px;
        font-weight: 600;
    }

    /* Style text input boxes */
    .stTextInput > div > div > input {
        background-color: white;
        border-radius: 8px;
        border: 1px solid #d1d5db;
        padding: 10px 14px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    .stTextInput > div > div > input:focus {
        border-color: #4f46e5;
        box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.2);
        outline: none;
    }

    /* Label styling */
    .stTextInput label {
        font-weight: 500;
        color: #374151;
        font-size: 14px;
        margin-bottom: 4px;
    }

    /* Button styling */
    .stButton > button {
        background-color: #4f46e5;
        color: white;
        font-weight: 600;
        padding: 10px 24px;
        border-radius: 40px;
        border: none;
        font-size: 16px;
        transition: 0.2s;
        width: 100%;
        margin-top: 20px;
    }
    .stButton > button:hover {
        background-color: #4338ca;
        transform: scale(1.01);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        cursor: pointer;
    }

    /* Result message boxes */
    .duplicate-box {
        background-color: #fee2e2;
        border-left: 8px solid #dc2626;
        padding: 16px 20px;
        border-radius: 12px;
        text-align: center;
        margin-top: 30px;
        font-size: 24px;
        font-weight: bold;
        color: #991b1b;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .not-duplicate-box {
        background-color: #dcfce7;
        border-left: 8px solid #16a34a;
        padding: 16px 20px;
        border-radius: 12px;
        text-align: center;
        margin-top: 30px;
        font-size: 24px;
        font-weight: bold;
        color: #166534;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    /* Footer or helper text */
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #6b7280;
        font-size: 13px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App header
st.header("🔍 Duplicate Question Pairs")

# Input fields
q1 = st.text_input("Enter question 1", placeholder="e.g., How to learn Python?")
q2 = st.text_input("Enter question 2", placeholder="e.g., What is the best way to learn Python?")

# Predict button
if st.button('Find Duplicate'):
    if q1.strip() and q2.strip():
        query = helper.query_point_creator(q1, q2)
        result = model.predict(query)[0]

        if result:
            st.markdown(
                '<div class="duplicate-box">⚠️ Duplicate Questions ⚠️</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div class="not-duplicate-box">✅ Not Duplicate ✅</div>',
                unsafe_allow_html=True
            )
    else:
        st.warning("Please enter both questions to proceed.")

# Optional footer
st.markdown('<div class="footer">Powered by Machine Learning | Detects duplicate question pairs by chinu</div>',
            unsafe_allow_html=True)