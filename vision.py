import base64
from openai import OpenAI
import os

print("👁️ Booting up Local Vision Model...")

# 1. Connect to Local Brain
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def encode_image(image_path):
    """Converts an image file into a Base64 text string."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Could not find {image_path}")
        
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# 2. Setup the image and prompt
image_filename = "test.jpg"  # Make sure this image is in your folder!
user_prompt = "Describe exactly what you see in this image."

try:
    print(f"🔄 Encoding {image_filename}...")
    base64_image = encode_image(image_filename)
    
    print("🧠 Analyzing image...")
    # 3. The Multimodal Payload
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
                            # We inject the base64 string directly into the URL field
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        temperature=0.3
    )
    
    print("\n================================================")
    print("✅ VISION REPORT:")
    print(response.choices[0].message.content)
    print("================================================")

except Exception as e:
    print(f"❌ Error: {e}")