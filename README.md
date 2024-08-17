# WEB SCRAPING WITH STREAMLIT APPLICATION

## Project Description

This project is a web scraping application developed using Streamlit and Python. The application scrapes doctor profiles from Practo based on user-provided location and specialization. It extracts information such as doctor's name, specialization, experience, clinic name, and consultation fees. The results are displayed in a user-friendly format within the Streamlit app.

## Installation Instructions

To set up and run the application, follow these steps:

1. **Install Python**: Make sure you have Python 3.7 or later installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**: Install the necessary Python libraries by running the following commands in your terminal or command prompt:

    ```bash
    pip install streamlit
    pip install requests
    pip install beautifulsoup4
    ```

3. **Download the Project**: Clone or download the project repository from [GitHub](https://github.com/your-repo/your-project).

4. **Navigate to the Project Directory**: Open your terminal or command prompt and navigate to the directory where the project files are located.

    ```bash
    cd path/to/your-project
    ```

5. **Run the Application**: Start the Streamlit application using the following command:

    ```bash
    streamlit run app.py
    ```

## Usage

1. **Open the Application**: After running the command above, your default web browser should automatically open and display the Streamlit app. If not, you can access it at `http://localhost:8501` in your web browser.

2. **Input Location and Specialization**: 
    - In the sidebar, enter the location (e.g., Bangalore) in the text input field.
    - Select the specialization from the dropdown list.

3. **Start Scraping**: Click the "Scrape" button to begin the web scraping process.

## Output

After scraping, the application will display the following:

- **Total Number of Doctor Profiles**: A message showing the total number of doctor profiles available based on your search criteria.
- **Doctor Profiles**: A list of doctor profiles with the following details for each doctor:
  - Name
  - Specialization
  - Experience
  - Clinic Name
  - Consultation Fees

The results are shown in a series of "doctor cards" within the Streamlit application interface.

## Contact

For any questions or feedback, please contact [HIMANSHU SRIVASTAV](mailto:hsrivastavsans@gmail.com)
