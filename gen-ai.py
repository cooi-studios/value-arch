import streamlit as st
import openai
import os

openai.api_key = "sk-proj-RDiG6543tSs4INeTNcYST3BlbkFJnRZTbTE3JYmsa2KVeRwk"

# col1, col2 = st.columns([1, 4])
# with col1:
#     st.image("mfest.jpeg", width=300) 
# with col2:
#     st.markdown("<h1 style='color: #004A8F; text-align: center;'>AI-Insight</h1>", unsafe_allow_html=True)

# Check if the background image file exists in the current directory
background_image = "image.png"

if os.path.exists(background_image):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{st.image(background_image, use_column_width=True)}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.error("Background image not found! Please ensure 'background.png' is in the app directory.")

def generate_insights(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": "You are an assistant that helps generate market research insights."},
                {"role": "user", "content": prompt} 
            ]
        )
       
        if response.choices:
            return response.choices[0].message['content'].strip()
        else:
            return "No insights generated."
    except Exception as e:
        return f"Error generating insights: {str(e)}"

# Main content section
def main():
    st.markdown("<div class='content-section'>", unsafe_allow_html=True)
    st.header("Market Research Insights")

    sector = st.text_input("Sector", placeholder="e.g., Automotive")
    region = st.text_input("Region", placeholder="e.g., Southern Africa")
    company = st.text_input("Company", placeholder="e.g., FastCar Inc.")
    customer_persona = st.text_input("Customer Persona", placeholder="e.g., Small Business Owners")

    prompt = ""

    if st.button("Generate Insights"):
      
        prompt = f"Generate market research insights for the following details:\n\n"
        prompt += f"Sector: {sector}\n"
        prompt += f"Region: {region}\n"
        prompt += f"Company: {company}\n"
        prompt += f"Customer Persona: {customer_persona}\n"

        insights = generate_insights(prompt)
        st.subheader("Generated Market Research Insights")
        st.write(insights)

      
        if insights and isinstance(insights, str):
            st.download_button("Download Insights", data=insights, file_name="generated_insights.txt")
        else:
            st.error("Unable to generate valid insights. Please check the input details.")

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
