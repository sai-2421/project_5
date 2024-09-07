import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import datetime
import pickle


#set up page configuration for streamlit
st.set_page_config(page_title='HDB Flat Resale Price Predictor',
                   page_icon='house',
                   initial_sidebar_state='expanded',
                   layout='wide')

#css for page setup
st.markdown("""
    <style>
    .main-menu {font-size:20px; margin-top:-40px;}
    .content {padding: 20px;}
    .header {margin-top: 20px; padding-top: 30px; text-align: center; background-color:#002b36; padding-bottom: 10px;}
    </style>
    """, unsafe_allow_html=True)


c1,_,c2=st.columns([2,1,2])
with _:
    st.empty()
    st.image('https://thumbs.dreamstime.com/b/sign-housing-development-board-hdb-singapore-jan-responsible-public-139776292.jpg',width=300)
    st.empty()

#set up the sidebar with optionmenu

selected = option_menu ("Menu",
    options=["Home", "Price Prediction"],
    icons=['house', "lightbulb"],  
    default_index=0, 
    orientation="horizontal",
    styles={
        "container": {"padding": "5px","border": "2px ridge ", "background-color": "#DD1D06"},
        "icon": {"color": 'yellow', "font-size": "25px"},
        "nav-link": {"font-size": "18px","margin": "0px", "--hover-color": "#FFD700"},
        "nav-link-selected": {"background-color":"#46B253"},  
            })

#user input values for selectbox and encoded for respective features
class option:

    option_months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

    encoded_month= {"January" : 1,"February" : 2,"March" : 3,"April" : 4,"May" : 5,"June" : 6,"July" : 7,"August" : 8,"September" : 9,
            "October" : 10 ,"November" : 11,"December" : 12}

    option_town=['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH','BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI',
        'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST','KALLANG/WHAMPOA', 'MARINE PARADE', 'QUEENSTOWN', 'SENGKANG','SERANGOON',
        'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN','LIM CHU KANG', 'SEMBAWANG', 'BUKIT PANJANG', 'PASIR RIS','PUNGGOL']
    
    encoded_town={'ANG MO KIO' : 0 ,'BEDOK' : 1,'BISHAN' : 2,'BUKIT BATOK' : 3,'BUKIT MERAH' : 4,'BUKIT PANJANG' : 5,'BUKIT TIMAH' : 6,
        'CENTRAL AREA' : 7,'CHOA CHU KANG' : 8,'CLEMENTI' : 9,'GEYLANG' : 10,'HOUGANG' : 11,'JURONG EAST' : 12,'JURONG WEST' : 13,
        'KALLANG/WHAMPOA' : 14,'LIM CHU KANG' : 15,'MARINE PARADE' : 16,'PASIR RIS' : 17,'PUNGGOL' : 18,'QUEENSTOWN' : 19,
        'SEMBAWANG' : 20,'SENGKANG' : 21,'SERANGOON' : 22,'TAMPINES' : 23,'TOA PAYOH' : 24,'WOODLANDS' : 25,'YISHUN' : 26}
    
    option_flat_type=['1 ROOM', '2 ROOM','3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE','MULTI-GENERATION']

    encoded_flat_type={'1 ROOM': 0,'2 ROOM' : 1,'3 ROOM' : 2,'4 ROOM' : 3,'5 ROOM' : 4,'EXECUTIVE' : 5,'MULTI-GENERATION' : 6}

    option_flat_model=['2-ROOM','3GEN','ADJOINED FLAT', 'APARTMENT' ,'DBSS','IMPROVED' ,'IMPROVED-MAISONETTE', 'MAISONETTE',
                    'MODEL A', 'MODEL A-MAISONETTE','MODEL A2' ,'MULTI GENERATION' ,'NEW GENERATION', 'PREMIUM APARTMENT',
                    'PREMIUM APARTMENT LOFT', 'PREMIUM MAISONETTE','SIMPLIFIED', 'STANDARD','TERRACE','TYPE S1','TYPE S2']

    encoded_flat_model={'2-ROOM' : 0,'3GEN' : 1,'ADJOINED FLAT' : 2,'APARTMENT' : 3,'DBSS' : 4,'IMPROVED' : 5,'IMPROVED-MAISONETTE' : 6,
                'MAISONETTE' : 7,'MODEL A' : 8,'MODEL A-MAISONETTE' : 9,'MODEL A2': 10,'MULTI GENERATION' : 11,'NEW GENERATION' : 12,
                'PREMIUM APARTMENT' : 13,'PREMIUM APARTMENT LOFT' : 14,'PREMIUM MAISONETTE' : 15,'SIMPLIFIED' : 16,'STANDARD' : 17,
                'TERRACE' : 18,'TYPE S1' : 19,'TYPE S2' : 20}
    

