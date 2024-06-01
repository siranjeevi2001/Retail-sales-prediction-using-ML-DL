import streamlit as st
import pandas as pd
import pickle
import joblib
import streamlit.components.v1 as components


# Load the saved model
# with open('trained_model2.pkl', 'rb') as f:
#     model = pickle.load(f)
    
# option extract techniq

def option_exract(option):
    
    df = pd.read_csv('merge_sales_store_data.csv')
    df1 = pd.read_csv('Final.csv')
    
    test = df[option].value_counts()
    # Convert to DataFrame
    test = test.reset_index()
    test.columns = [option, 'count']



    en_code = df1[option].value_counts()
    en_code = en_code.reset_index()
    en_code.columns = [option, 'count']


    # Create a dictionary from the two lists
    status_dict = {j: i for i, j in zip(en_code[option], test[option])}

    return status_dict

# Season	Season_encoded

def option_exract1(option):
    
    df = pd.read_csv('cleaned_Features_data_set.csv')
    df1 = pd.read_csv('Final.csv')
    
    test = df[option].value_counts()
    # Convert to DataFrame
    test = test.reset_index()
    test.columns = [option, 'count']

    en_code = df1[option].value_counts()
    en_code = en_code.reset_index()
    en_code.columns = [option, 'count']


    # Create a dictionary from the two lists
    status_dict = {j: i for i, j in zip(en_code[option], test[option])}

    return status_dict



def exgboost():

    # Title of the page
    st.header("Retail Weeekly sales prediction", divider='rainbow')
    st.write("Mean Squared Error: 10400504.256164866")
    st.write("R² Score: 0.9534317034121326")
    


    model = joblib.load('xgbooster_model1.pkl')
    # model2 = joblib.load('trained_model1.pkl')

    # Collecting user inputs
    store = st.number_input('Store', min_value=1, step=1, value=1)
    dept = st.number_input('Dept', min_value=1, max_value=98,step=1, value=1)


    type_option = {'A': 0, 'B': 1, 'C': 2}
    selection_type = st.selectbox('Type', options=list(type_option.keys()), index=0)
    store_type = type_option[selection_type]

    size = st.number_input('Size', min_value=0, step=1, value=150000)
    # temperature = st.number_input('Temperature', min_value=-100.0, max_value=150.0, step=0.1, value=55.0)
    fuel_price = st.number_input('Fuel Price', min_value=0.0, step=0.01, value=2.5)
    markdown1 = st.number_input('MarkDown1', min_value=0.0, step=0.01, value=0.0)
    markdown2 = st.number_input('MarkDown2', min_value=0.0, step=0.01, value=0.0)
    markdown3 = st.number_input('MarkDown3', min_value=0.0, step=0.01, value=0.0)
    markdown4 = st.number_input('MarkDown4', min_value=0.0, step=0.01, value=0.0)
    markdown5 = st.number_input('MarkDown5', min_value=0.0, step=0.01, value=0.0)
    cpi = st.number_input('CPI', min_value=0.0, step=0.1, value=211.0)
    unemployment = st.number_input('Unemployment', min_value=0.0, step=0.1, value=8.1)

    # Assuming option_exract1 is a function that extracts unique options from a column
    season_option = {'Spring': 2, 'Summer': 3, 'Autumn': 0, 'Winter': 4, 'Extreme Heat': 1}
    selection_season = st.selectbox('Select season', options=list(season_option.keys()), index=0)
    season_encoded = season_option[selection_season]

    holiday_option = {False: 0, True: 1}
    selected_is_holiday_encoded = st.selectbox('IsHoliday_encoded', options=list(holiday_option.keys()), index=0)
    is_holiday_encoded = holiday_option[selected_is_holiday_encoded]

    week_number = st.number_input('Week Number', min_value=1, max_value=52, step=1, value=5)
    year = st.number_input('Year', min_value=2000, max_value=2100, step=1, value=2010)

    # Creating a dictionary from the inputs
    input_data = {
        'Store': [store],
        'Dept': [dept],
        'Type': [store_type],
        'Size': [size],
        # 'Temperature': [temperature],
        'Fuel_Price': [fuel_price],
        'MarkDown1': [markdown1],
        'MarkDown2': [markdown2],
        'MarkDown3': [markdown3],
        'MarkDown4': [markdown4],
        'MarkDown5': [markdown5],
        'CPI': [cpi],
        'Unemployment': [unemployment],
        'Season_encoded': [season_encoded],
        'IsHoliday_encoded': [is_holiday_encoded],
        'week_number': [week_number],
        'year': [year]
        }
        
    df = pd.DataFrame(input_data)

        # Apply the same preprocessing steps to the sample data
        # (e.g., encoding, scaling, etc.)
    if st.button('XGboost Submit'):
        # Predict the selling price using the sample data
        prediction = model.predict(df)
        st.write("Sample Data:")
        st.write(df)
        st.header(f"The Sales predicted is: {prediction[0]}")
            
            
