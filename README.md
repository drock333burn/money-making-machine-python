# Money Making Machine

This is a simple **Streamlit** application that allows users to either generate virtual money or get motivational quotes. It features a sidebar for navigation between two sections:

1. **Money Generator** 💰: Randomly generates a virtual amount of money.
2. **Motivational Quotes** 🌟: Fetches an inspiring quote from an API.

## Features
- Generate random money amounts between $1 and $1000.
- Fetch motivational quotes from an API.
- User-friendly interface with a sidebar navigation menu.
- Animated spinners for better user experience.

## Installation
To run this project on your local machine, follow these steps:

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd money-making-machine
```

### 2️⃣ Install Dependencies
Ensure you have **Python 3.7+** installed, then run:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
streamlit run app.py
```

## Project Structure
```
📂 money-making-machine
│── app.py                # Main Streamlit application
│── requirements.txt      # List of dependencies
│── README.md             # Project documentation
```

## Dependencies
- `streamlit`
- `requests`

## API Used
This project fetches motivational quotes from **DummyJSON API**:
- Endpoint: [https://dummyjson.com/quotes](https://dummyjson.com/quotes)

## License
This project is open-source and available under the **MIT License**.
