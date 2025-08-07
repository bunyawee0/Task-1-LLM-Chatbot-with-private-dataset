# Task-1-LLM-Chatbot-with-Private-Dataset

A chatbot application that uses LLM (Large Language Model) to answer questions based on your private dataset scraped from websites.

## Features

- Web scraping functionality to collect data from specified websites
- Integration with Ollama for local LLM inference
- Streamlit-based user interface for easy interaction
- Support for private dataset integration with RAG (Retrieval-Augmented Generation)

## Installation

### 1. Install Ollama

Download and install Ollama from [https://ollama.com/download](https://ollama.com/download)

After installation, open Command Prompt (cmd) and pull the Mistral model:
```bash
ollama pull mistral
```

### 2. Clone the Repository

```bash
git clone https://github.com/bunyawee0/Task-1-LLM-Chatbot-with-private-dataset.git
cd Task-1-LLM-Chatbot-with-private-dataset
code . # open vscode
```

### 3. Set Up Python Environment

Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root directory with the following configuration:

```env
URL = "https://www.agnoshealth.com/forums"
RAW_DATA_FILE = "data.csv"
```

### Configuration Options:
- `URL`: The website URL to scrape data from
- `RAW_DATA_FILE`: Name of the CSV file to store scraped data

## Usage

### 1. Scrape Data

Run the data scraping script to collect data from your specified website:
```bash
python data_scrape.py
```

This will create a CSV file containing the scraped data based on your configuration.

### 2. Start the Chatbot

Launch the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default web browser, typically at `http://localhost:8501`

## Project Structure

```
Task-1-LLM-Chatbot-with-private-dataset/
├── app.py              # Main Streamlit application
├── data_scrape.py      # Web scraping script
├── requirements.txt    # Python dependencies
├── .env               # Environment configuration
├── README.md          # This file
└── data.csv
```
