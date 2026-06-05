# ✍️ Handwritten Digit Recognition

## 📌 Overview

This project is a **Handwritten Digit Recognition Web Application** built using **Python**, **Scikit-learn**, and **Streamlit**. The application automatically trains a Neural Network model on the Scikit-learn Digits dataset and allows users to upload images of handwritten digits for real-time prediction.

The model recognizes digits from **0 to 9** and displays both the predicted digit and the confidence score.

---

## 🚀 Features

* Automatic model training on startup
* Handwritten digit prediction (0–9)
* Real-time image upload and processing
* Confidence score display
* Class probability distribution for all digits
* Interactive web interface using Streamlit
* No external dataset download required

---

## 🛠️ Technologies Used

* Python 3.13
* Streamlit
* NumPy
* Pillow (PIL)
* Scikit-learn

---

## 📂 Project Structure

```text
Handwritten_Digit_Recognition/
│
├── app.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/CodeAlpha_Handwritten_Digit_Recognition.git
cd CodeAlpha_Handwritten_Digit_Recognition
```

### 2. Install Required Libraries

```bash
pip install streamlit numpy pillow scikit-learn
```

---

## ▶️ Running the Application

Execute the following command in the terminal:

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

## 📊 Model Information

The application uses:

* Dataset: Scikit-learn Digits Dataset
* Algorithm: Multi-Layer Perceptron (MLPClassifier)
* Hidden Layers: (128, 64)
* Maximum Iterations: 500

The model is trained automatically when the application starts.

---

## 🖼️ How to Use

1. Launch the Streamlit application.
2. Upload an image containing a handwritten digit.
3. The image is converted to grayscale.
4. The image is resized to 8×8 pixels.
5. The trained model predicts the digit.
6. View:

   * Predicted Digit
   * Confidence Score
   * Probability for each digit class

---

## 📈 Output Example

```text
Prediction: 7
Confidence: 98.45%
```

---

## 🎯 Future Improvements

* Support for handwritten alphabets (A–Z)
* Custom dataset training
* Drawing canvas for direct digit input
* CNN-based deep learning model
* Enhanced image preprocessing

---

## 👩‍💻 Author

**Chandana**

CodeAlpha Internship Project

---

## 📜 License

This project is developed for educational and learning purposes under the CodeAlpha Internship Program.
