import numpy as np
import sys

def run_chatbot_interface():
    """Accepts user input and uses a simple, runnable logic to respond."""

    print("\n--- 🤖 Chatbot Interface Initialized ---")

    # --- 1. Get User Input ---
    user_input = input("Ask your question to Chatbot007: ").lower() # Convert to lowercase for easy searching

    # --- 2. Keyword Prediction Logic (New) ---

    # Check for specific keywords
    if "weather" in user_input:
        response = "The weather model predicts sun and a high of 75°F today. Always bring an umbrella just in case!"
        print(f"\n--- 2. Prediction Logic (Keyword) ---")
        print(f"Keyword 'weather' detected.")

    # --- 3. Default Length Prediction Logic (Existing) ---
    else:
        input_feature = len(user_input)

        # Simple Logic: If the input is long (more than 15 characters), categorize it as complex.
        if input_feature > 15:
            response = "That is an interesting and detailed question. Let me find that complex answer for you."
            prediction_value = 1
        else:
            response = "I see your short question. I can answer that quickly."
            prediction_value = 0

        print(f"\n--- 2. Prediction Logic (Length) ---")
        print(f"Input Length (Feature): {input_feature} characters")
        print(f"Prediction Result: {prediction_value}")

    # --- 4. Generate Response ---
    print(f"Chatbot007 Says: {response}")


if __name__ == "__main__":
    run_chatbot_interface()