# def randomforest():
    
#     # Title of the page
#     st.header("Retail Weeekly sales prediction", divider='rainbow')


#     model = joblib.load('randomforest_model2.pkl')
#     # model2 = joblib.load('trained_model1.pkl')

#     # Collecting user inputs
#     store = st.number_input('Store', min_value=1, step=1, value=1)
#     dept = st.number_input('Dept', min_value=1, max_value=98,step=1, value=1)


#     type_option = {'A': 0, 'B': 1, 'C': 2}
#     selection_type = st.selectbox('Type', options=list(type_option.keys()), index=0)
#     store_type = type_option[selection_type]

#     size = st.number_input('Size', min_value=0, step=1, value=150000)
#     # temperature = st.number_input('Temperature', min_value=-100.0, max_value=150.0, step=0.1, value=55.0)
#     fuel_price = st.number_input('Fuel Price', min_value=0.0, step=0.01, value=2.5)
#     markdown1 = st.number_input('MarkDown1', min_value=0.0, step=0.01, value=0.0)
#     markdown2 = st.number_input('MarkDown2', min_value=0.0, step=0.01, value=0.0)
#     markdown3 = st.number_input('MarkDown3', min_value=0.0, step=0.01, value=0.0)
#     markdown4 = st.number_input('MarkDown4', min_value=0.0, step=0.01, value=0.0)
#     markdown5 = st.number_input('MarkDown5', min_value=0.0, step=0.01, value=0.0)
#     cpi = st.number_input('CPI', min_value=0.0, step=0.1, value=211.0)
#     unemployment = st.number_input('Unemployment', min_value=0.0, step=0.1, value=8.1)

#     # Assuming option_exract1 is a function that extracts unique options from a column
#     season_option = {'Spring': 2, 'Summer': 3, 'Autumn': 0, 'Winter': 4, 'Extreme Heat': 1}
#     selection_season = st.selectbox('Select season', options=list(season_option.keys()), index=0)
#     season_encoded = season_option[selection_season]

#     holiday_option = {False: 0, True: 1}
#     selected_is_holiday_encoded = st.selectbox('IsHoliday_encoded', options=list(holiday_option.keys()), index=0)
#     is_holiday_encoded = holiday_option[selected_is_holiday_encoded]

#     week_number = st.number_input('Week Number', min_value=1, max_value=52, step=1, value=5)
#     year = st.number_input('Year', min_value=2000, max_value=2100, step=1, value=2010)

#     # Creating a dictionary from the inputs
#     input_data = {
#         'Store': [store],
#         'Dept': [dept],
#         'Type': [store_type],
#         'Size': [size],
#         # 'Temperature': [temperature],
#         'Fuel_Price': [fuel_price],
#         'MarkDown1': [markdown1],
#         'MarkDown2': [markdown2],
#         'MarkDown3': [markdown3],
#         'MarkDown4': [markdown4],
#         'MarkDown5': [markdown5],
#         'CPI': [cpi],
#         'Unemployment': [unemployment],
#         'Season_encoded': [season_encoded],
#         'IsHoliday_encoded': [is_holiday_encoded],
#         'week_number': [week_number],
#         'year': [year]
#         }
        
#     df = pd.DataFrame(input_data)

#         # Apply the same preprocessing steps to the sample data
#         # (e.g., encoding, scaling, etc.)
#     if st.button('XGboost Submit'):
#         # Predict the selling price using the sample data
#         prediction = model.predict(df)
#         st.write("Sample Data:")
#         st.write(df)
#         st.header(f"The predicted selling price is: {prediction[0]}")
            



def image():

    # URL you want to embed in the iframe
    tableau_url = "https://public.tableau.com/app/profile/siranjeevi.v/viz/retail_sales_final_guvi_project/Dashboard1?publish=yes"

    
    
    
    # Create a button
    if st.button('Click View Live Dashboard'):
        st.write(f'<a href="{tableau_url}" target="_blank">Click here to open Tableau Visualization</a>', unsafe_allow_html=True)

    st.image('Dashboard 1.png',width=800)
    
    
    st.image('markdown_sales_corr.png',width=800)    
    st.image('corr.png',width=800)
    
    
    
def home():
    st.image('home.jpeg',width=800)
    
# Page navigation
st.sidebar.header("welcome to Retal weekly sale price Pridication", divider='rainbow')
page = st.sidebar.radio("Choose a page",
                            ["Home","Data Analysis using Tableau","weekly sale predication"],index=2)

if page == "weekly sale predication":
    exgboost()
elif page == "Data Analysis using Tableau":
    image()
elif page == "Home":
   home()