#set up information for the 'get prediction' menu

if selected == "Price Prediction":
    st.write('')
    st.markdown("<h5 style=color:red>Please Fill in the Following Information to Predict the Resale Price of a Flat :",unsafe_allow_html=True)
    st.write('')

    # created form to get the user input 
    with st.form('prediction'):
        col1,col2=st.columns(2)
        with col1:

            user_month=st.selectbox(label='Month',options=option.option_months,index=None)

            user_town=st.selectbox(label='Town',options=option.option_town,index=None)

            user_flat_type=st.selectbox(label='Flat Type',options=option.option_flat_type,index=None)

            user_flat_model=st.selectbox(label='Flat Model',options=option.option_flat_model,index=None)

            floor_area_sqm=st.number_input(label='Floor area sqm',min_value=10.0)

            price_per_sqm=st.number_input(label='Price Per sqm',min_value=100.00)


        
        with col2:

            year=st.text_input(label='year',max_chars=4)

            block=st.text_input(label='Block',max_chars=3)

            lease_commence_date=st.text_input(label='Year of lease commence',max_chars=4)

            remaining_lease=st.number_input(label='Remaining lease year',min_value=0,max_value=99)

            years_holding=st.number_input(label='Years Holding',min_value=0,max_value=99)

            c1,c2=st.columns(2)

            with c1:
                storey_start=st.number_input(label='Storey start',min_value=1,max_value=50)

            with c2:
                storey_end=st.number_input(label='Storey end',min_value=1,max_value=51)
            
            st.markdown('<br>', unsafe_allow_html=True)

            button=st.form_submit_button('PREDICT',use_container_width=True)

        if button:
            with st.spinner("Predicting..."):

            #check whether user fill all required fields
                if not all([user_month,user_town,user_flat_type,user_flat_model,floor_area_sqm,price_per_sqm,year,block,
                        lease_commence_date,remaining_lease,years_holding,storey_start,storey_end]):
                    st.error("Please fill in all required fields.")


                else:
                #create features from user input 
                    current_year=datetime.datetime.now().year

                current_remaining_lease=remaining_lease-(current_year-(int(year)))
                age_of_property=current_year-int(lease_commence_date)


                month=option.encoded_month[user_month]
                town=option.encoded_town[user_town]
                flat_type=option.encoded_flat_type[user_flat_type]
                flat_model=option.encoded_flat_model[user_flat_model]

                floor_area_sqm_log=np.log(floor_area_sqm)
                remaining_lease_log=np.log1p(remaining_lease)
                price_per_sqm_log=np.log(price_per_sqm)


                # opened pickle model and predict the resale price with user data
                with open('RandomForestRegressor','rb') as files:
                    model=pickle.load(files)
                
                user_data=np.array([[month, town, flat_type, block, flat_model, lease_commence_date, year, storey_start,
                                    storey_end, years_holding, current_remaining_lease, age_of_property, floor_area_sqm_log, 
                                    remaining_lease_log,price_per_sqm_log ]])

                predict=model.predict(user_data)
                resale_price=np.exp(predict[0])

                #display the predicted selling price 
                st.subheader(f"Predicted Resale price is: :green[{resale_price:.2f}]")

