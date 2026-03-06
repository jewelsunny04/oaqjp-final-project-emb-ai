# Emotion Detector – AI Web Application

## Project Overview

This project is an AI-based web application that detects emotions from text using the **IBM Watson NLP Emotion Detection API**. The application analyzes user input and returns the emotions present in the text along with the dominant emotion.

The project was developed as part of the **IBM AI Developer course final project**.

---

## Features

* Detects emotions from text
* Uses **IBM Watson NLP Emotion Detection**
* Returns five emotion scores:

  * Anger
  * Disgust
  * Fear
  * Joy
  * Sadness
* Identifies the **dominant emotion**
* Web interface using **Flask**
* Unit testing using **unittest**
* Static code analysis using **pylint**
* Error handling for invalid input

---

## Technologies Used

* Python
* Flask
* IBM Watson NLP API
* unittest
* pylint
* GitHub

---

## Project Structure

```
emotion-detector
│
├── EmotionDetection
│   ├── __init__.py
│   └── emotion_detection.py
│
├── test_emotion_detection.py
├── server.py
└── README.md
```

---

## How to Run the Application

### 1. Clone the repository

```
git clone https://github.com/yourusername/emotion-detector.git
```

### 2. Navigate to project folder

```
cd emotion-detector
```

### 3. Run the Flask server

```
python server.py
```

### 4. Open in browser

```
http://localhost:5000
```

---

## Example Output

Input:

```
I am very happy today
```

Output:

```
anger: 0.01
disgust: 0.01
fear: 0.02
joy: 0.93
sadness: 0.03
dominant_emotion: joy
```

---

## Author

Developed as part of the **Emotion Detector Final Project** for the IBM AI Developer course.
