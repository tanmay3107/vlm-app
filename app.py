import streamlit as st
import base64
from openai import OpenAI

# 1. Connect to Local Brain
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# 2. Setup Web Page Configurations
st.set_page_config(page_title="Local Vision AI", page_icon="👁️", layout="centered")

st.title("👁️ Local Vision AI Engine")
st.write("Upload any image and ask your local Multimodal AI to analyze it. Everything runs 100% locally and privately.")

st.markdown("---")

# 3. Create a Drag-and-Drop Uploader
uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the image on the web page
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)    
    # 4. Text Input for the Prompt
    user_prompt = st.text_input("Ask a question about this image:", "Describe exactly what you see in this image.")
    
    # 5. The "Submit" Button
    if st.button("Analyze Image", type="primary"):
        with st.spinner("🧠 AI is analyzing the pixels..."):
            try:
                # Read the file directly from memory (no need to save to hard drive!)
                bytes_data = uploaded_file.getvalue()
                base64_image = base64.b64encode(bytes_data).decode('utf-8')
                
                # Determine correct MIME type
                file_extension = uploaded_file.name.split('.')[-1].lower()
                mime_type = "image/jpeg" if file_extension in ['jpg', 'jpeg'] else "image/png"
                
                # Ping the VLM
                response = client.chat.completions.create(
                    model="local-model",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": user_prompt},
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:{mime_type};base64,{base64_image}"
                                    }
                                }
                            ]
                        }
                    ],
                    temperature=0.3
                )
                
                # 6. Display the Output beautifully
                st.success("Analysis Complete!")
                st.markdown("### 🤖 AI's Report:")
                st.info(response.choices[0].message.content)
                
            except Exception as e:
                st.error(f"❌ Server Error. Is LM Studio running on port 1234? Details: {e}")