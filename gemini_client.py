from google import genai
from dotenv import load_dotenv
from config import Config
from utils import log_info, log_error
from validator import validate_response
import os
import time
import json

# Load environment variables
load_dotenv()


class GeminiClient:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("API key missing. Please set GEMINI_API_KEY in .env file.")

        self.client = genai.Client(api_key=api_key)
        log_info("Gemini Client initialized.")

    
    # Generate Structured Career Response
    
    def generate_response(self, prompt, retries=2, delay=2):
        """
        Generates structured JSON response from Gemini.
        Includes retry logic and token tracking.
        """

        try:
            log_info("Sending request to Gemini API.")

            response = self.client.models.generate_content(
                model=Config.model_name,
                contents=prompt
            )

          
            # Token Usage Tracking
          
            input_tokens = 0
            output_tokens = 0

            if Config.track_tokens and hasattr(response, "usage_metadata"):
                usage = response.usage_metadata

                input_tokens = getattr(usage, "prompt_token_count", 0)
                output_tokens = getattr(usage, "candidates_token_count", 0)
                total = input_tokens + output_tokens

                # Streamlit sidebar 
                try:
                    import streamlit as st
                    if "token_usage" in st.session_state:
                        st.session_state.token_usage["input_tokens"] += input_tokens
                        st.session_state.token_usage["output_tokens"] += output_tokens
                        st.session_state.token_usage["total_tokens"] += total
                except Exception:
                    pass

                log_info(f"Tokens Used - Input: {input_tokens}, Output: {output_tokens}")

           
            # JSON Parsing (Robust)
            
            raw_text = response.text.strip()

            try:
                # Attempt strict JSON parsing
                parsed_json = json.loads(raw_text)

            except json.JSONDecodeError:
                # Try extracting JSON from mixed text
                try:
                    start = raw_text.index("{")
                    end = raw_text.rindex("}") + 1
                    parsed_json = json.loads(raw_text[start:end])
                except Exception:
                    log_error("JSON parsing failed.")
                    return "⚠️ Failed to generate structured JSON response."

           
            # Validation 
           
            if getattr(Config, "strict_validation", False):
                if not validate_response(parsed_json):
                    log_error("Response structure invalid.")
                    return "⚠️ Structured response could not be generated."

            log_info("Response generated successfully.")
            return parsed_json

        except Exception as e:
            log_error(f"Gemini API Error: {str(e)}")

            if retries > 0:
                log_info(f"Retrying API call... attempts left: {retries}")
                time.sleep(delay)
                return self.generate_response(prompt, retries=retries - 1, delay=delay)

            log_error("All retry attempts failed.")
            return "⚠️ System error occurred after multiple attempts."

    
    # AI-Based Guardrail
   
    def classify_career_query(self, user_input):
        """
        Uses Gemini to classify whether the input is career-related.
        Returns True if career-related, else False.
        """

        try:
            classification_prompt = f"""
            You are a strict intent classifier for a Career and Education AI Assistant.
            
            Your task is to determine whether the user query is related to:
            
            1. Career guidance
            2. Job search
            3. Professional development
            4. Skill development
            5. Certifications
            6. Resume building
            7. Interview preparation
            8. Career switching
            9. Promotions
            10. Salary negotiation
            11. Internships
            12. Freelancing
            13. Entrepreneurship / startup
            14. Higher education (BTech, MTech, MBA, PhD, etc.)
            15. Entrance exams (GRE, GMAT, CAT, GATE, IELTS, etc.)
            16. Scholarships
            17. Study abroad
            18. Academic planning
            19. Portfolio building
            20. LinkedIn / GitHub optimization
            21. Career gap management
            22. Layoffs and recovery
            23. Tech careers (AI, ML, Data Science, Cloud, DevOps, Cybersecurity, etc.)
            24. Non-tech careers (Finance, Marketing, HR, Civil Services, etc.)
            25. Government jobs
            26. Professional certifications (AWS, Azure, GCP, PMP, etc.)
            27. Learning roadmap
            28. Upskilling / reskilling
            29. Industry trends related to careers
            30. Career growth strategies
            
            If the query relates to ANY of the above topics, return ONLY:
            
            YES
            
            If the query is about unrelated topics such as:
            - Sports
            - Politics
            - Entertainment
            - General trivia
            - Jokes
            - Personal gossip
            - Random facts
            - Cooking
            - Travel
            - Weather
            
            Return ONLY:
            
            NO
            
            User Query:
            "{user_input}"
            
            Respond with ONLY one word: YES or NO.
            Do not explain your answer.
            """

            response = self.client.models.generate_content(
                model=Config.model_name,
                contents=classification_prompt
            )

            answer = response.text.strip().upper()
            log_info(f"Classification output: {answer}")

            # Flexible YES detection
            return "YES" in answer.upper()

        except Exception as e:
            log_error(f"Classification error: {str(e)}")
            return False