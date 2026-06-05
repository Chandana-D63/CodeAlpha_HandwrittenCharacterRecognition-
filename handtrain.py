import streamlit as st
import numpy as np
from PIL import Image, ImageOps
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="Handwritten Digit Recognition")

# -------------------------
# Train model automatically
# -------------------------
@st.cache_resource
def train_model():
    digits = load_digits()

    X = digits.data
    y = digits.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42
    )

    model = MLPClassifier(
        hidden_layer_sizes=(128, 64),
        max_iter=500,
        random_state=42
    )

    model.fit(X_train, y_train)

    acc = accuracy_score(y_test, model.predict(X_test))

    return model, acc

model, accuracy = train_model()

# -------------------------
# UI
# -------------------------
st.title("✍️ Handwritten Digit Recognition")
st.write("Upload an image containing a handwritten digit (0-9).")

st.success(f"Model Accuracy: {accuracy*100:.2f}%")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("L")

    st.image(image, caption="Uploaded Image", width=250)

    # Convert to grayscale and invert
    image = ImageOps.invert(image)

    # Resize to 8x8 (same as sklearn digits dataset)
    image = image.resize((8, 8))

    img_array = np.array(image)

    # Normalize to dataset scale (0-16)
    img_array = (img_array / 255.0) * 16

    img_array = img_array.reshape(1, -1)

    prediction = model.predict(img_array)[0]

    probabilities = model.predict_proba(img_array)[0]

    confidence = np.max(probabilities) * 100

    st.subheader("Prediction")

    st.success(f"Digit: {prediction}")

    st.info(f"Confidence: {confidence:.2f}%")

    st.subheader("Class Probabilities")

    for digit, prob in enumerate(probabilities):
        st.write(f"{digit}: {prob*100:.2f}%")