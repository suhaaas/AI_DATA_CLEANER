# AI_DATA_CLEANER

🧹 AI-Powered Data Cleaning Application

An intelligent, end-to-end data cleaning platform built using FastAPI, Streamlit, and LLMs.
The app allows users to upload CSV/Excel files or connect to databases, and automatically performs data validation, cleaning, transformation, and structured output generation.

🚀 Project Overview

This project provides a unified interface for:

📤 File Uploads (CSV, Excel)

🗄️ Database Cleaning through SQL queries

🤖 AI-Driven Cleaning Logic using LangGraph + OpenAI

📊 Instant Data Preview before and after cleaning

🔗 API-First Architecture with a FastAPI backend and a Streamlit UI

The system intelligently handles missing values, duplicates, type mismatches, outliers, and more — returning structured, ready-to-use cleaned datasets.

🧠 Core Components
1. Streamlit Frontend

User-friendly UI

File upload + display

API calls to backend

Cleaned dataframe preview

2. FastAPI Backend

Receives input files or DB connections

Applies cleaning pipelines

Returns cleaned datasets in JSON

3. AI Cleaning Agent (LangGraph)

LLM-powered decisioning

Converts natural-language cleaning instructions into structured output

Ensures consistent and repeatable cleaning actions

🛠️ Tech Stack

Python, Pandas, NumPy

FastAPI

Streamlit

LangChain / LangGraph

OpenAI GPT Models

Requests

Pydantic
