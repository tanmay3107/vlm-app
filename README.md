# Local Vision AI Engine 👁️🖼️

A full-stack, drag-and-drop web application that allows users to upload images and analyze them using local Vision-Language Models (VLMs). 

This project demonstrates proficiency in multimodal AI integration, on-the-fly Base64 image encoding, and rapid frontend prototyping using Streamlit. The entire pipeline runs 100% locally, ensuring zero data leakage and total privacy.

## ✨ Key Features

* **Interactive Web GUI:** Built with Streamlit to provide a seamless, user-friendly interface replacing standard terminal output.
* **Multimodal Inference:** Utilizes models like LLaVA or Moondream2 to process complex image-text pairs simultaneously.
* **In-Memory Processing:** Captures uploaded files and dynamically encodes them into Base64 byte strings without requiring intermediary hard-drive storage.
* **Privacy First:** Bypasses cloud APIs entirely, routing all image data and prompts to a local ASGI server (LM Studio).

## 🛠️ Tech Stack

* **Frontend Framework:** Streamlit
* **Inference Engine:** LM Studio (Localhost API), OpenAI Python Client
* **Data Encoding:** Base64, UTF-8
* **Language:** Python 3.10+

## 🚀 Setup & Installation

**1. Install Dependencies**
Ensure you have Python installed, then set up the required web and routing libraries:

    pip install streamlit openai

**2. Start the Local Brain**
Open LM Studio, download and load a Vision-Language Model (e.g., `Moondream2` or `LLaVA`), and start the Local Inference Server on port 1234.

**3. Launch the Web App**
Navigate to the project directory and boot up the Streamlit server:

    streamlit run app.py

## 💻 Usage

1. Open your browser to the local URL provided by Streamlit (usually `http://localhost:8501`).
2. Drag and drop any `.jpg` or `.png` file into the upload zone.
3. Type a custom prompt or question regarding the image.
4. Click **Analyze Image** to view the VLM's generated report.