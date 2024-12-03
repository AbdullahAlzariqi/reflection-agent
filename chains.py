from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

reflection_prompt = ChatPromptTemplate.from_messages(

    [
        ("system",
         "You are a viral twitter influencer grading a tweet. Gnerate critique and reccomendations for the user. Always provide detailed recommendations, including requests forlength, virality, style ,etc"
         ),
         MessagesPlaceholder(variable_name="messages")

    ] 
)


generation_prompt= ChatPromptTemplate.from_messages(
    [
        ("system",
         " You are a twitter techie influencer assistant tasked with writing excellent twitter posts. Generate the best twitter post possible for the user's request. If the user provides critique, respond with a revised version of the previous attempts"
         ),
         MessagesPlaceholder(variable_name="messages")

    ]
)

llm = ChatGoogleGenerativeAI(    model="gemini-1.5-flash", api_key=os.getenv("GEMINI_API_KEY"))
generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm