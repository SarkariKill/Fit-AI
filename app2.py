import subprocess
environment_build_command = "pip install -r requirements.txt"
subprocess.run(environment_build_command.split(" "))

import json
import streamlit as st
import cv2
import mediapipe as mp
from PIL import Image
from streamlit_lottie import st_lottie 
import numpy as np

# Navigation Bar
# Define the navigation options
nav_options = {
    "Home": "Home",
    "Rep Counter": "Rep Counter",
    "Documentation": "Documentation", 
    "About": "About"
}

#For Lootie Aimation
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)
    
# Create a sidebar with a selectbox for navigation
selected_page = st.sidebar.selectbox("Navigation", list(nav_options.keys()))

# Display content based on the selected page
if selected_page == "Home":
    # Title Of The Website
    st.markdown("""
        <style>
            .title {
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Fit AI</h1>", unsafe_allow_html=True)
    #Lottie
    lottie_scanner = load_lottiefile("lottie/home.json")
    st_lottie(
        lottie_scanner,
        key = "None",
    )
    
    st.markdown("""

Welcome to **Fit AI**, your personal fitness companion powered by artificial intelligence! Whether you're a fitness enthusiast or just getting started on your journey to better health, Fit AI is here to help you achieve your fitness goals effectively and intelligently.

### How It Works

1. **Select Your Exercise**: Choose the exercise you want to perform from the dropdown menu below.
2. **Start Your Workout**: Once you've selected an exercise, position yourself in front of your webcam and start your workout.
3. **Track Your Reps**: Our advanced computer vision technology will count the number of repetitions you perform, ensuring you maintain proper form and get the most out of your exercise.
4. **Run Checkbox**: Click on the **RUN** checkbox to start your workout. To stop and start again, simply click on the **RUN** checkbox again.

### Supported Exercises

Our Rep Counter currently supports the following exercises:
- **Curls**: Great for building bicep strength.
- **Jumping Jacks**: A fantastic full-body exercise to get your heart rate up.
- **Pushups**: Essential for building upper body strength and core stability.
- **Squats**: Ideal for strengthening the lower body and core.
- **Planks**: Excellent for improving core strength and stability.
- **Crunches**: Another great exercise for the abs.

Get ready to take your fitness to the next level with our Rep Counter tool!

### Get Started

Experience the future of fitness with Fit AI. Start your journey today towards a healthier, fitter you!

---

                """)
    
    
# Add content for home page
elif selected_page == "About":
    # Title Of The Website
    st.markdown("""
        <style>
            .title {
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)
    st.markdown("<h1 class='title'>About</h1>", unsafe_allow_html=True)
    #Lottie
    lottie_scanner = load_lottiefile("lottie/about.json")
    st_lottie(
        lottie_scanner,
        key = "None",
    )
    st.markdown("""

Hello, I'm **Aditya Sarkar**, the creator of Fit AI.

### Why I Created Fit AI

As a fitness enthusiast passionate about leveraging technology for personal health improvement, I created Fit AI to revolutionize how individuals approach fitness tracking and exercise performance assessment. With a background in machine learning and a deep interest in health and wellness, I saw an opportunity to merge these passions into a single, user-friendly platform.

### Our Mission

Fit AI is dedicated to empowering users on their fitness journeys by providing accurate and insightful workout analysis. Whether you're a beginner looking to start your fitness routine or a seasoned athlete aiming to optimize performance, Fit AI aims to provide the tools and insights needed to achieve your goals effectively.

### How It Works

Fit AI utilizes cutting-edge computer vision techniques to analyze exercise movements in real-time. By capturing and interpreting body movements through a camera feed, the app accurately counts repetitions, tracks exercise form, and offers personalized feedback to improve workout effectiveness.

## Contact Information

I welcome your feedback and suggestions to continually enhance Fit AI. Feel free to reach out to me through the following channels:

- **Email**: adi.sarkar2004@gmail.com
- **Phone**: +91 8989028700

                """)
 
elif selected_page == "Documentation":
       # Title Of The Website
       st.markdown("""
        <style>
            .title {
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)
       st.markdown("<h1 class='title'>Documentation</h1>", unsafe_allow_html=True)
            #Lottie
       lottie_scanner = load_lottiefile("lottie/documentation.json")
       st_lottie(
            lottie_scanner,
            key = "None",
        )
       st.markdown("""
                   ### Libraries Used

The project utilizes several libraries to enable various functionalities:

- **json**: Used for handling JSON files, particularly for loading Lottie animation files.
- **streamlit**: A web application framework used for building interactive web applications with Python.
- **cv2 (OpenCV)**: A library mainly used for computer vision tasks, such as capturing and processing webcam images.
- **mediapipe**: A machine learning library for building perception pipelines, used here for pose detection.
- **PIL (Image)**: Python Imaging Library used here to load and display images within the Streamlit application.
- **numpy**: Essential for numerical operations, especially useful for array manipulations in image processing.

### Project Overview

The Fit AI project is a web application designed to assist users in tracking their exercise repetitions using computer vision technology. Here's how you structured the project:

1. **Navigation Bar**: 
   - Created a sidebar with navigation options ("Home", "Rep Counter", "Documentation", "About").
   - Based on the selected page, different content is displayed.

2. **Pages and Content**:
   - **Home Page**: Provides an introduction to Fit AI, explaining its features and how it helps users achieve fitness goals using AI-powered technology.
   - **About Page**: Shares information about the creator (Aditya Sarkar) and the motivation behind developing Fit AI.
   - **Rep Counter Page**: Allows users to select different exercises (e.g., Curls, Jumping Jacks, Pushups) and uses computer vision (mediapipe) to count repetitions based on pose detection.

3. **Exercise Specific Logic**:
   - Each exercise (e.g., Curls, Jumping Jacks, Pushups) has its dedicated section with:
     - Description of the exercise and muscle groups targeted.
     - Instructions on how to perform the exercise.
     - An image illustrating the exercise technique.
     - Computer vision logic using mediapipe to detect and count repetitions based on pose landmarks.
     - Displaying real-time webcam feed with overlaid pose landmarks and rep counter.

4. **Real-time Interaction**:
   - Uses checkboxes (`st.checkbox`) to start and stop the exercise detection loop.
   - Captures webcam frames (`cv2.VideoCapture`) and processes them using mediapipe for pose detection.
   - Updates the Streamlit interface in real-time (`st.image`) with annotated frames showing exercise technique and current rep count.

This structure ensures that users can interactively select exercises, receive real-time feedback on their performance, and learn proper exercise techniques through visual and textual instructions.

This project effectively integrates computer vision (mediapipe), web application development (Streamlit), and libraries for image processing and user interface management to create an engaging and functional fitness tracking tool.

                   """)

elif selected_page == "Rep Counter":
    # Title Of The Website
    st.markdown("""
        <style>
            .title {
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Reps Counter</h1>", unsafe_allow_html=True)
    lottie_scanner = load_lottiefile("lottie/repcounter.json")
    st_lottie(
            lottie_scanner,
            key = "None",
        )
    st.markdown("""

Welcome to the Rep Counter page of Fit AI! This page is designed to help you track your exercise repetitions accurately using your webcam. Whether you're working on building muscle, improving endurance, or just staying active, our Rep Counter tool is here to assist you in achieving your fitness goals.

""")
     # Dropdown menu for selecting an exercise
    exercise = st.selectbox(
        "Select the exercise you want to perform:",
        ("Curls", "Jumping Jacks", "Pushups","Shoulder Press", "Squats", "Crunches")
    )
    
    
    def calculate_angle(a, b, c):
        a = np.array(a)  # First point
        b = np.array(b)  # Mid point
        c = np.array(c)  # End point
        
        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(radians * 180.0 / np.pi)
        
        if angle > 180.0:
            angle = 360 - angle
            
        return angle
    
    if exercise == "Curls":
        st.markdown("""
### Curls

**Muscle Groups Targeted**: Biceps

**Description**: Curls are a fundamental exercise for building and strengthening your biceps. They can be performed with dumbbells, a barbell, or resistance bands.

**How to Perform**:
1. Stand with your feet shoulder-width apart, holding a weight in each hand.
2. Keep your elbows close to your torso and curl the weights while contracting your biceps.
3. Continue to raise the weights until your biceps are fully contracted and the weights are at shoulder level.
4. Slowly lower the weights back to the starting position.
""")
        st.image('images/curls.png', caption='Curls')
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        
            # Curls Code
        run = st.checkbox('**Run**')
        FRAME_WINDOW = st.image([])

        cap = cv2.VideoCapture(0)

        counter = 0
        stage = None

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while run:
                ret, frame = cap.read()
                if not ret:
                    st.write("Failed to grab frame")
                    break
                
                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to RGB
                image.flags.writeable = True

                # Render detections
                if results.pose_landmarks:
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                    # Extract landmarks
                    landmarks = results.pose_landmarks.landmark

                    # Get coordinates of shoulder, elbow, and wrist
                    left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                    landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                    left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                                landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                    left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                                landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                    right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                    landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                    right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                                landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                    right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                                landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                    # Calculate angles
                    left_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)
                    right_angle = calculate_angle(right_shoulder, right_elbow, right_wrist)

                    # Curl counter logic
                    if left_angle > 160 and right_angle > 160:
                        stage = "down"
                    if left_angle < 30 and right_angle < 30 and stage == 'down':
                        stage = "up"
                        counter += 1

                    # Draw text on the image
                    cv2.putText(image, f"Reps: {counter}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

                # Display the frame in Streamlit
                FRAME_WINDOW.image(image)

        cap.release()
        cv2.destroyAllWindows()
    
    elif exercise == "Jumping Jacks":
        st.markdown("""

### Jumping Jacks

**Muscle Groups Targeted**: Full Body, with emphasis on legs, arms, and core

**Description**: Jumping jacks are a full-body aerobic exercise that increases your heart rate and helps improve cardiovascular fitness.

**How to Perform**:
1. Stand upright with your legs together and arms at your sides.
2. Jump up, spreading your legs to about shoulder-width apart while simultaneously bringing your arms above your head.
3. Jump again to return to the starting position.
    """)
        st.image('images/jumping_jacks.png', caption='Jumping Jacks')
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        
            # Curls Code
        run = st.checkbox('Run')
        FRAME_WINDOW = st.image([])

        cap = cv2.VideoCapture(0)

        counter = 0
        stage = None

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while run:
                ret, frame = cap.read()
                if not ret:
                    st.write("Failed to grab frame")
                    break
                
                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to RGB
                image.flags.writeable = True

                # Render detections
                if results.pose_landmarks:
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                    # Extract landmarks
                    landmarks = results.pose_landmarks.landmark

                            # Get coordinates of shoulder, elbow, and wrist
                    left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                    left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                    left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                    
                    # Get coordinates of shoulder, elbow, and wrist
                    right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                            landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                    right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                    right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]

                    # Calculate angles
                    left_angle = calculate_angle(left_wrist,left_shoulder,left_hip)
                    right_angle = calculate_angle(right_wrist,right_shoulder,right_hip)

                    # Jumping Jacks Logic
                    if left_angle < 45 and right_angle < 45:
                        stage = "down"
                    if left_angle > 90 and right_angle >90 and stage == 'down':
                        stage = "up"
                        counter += 1

                    # Draw text on the image
                    cv2.putText(image, f"Reps: {counter}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

                # Display the frame in Streamlit
                FRAME_WINDOW.image(image)

        cap.release()
        cv2.destroyAllWindows()
    
    elif exercise == "Pushups":
        st.markdown("""


### Pushups

**Muscle Groups Targeted**: Chest, Shoulders, Triceps, Core

**Description**: Pushups are a classic bodyweight exercise that builds upper body strength and core stability.

**How to Perform**:
1. Start in a plank position with your hands slightly wider than shoulder-width apart.
2. Lower your body until your chest nearly touches the floor, keeping your elbows close to your body.
3. Push yourself back up to the starting position.
 """)
        st.image('images/Push Ups.png', caption='Pushups')
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        
            # Curls Code
        run = st.checkbox('Run')
        FRAME_WINDOW = st.image([])

        cap = cv2.VideoCapture(0)

        counter = 0
        stage = None

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while run:
                ret, frame = cap.read()
                if not ret:
                    st.write("Failed to grab frame")
                    break
                
                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to RGB
                image.flags.writeable = True

                # Render detections
                if results.pose_landmarks:
                    landmarks = results.pose_landmarks.landmark
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                            # Get coordinates of shoulder, elbow, and wrist
                    right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                            landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                    right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                                landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                    right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                            landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                    
                    # Get coordinates of shoulder, elbow, and wrist
                    left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                    left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                                landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                    left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                
                            # Calculate angle between the shoulder, elbow, and wrist
                    left_angle = calculate_angle(left_wrist,left_elbow,left_shoulder)
                    right_angle = calculate_angle(right_wrist,right_elbow,right_shoulder)

                    # Jumping Jacks Logic
                    if left_angle < 100 and right_angle < 100:
                        stage = "down"
                    if left_angle >170 and right_angle > 170 and stage == 'down':
                        stage = "up"
                        counter += 1

                    # Draw text on the image
                    cv2.putText(image, f"Reps: {counter}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

                # Display the frame in Streamlit
                FRAME_WINDOW.image(image)

        cap.release()
        cv2.destroyAllWindows()

    elif exercise == "Shoulder Press":
        st.markdown("""
    ### Shoulder Press

**Muscle Groups Targeted**: Shoulders, Triceps

**Description**: The shoulder press is an excellent exercise for building shoulder strength and size. It can be performed with dumbbells, a barbell, or a machine.

**How to Perform**:
1. Sit or stand with a weight in each hand at shoulder height.
2. Press the weights overhead until your arms are fully extended.
3. Lower the weights back to the starting position.
                """)
        st.image('images/shoulder_press.png', caption='Shoulder Press')
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        
            # Curls Code
        run = st.checkbox('Run')
        FRAME_WINDOW = st.image([])

        cap = cv2.VideoCapture(0)

        counter = 0
        stage = None

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while run:
                ret, frame = cap.read()
                if not ret:
                    st.write("Failed to grab frame")
                    break
                
                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to RGB
                image.flags.writeable = True

                # Render detections
                if results.pose_landmarks:
                    landmarks = results.pose_landmarks.landmark
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                            # Get coordinates of shoulder, elbow, and wrist
                    right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                            landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                    right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                                landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                    right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                            landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                    
                    # Get coordinates of shoulder, elbow, and wrist
                    left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                    left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                                landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                    left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                
                            # Calculate angle between the shoulder, elbow, and wrist
                    left_angle = calculate_angle(left_wrist,left_elbow,left_shoulder)
                    right_angle = calculate_angle(right_wrist,right_elbow,right_shoulder)

                    # Jumping Jacks Logic
                    if left_angle < 110 and right_angle < 110:
                        stage = "down"
                    if left_angle >165 and right_angle > 165 and stage == 'down':
                        stage = "up"
                        counter += 1

                    # Draw text on the image
                    cv2.putText(image, f"Reps: {counter}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

                # Display the frame in Streamlit
                FRAME_WINDOW.image(image)

        cap.release()
        cv2.destroyAllWindows()
      
    elif exercise == "Squats":
        st.markdown("""
### Squats

**Muscle Groups Targeted**: Quads, Hamstrings, Glutes, Core

**Description**: Squats are a powerful exercise for building lower body strength and improving core stability.

**How to Perform**:
1. Stand with your feet shoulder-width apart.
2. Lower your body by bending your knees and hips as if you are sitting back into a chair.
3. Keep your chest up and your back straight.
4. Push through your heels to return to the starting position.
 """)
        st.image('images/squats.png', caption='Squats')
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        
            # Curls Code
        run = st.checkbox('Run')
        FRAME_WINDOW = st.image([])

        cap = cv2.VideoCapture(0)

        counter = 0
        stage = None

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while run:
                ret, frame = cap.read()
                if not ret:
                    st.write("Failed to grab frame")
                    break
                
                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to RGB
                image.flags.writeable = True

                # Render detections
                if results.pose_landmarks:
                    landmarks = results.pose_landmarks.landmark
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                            # Get coordinates of hip, knee, and ankle
                    right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                                landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                    right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                                landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                    right_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                                landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

                    left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                                landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                    left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                                landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                    left_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                                landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                                    
                            # Calculate angle between the shoulder, elbow, and wrist
                    left_angle = calculate_angle(left_hip,left_knee,left_ankle)
                    right_angle = calculate_angle(right_hip,right_knee,right_ankle)

                    # Jumping Jacks Logic
                    if left_angle < 90 and right_angle < 90:
                        stage = "down"
                    if left_angle >165 and right_angle > 165 and stage == 'down':
                        stage = "up"
                        counter += 1

                    # Draw text on the image
                    cv2.putText(image, f"Reps: {counter}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

                # Display the frame in Streamlit
                FRAME_WINDOW.image(image)

        cap.release()
        cv2.destroyAllWindows()
    
    # Unstable Exercise
    elif exercise == "Crunches":
         st.markdown("""
   ### Crunches

**Muscle Groups Targeted**: Abdominals

**Description**: Crunches are a popular abdominal exercise that helps build core strength and definition.

**How to Perform**:
1. Lie on your back with your knees bent and feet flat on the floor.
2. Place your hands behind your head, elbows pointing outwards.
3. Lift your upper body towards your knees by contracting your abdominal muscles.
4. Lower yourself back to the starting position.
                """)
         st.image('images/crunches.png', caption='Crunches')
         mp_drawing = mp.solutions.drawing_utils
         mp_pose = mp.solutions.pose
        
            # Curls Code
         run = st.checkbox('Run')
         FRAME_WINDOW = st.image([])

         cap = cv2.VideoCapture(0)

         counter = 0
         stage = None
 
         with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
             while run:
                ret, frame = cap.read()
                if not ret:
                    st.write("Failed to grab frame")
                    break
                
                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to RGB
                image.flags.writeable = True

                # Render detections
                if results.pose_landmarks:
                    landmarks = results.pose_landmarks.landmark
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                                        # To get right shoulder, right hip, and right knee
                    right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                    landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                    right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                                landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                    right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                                landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]

                    # To get left shoulder, left hip, and left knee
                    left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                    landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                    left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                                landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                    left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                                landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                                                        
                            # Calculate angle between the shoulder, elbow, and wrist
                    left_angle = calculate_angle(left_shoulder,left_hip,left_knee)
                    right_angle = calculate_angle(right_shoulder,right_hip,right_knee)

                    # Jumping Jacks Logic
                    if left_angle < 145 and right_angle < 145:
                        stage = "down"
                    if left_angle <80 and right_angle > 80 and stage == 'down':
                        stage = "up"
                        counter += 1

                    # Draw text on the image
                    cv2.putText(image, f"Reps: {counter}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

                # Display the frame in Streamlit
                FRAME_WINDOW.image(image)
                
         cap.release()
         cv2.destroyAllWindows()


#Footer
st.markdown("""
    <style>
        .social-icons {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px; /* Adjust the gap between icons if needed */
        }
        .social-icons .icon {
            margin: 0 10px;
        }
    </style>
    <div class="social-icons">
        <a href="https://www.linkedin.com/in/aditya-sarkar-a7a321206/" target="_blank" class="icon">
            <img src="https://img.icons8.com/color/48/000000/linkedin.png"/>
        </a>
        <a href="https://www.instagram.com/adi_jong_un/" target="_blank" class="icon">
            <img src="https://img.icons8.com/color/48/000000/instagram-new.png"/>
        </a>
        <a href="https://github.com/SarkariKill" target="_blank" class="icon">
            <img src="https://img.icons8.com/material-rounded/48/000000/github.png"/>
        </a>
    </div>
    """, unsafe_allow_html=True)


# Display footer line using st.markdown
st.markdown("---")
st.markdown("Step into a fitter future with Fit AI – where precision meets progress for your ultimate fitness journey!")





      