# set up the information for 'Home' menu
if selected == "Home":

    # Main header
    st.markdown("<h1 style='text-align: center;'>Welcome to the Housing & Development Board (HDB)</h1>", unsafe_allow_html=True)

    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#4682b4">HDB</h3>', unsafe_allow_html=True)
    st.markdown('''<p style='font-size:16px; color:#9e9e9e; line-height:1.6'>
                    The Housing & Development Board (HDB), also known as the Housing Board, operates under the Ministry of National Development and oversees public housing in Singapore. Established in 1960, HDB's early efforts were concentrated on providing emergency housing and resettling kampong (village) residents. Over the years, it has implemented various upgrading initiatives and introduced diverse housing options tailored to different income brackets.
                </p>
                ''', unsafe_allow_html=True)
    
      # History section
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#4682b4">History of HDB</h3>', unsafe_allow_html=True)
    st.markdown('''<ul style='font-size:16px; color:#9e9e9e; line-height:1.6'>
                  <li>In the mid-20th century, Singapore underwent a period of rapid demographic expansion, with its population soaring from 940,700 to 1.7 million between 1947 and 1957.</li>
                  <li>This population boom exacerbated already precarious living conditions, forcing many residents into overcrowded shophouses and informal settlements.</li>
                  <li>The Singapore Improvement Trust (SIT), responsible for public housing at the time, struggled with financial sustainability due to low rental rates that were impractical for upkeep and yet unaffordable for the city's poorer inhabitants.</li>
                  <li>By 1958, delays in approving new housing projects had significantly hampered construction efforts.</li>
                  <li>Responding to mounting challenges, the government initiated reforms in the mid-1950s, culminating in the Housing and Development Bill.</li>
                  <li>Passed in 1959, this legislation paved the way for the establishment of the Housing & Development Board (HDB) in February 1960, marking a pivotal moment in Singapore's approach to public housing.</li>
              </ul>
              ''', unsafe_allow_html=True)
    

    with st.container():
     cl,c2,c3=st.columns(3)
     
    with cl:
        st.subheader(':blue[Impact on Community]')
        st.markdown('''<p style='font-size:16px; color:#9e9e9e; line-height:1.6'>
                            HDB has played a pivotal role in shaping Singapore's social fabric by providing affordable, quality housing for all segments of the population. 
                            Its initiatives have fostered cohesive communities and improved the overall quality of life for residents.
                        </p>
                        ''', unsafe_allow_html=True)
        
    with c2:
        st.subheader(':blue[Achievements]')
        st.markdown('''<p style='font-size:16px; color:#9e9e9e; line-height:1.6'>
                    Over the decades, HDB has achieved significant milestones in transforming Singapore's housing landscape. 
                    This includes the successful resettlement of kampong residents into public housing, introduction of upgrading programs, and sustainable urban planning initiatives.
                </p>
                ''', unsafe_allow_html=True)
        

    with c3:
        st.subheader(':blue[Future Directions]')
        st.markdown('''<p style='font-size:16px; color:#9e9e9e; line-height:1.6'>
                            Looking forward, HDB continues to innovate in urban planning, sustainability, and community development. 
                            Future projects aim to enhance living environments, promote inclusivity, and meet the evolving needs of Singapore's diverse population.
                        </p>
                        ''', unsafe_allow_html=True)
        

    c1,c2,c3,=st.columns(3)     
    with c1:
        st.image('https://upload.wikimedia.org/wikipedia/commons/9/9d/Hdb123.jpg',use_column_width=True)
    with c2:
        st.image('https://upload.wikimedia.org/wikipedia/commons/9/91/Hdb-resale.jpg',use_column_width=True)
    with c3:
        st.image('https://upload.wikimedia.org/wikipedia/commons/b/b6/Hdb369.jpg',use_column_width=True)


    st.link_button(label='Official Website',url='https://www.hdb.gov.sg/cs/infoweb/homepage',use_container_width=True)