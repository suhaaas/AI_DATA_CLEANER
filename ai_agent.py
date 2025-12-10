import openai
import pandas as pd
from dotenv import load_dotenv
import os
from langchain_openai import OpenAI
from langgraph.graph import StateGraph, END
from pydantic import BaseModel

#Load API key from environment
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")


#   Define the AI Agent class

llm = OpenAI(openai_api_key=openai_api_key, temperature=0)  

class CleaningState(BaseModel):
    """State schema defining input and output for the Langraph agent"""
    input_text: str
    structured_response: str = ""

class AIAgent:
    def __init__(self):
        self.graph = self.create_graph()

    def create_graph(self):
        """Create the Langraph state graph for the AI agent."""
        graph = StateGraph(CleaningState)


        # Ensure agent outputs structured response
        def agent_logic(state: CleaningState) -> CleaningState:
            response = llm.invoke(state.input_text)
            return CleaningState(
                input_text=state.input_text,
                structured_response=response)

        graph.add_node("cleaning_agent", agent_logic)
        graph.add_edge("cleaning_agent", END)
        graph.set_entry_point("cleaning_agent")
        return graph.compile()

    def process_data(self,df,batch_size=20):
        """Process data in batches to avoid OpenAIs token limits."""
        cleaned_responses = []


        for i in range(0,len(df),batch_size):
            df_batch = df.iloc[i:i + batch_size]

            prompt = f"""
            You are a data cleaning assistant. Given the following data rows, identify and correct any inconsistencies, missing values, or errors. Provide the cleaned data in a structured format.

            
            {df_batch.to_string()}

            Identify missing values,choose the best imputation strategy(mean,mode,median),
            reomve duplicates, and fix data types as necessary.

            Return the cleaned data in a tabular format.
            """

            state = CleaningState(input_text=prompt, structured_response="")
            response = self.graph.invoke(state)
            
            if isinstance(response,dict):
                response = CleaningState(**response)


            cleaned_responses.append(response.structured_response)

        return "\n".join(cleaned_responses)

        

