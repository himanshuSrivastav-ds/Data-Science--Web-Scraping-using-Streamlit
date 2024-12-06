import streamlit as st
import requests
from bs4 import BeautifulSoup
import urllib.parse

def scrape_practo(location, specialization):
    specialization_query = urllib.parse.quote(f'[{{"word":"{specialization}","autocompleted":true,"category":"subspeciality"}}]')
    base_url = f"https://www.practo.com/search/doctors?results_type=doctor&q={specialization_query}&city={location}&page="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    doctors = []
    page = 1
    
    while True:
        url = base_url + str(page)
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            break  
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        if page == 1:
            doctor_count_tag = soup.find("h1", class_="u-xx-large-font u-bold")
            if doctor_count_tag:
                doctor_count_text = doctor_count_tag.text.strip()
            else:
                doctor_count_text = "No doctors found or the element could not be located."
        
        doctor_elements = soup.find_all("div", class_="info-section")  
        
        if not doctor_elements:
            break  
        
        for element in doctor_elements:
            name_tag = element.find("h2", {"data-qa-id": "doctor_name"})
            name = name_tag.text.strip() if name_tag else "Name not found"
            
            specialization_tag = element.find("div", class_="u-d-flex")
            specialization_text = specialization_tag.text.strip() if specialization_tag else "Specialization not found"
            
            experience_tag = element.find("div", {"data-qa-id": "doctor_experience"})
            experience = experience_tag.text.strip() if experience_tag else "Experience not found"
            
            clinic_name_tag = element.find("span", {"data-qa-id": "doctor_clinic_name"})
            clinic_name = clinic_name_tag.text.strip() if clinic_name_tag else "Clinic name not found"

            practice_locality_tag = element.find("span", {"data-qa-id": "practice_locality"})
            practice_locality = practice_locality_tag.text.strip() if practice_locality_tag else "Practice locality not found"
            
            consultation_fees_tag = element.find("span", {"data-qa-id": "consultation_fee"})
            consultation_fees = consultation_fees_tag.text.strip() if consultation_fees_tag else "Consultation fee not found"
            
            doctors.append({
                "name": name,
                "specialization": specialization_text,
                "experience": experience,
                "clinic_name": clinic_name,
                "practice_locality": practice_locality,
                "consultation_fees": consultation_fees
            })
        
        page += 1  

    return doctor_count_text, doctors

st.set_page_config(page_title="Practo Doctor Scraper🩺", page_icon="🩺", layout="wide")


st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #e9f5f9; /* Light Blue */
        }
        .stApp {
            background-color: #e9f5f9; /* Light Blue */
        }
        .css-1d391kg {
            background-color: #007bff; /* Primary Blue */
            color: white;
        }
        .css-1d391kg .stTextInput input, .css-1d391kg .stSelectbox select {
            width: 100%;
            margin-bottom: 10px;
            padding: 10px;
            border-radius: 8px;
            border: none;
            background-color: #ffffff; /* White */
        }
        .css-1d391kg .stButton button {
            background-color: #28a745; /* Success Green */
            color: white;
            padding: 10px 24px;
            border-radius: 8px;
            margin: auto;
            display: block;
            font-size: 16px;
        }
        .css-1d391kg .stButton button:hover {
            background-color: #218838; /* Darker Green */
        }
        .main-content {
            background-color: #ffffff; /* White */
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin: 20px;
        }
        .doctor-card {
            background-color: #f7f7f7; /* Light Gray */
            border: 1px solid #e1e1e1;
            border-radius: 8px;
            padding: 15px;
            margin: 10px 0;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .doctor-card h2 {
            color: #007bff; /* Primary Blue */
        }
        .doctor-card .details {
            color: #555;
        }
        .stTitle, .stSubheader {
            color: #007bff; /* Primary Blue */
        }
        .stWarning {
            color: #e74c3c; /* Red */
        }
        .stSuccess {
            color: #2ecc71; /* Green */
        }
        .stMarkdown {
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.header("Search Parameters")
location = st.sidebar.text_input("Enter Location (e.g., Bangalore):")
specializations = [
    "Cardiologist",
    "Dentist",
    "Dermatologist",
    "ENT Specialist",
    "General Physician",
    "Gynecologist",
    "Neurologist",
    "Orthopedic",
    "Pediatrician",
    "Psychiatrist",
    "Radiologist",
    "Urologist"
]
specialization = st.sidebar.selectbox("Select Specialization:", specializations)

st.title("Practo Doctor Scraper🩺")
st.markdown("### Find Doctors in Your Area")

with st.container():
    st.markdown("""
        <div class="main-content">
            This tool allows you to search for doctors based on location and specialization. 
            Enter the details in the sidebar, and click "Scrap" to view the results.
        </div>
    """, unsafe_allow_html=True)

    if st.sidebar.button("Scrape"):
        if location and specialization:
            with st.spinner("Scraping data from Practo..."):
                doctor_count, doctors = scrape_practo(location, specialization)
                st.success(f"Total number of doctor profiles available: {doctor_count}")
                
                if doctors:
                    st.subheader("Doctor Profiles")
                    for doctor in doctors:
                        st.markdown(f"""
                            <div class="doctor-card">
                                <h2>{doctor['name']}</h2>
                                <p class="details"><strong>Specialization:</strong> {doctor['specialization']}</p>
                                <p class="details"><strong>Experience:</strong> {doctor['experience']}</p>
                                <p class="details"><strong>Clinic Name:</strong> {doctor['clinic_name']}</p>
                                <p class="details"><strong>Practice Locality:</strong> {doctor['practice_locality']}</p>
                                <p class="details"><strong>Consultation Fees:</strong> {doctor['consultation_fees']}</p>
                            </div>
                        """, unsafe_allow_html=True)
                else:
                    st.warning("No doctor profiles found.")
        else:
            st.error("Please enter both location and specialization.")

st.markdown("----")
st.markdown("Created by HIMANSHU SRIVASTAV")
