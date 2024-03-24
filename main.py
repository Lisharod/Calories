import streamlit as st
import pickle
from PIL import Image

st.set_page_config(
    page_title="Calories Burnt Prediction",
    page_icon="💪",
    layout="wide",
)

# Load the scikit-learn model from the .pkl file
with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Function to make predictions
def make_prediction(age, bmi, duration, heart_rate, body_temperature, gender):
    input_data = [[age, bmi, duration, heart_rate, body_temperature, gender]]
    prediction = loaded_model.predict(input_data)
    return prediction[0]

# Streamlit UI
page = st.sidebar.selectbox("Select Page", ["Home", "Model Info"])

st.markdown(
    """
    <style>
        body {
            background-color: #EDDAD9; /* Background color for the entire app */
            font-family: "Arial", sans-serif;
        }
        .st-bw {
            background-color: #BAACAB;
            color: #ffffff;
        }
        .st-cn {
            background-color: #f0f0f0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
            border-radius: 8px;
            position: relative;
        }
        .st-cn::after {
            content: '\\2193'; /* Unicode arrow-down character */
            font-size: 24px;
            color: #0f0205; /* Color of the arrow */
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if page == "Home":
    def display_image(image_file, width=30):
        image_path = f"{image_file}"
        try:
            image = Image.open(image_path)
            st.image(image, use_column_width=False, width=100)
        except FileNotFoundError:
            st.warning(f"Image not found: {image_path}")
    image_files = ["logo.jpg"]
    for image_file in image_files:
        display_image(image_file, width=30)
    st.title("Calories Burnt Prediction")

    # User input for necessary attributes
    height = st.number_input("Enter Height (in cm):")
    weight = st.number_input("Enter Weight (in kg):")

    age = st.number_input("Enter Age:")
    duration = st.number_input("Enter Exercise Duration (in minutes):")
    heart_rate = st.number_input("Enter Heart Rate (beats per minute):")
    body_temperature = st.number_input("Enter Body Temperature (in Celsius):")
    gender = st.radio("Select Gender:", ["Male", "Female"])
    if gender=="Male":
        gender=1
    else:
        gender=0

    # Button to make prediction
    
    if st.button("Make Prediction"):
        bmi = weight / ((height / 100) ** 2)
        st.write(f"**BMI:** {bmi:.2f}")
        
        prediction = make_prediction(age, bmi, duration, heart_rate, body_temperature, gender)
        st.success(f"Estimated Calories Burnt: {prediction:.2f} calories")
        if 11 <= bmi <= 18.4:
            st.warning("You are underweight.")
            st.warning("Please Follow this routine to gain weight and Include nutrient-dense foods like lean proteins, whole grains, healthy fats, and dairy in your diet to support weight gain in a balanced and sustainable way")
            st.write("Day 1: Push :Barbell bench press,Dumbbell incline press, Dumbbell lateral raises ,Dumbbell tricep extensions ")
            st.write("Day 2: Pull :Barbell bent over rows, Lat pulldowns , Dumbbell upright rows ,Dumbbell single arm bicep curls")
            st.write("Day 3: Legs :Barbell squats , Bulgarian split squat , Leg press ,Leg extensions,Standing calf raises ")
            st.write("Day 4: Push :Push ups, Barbell incline bench press ,Dumbbell shoulder press, Tricep pushdowns")
            st.write("Day 5: Pull :Pull ups, Seated cable row, Face pulls, Barbell bicep curl ")
            st.write("Day 6: Legs :Lunges , Hip thrust , Romanian deadlifts, Glute kickbacks")
            st.write("Day 7: Rest")
        elif 18.5 <= bmi <= 24.9:
            st.success("You have a normal weight.")
            st.success("Please follow this routine to maintain your current weight and include a well-rounded diet that incorporates a variety of fruits, vegetables, lean proteins, whole grains, and moderate portions")
            st.write("Day 1: Push :Barbell bench press ,Barbell military press,Dumbbell incline press, Dumbbell lateral raises,Dumbbell tricep extensions")
            st.write("Day 2: Pull :Barbell deadlifts, Barbell bent over rows, Lat pulldowns, Dumbbell upright rows ,Dumbbell single arm bicep curl")
            st.write("Day 3: Legs :Barbell squats , Bulgarian split squat, Leg press ,Leg extensions,Standing calf raises ")
            st.write("Day 4: Push :Push ups , Barbell incline bench press ,Dumbbell shoulder press , Tricep pushdowns ")
            st.write("Day 5: Pull :Pull ups , Seated cable row , Face pulls , Barbell bicep curl , Barbell good mornings ")
            st.write("Day 6: Legs :Goblet squats , Lunges , Hip thrust , Romanian deadlifts, Glute kickbacks ")
            st.write("Day 7: Rest")
        elif 25 <= bmi <= 100:
            st.error("You are overweight.")
            st.error("Please follow this routine for weight loss and include calorie-controlled diet rich in vegetables, lean proteins, and whole grains. ")
            st.write("Day 1: Push :Barbell bench press , Barbell military press ,Dumbbell incline press , Dumbbell lateral raises ,Dumbbell tricep extensions , along with cardio")
            st.write("Day 2: Pull :Barbell deadlifts, Barbell bent over rows, Lat pulldowns, Dumbbell upright rows ,Dumbbell single arm bicep curls , along with cardio")
            st.write("Day 3: Legs :Barbell squats, Bulgarian split squat, Leg press ,Leg extensions ,Standing calf raises, along with cardio")
            st.write("Day 4: Push :Push ups, Barbell incline bench press,Dumbbell shoulder press, Tricep pushdowns, along with cardio")
            st.write("Day 5: Pull :Pull ups, Seated cable row , Face pulls, Barbell bicep curl, Barbell good mornings ,along with cardio")
            st.write("Day 6: Legs :Goblet squats, Lunges, Hip thrust, Romanian deadlifts, Glute kickbacks ,along with cardio")
            st.write("Day 7: Rest")
        

elif page == "Model Info":
    st.title("Model Information")
    st.write("This page provides information about the model.")

    # Display any additional information about the model
    # For example, you can include model parameters, feature importance, etc.
    st.write("Example model information:")
    st.write("- Model Type: RandomForestRegressor")
    st.write("- Number of Estimators: 100")
    st.write("- Other Model Parameters: ...")
    
    st.subheader("Images in the Directory")
    def display_image(image_file, width=30):
        image_path = f"{image_file}"
        try:
            image = Image.open(image_path)
            st.image(image, caption=f"Exercise columns", use_column_width=True, width=30)
        except FileNotFoundError:
            st.warning(f"Image not found: {image_path}")
    image_files = ["Exercise Columns.png"]
    for image_file in image_files:
        display_image(image_file, width=30)
        
    def display_image(image_file, width=None):
        image_path = f"{image_file}"
        try:
            image = Image.open(image_path)
            st.image(image, caption=f"Datasets overall statistics", use_column_width=True, width=30)
        except FileNotFoundError:
            st.warning(f"Image not found: {image_path}")
    image_files = ["Dataset's Overall Statistic.png"]
    for image_file in image_files:
        display_image(image_file, width=30)
    
    def display_image(image_file, width=None):
        image_path = f"{image_file}"
        try:
            image = Image.open(image_path)
            st.image(image, caption=f"BMI Calculated", use_column_width=True, width=30)
        except FileNotFoundError:
            st.warning(f"Image not found: {image_path}")
    image_files = ["BMI Calculated.png"]
    for image_file in image_files:
        display_image(image_file, width=30)
    
    def display_image(image_file, width=None):
        image_path = f"{image_file}"
        try:
            image = Image.open(image_path)
            st.image(image, caption=f"Box Plot", use_column_width=True, width=30)
        except FileNotFoundError:
            st.warning(f"Image not found: {image_path}")
    image_files = ["Box Plot.png"]
    for image_file in image_files:
        display_image(image_file, width=30)
    
    def display_image(image_file, width=None):
        image_path = f"{image_file}"
        try:
            image = Image.open(image_path)
            st.image(image, caption=f"Categorized BMI Distributed Between age groups", use_column_width=True, width=30)
        except FileNotFoundError:
            st.warning(f"Image not found: {image_path}")
    image_files = ["Categorized_BMI Distributed Between age_groups.png"]
    for image_file in image_files:
        display_image(image_file, width=30)
        
    def display_image(image_file, width=None):
        image_path = f"{image_file}"
        try:
            image = Image.open(image_path)
            st.image(image, caption=f"Categorized BMI", use_column_width=True, width=30)
        except FileNotFoundError:
            st.warning(f"Image not found: {image_path}")
    image_files = ["Categorized_BMI.png"]
    for image_file in image_files:
        display_image(image_file, width=30)
        
    def display_image(image_file, width=None):
        image_path = f"{image_file}"
        try:
            image = Image.open(image_path)
            st.image(image, caption=f"CountPlot of age groups", use_column_width=True, width=30)
        except FileNotFoundError:
            st.warning(f"Image not found: {image_path}")
    image_files = ["CountPlot of age_groups.png"]
    for image_file in image_files:
        display_image(image_file, width=30)
        
    def display_image(image_file, width=None):
        image_path = f"{image_file}"
        try:
            image = Image.open(image_path)
            st.image(image, caption=f"CountPlot of each gender", use_column_width=True, width=30)
        except FileNotFoundError:
            st.warning(f"Image not found: {image_path}")
    image_files = ["CountPlot of each gender.png"]
    for image_file in image_files:
        display_image(image_file, width=30)
    
    def display_image(image_file, width=None):
        image_path = f"{image_file}"
        try:
            image = Image.open(image_path)
            st.image(image, caption=f"Learning Curve", use_column_width=True, width=30)
        except FileNotFoundError:
            st.warning(f"Image not found: {image_path}")
    image_files = ["Learning Curve.png"]
    for image_file in image_files:
        display_image(image_file, width=30)
    
    def display_image(image_file, width=None):
        image_path = f"{image_file}"
        try:
            image = Image.open(image_path)
            st.image(image, caption=f"comparision bar plot graph", use_column_width=True, width=30)
        except FileNotFoundError:
            st.warning(f"Image not found: {image_path}")
    image_files = ["comparision_bar_plot_graph.png"]
    for image_file in image_files:
        display_image(image_file, width=30)
        
    def display_image(image_file, width=None):
        image_path = f"{image_file}"
        try:
            image = Image.open(image_path)
            st.image(image, caption=f"RMSE Comparision graph", use_column_width=True, width=30)
        except FileNotFoundError:
            st.warning(f"Image not found: {image_path}")
    image_files = ["RMSE_graph.png"]
    for image_file in image_files:
        display_image(image_file, width=30)
        
    
# Run the app
