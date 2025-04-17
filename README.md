# AI Sales Analyst: Intelligent Insights for Business Growth 📈

Unlock the power of data with the AI Sales Analyst, a comprehensive tool designed to provide advanced analytics, insightful customer review processing, and intelligent answers to your sales-related queries. Leverage the power of artificial intelligence to gain a deeper understanding of your sales performance and customer feedback.

## ✨ Key Features

* **Interactive Sales Metrics Dashboard:** Visualize crucial sales indicators at a glance. Track total revenue and identify key sales trends over different timeframes. Gain actionable insights from clear and concise visual representations.
* **Intelligent Deep Learning Chatbot:** Engage in natural language conversations with our PyTorch-powered chatbot. Ask specific questions about your sales data and receive intelligent, context-aware responses. Get quick answers and explore your data through an intuitive conversational interface.
* **Robust Exploratory Data Analysis (EDA):** Dive deep into your sales data using the power of pandas. Clean, transform, and analyze your datasets to uncover hidden patterns, correlations, and trends that might not be immediately obvious. Gain a thorough understanding of your data's characteristics.
* **Dynamic Data Visualization:** Transform raw sales data into compelling and easy-to-understand visualizations. Create interactive charts and graphs to identify opportunities, understand customer behavior, and communicate key findings effectively.

## 🛠️ Technologies Used

* **Backend Framework:** [Flask](https://flask.palletsprojects.com/en/2.3.x/) (A lightweight and flexible Python web framework for building the API.)
* **Deep Learning Engine:** [PyTorch](https://pytorch.org/) (A powerful open-source machine learning framework used to power the intelligent chatbot.)
* **Data Analysis & Manipulation:** [pandas](https://pandas.pydata.org/) (A versatile Python library providing data structures and tools for data analysis.)
* **Frontend Development:** HTML, CSS, Streamlit (Standard web technologies for building the user interface.)

## 🖼️ Screenshots

**Enhance your understanding with visual examples:**

* **HOME PAGE: A snapshot of the main dashboard showcasing key sales metrics and visualizations.**
    
    ![Screenshot 2025-04-17 at 5 15 41 PM](https://github.com/user-attachments/assets/cf57bd68-87bf-412e-93fa-a3eab63a4554)

    
* **OTHER ANALYSIS PAGES: Snapshots of advanced analysis and some charts.**
    
    ![Screenshot 2025-04-17 at 5 15 53 PM](https://github.com/user-attachments/assets/3b0c36a9-de98-4b6e-a8c3-e81d83a7e5a0)
    ![Screenshot 2025-04-17 at 5 15 53 PM](https://github.com/user-attachments/assets/bfe15372-3bc6-420b-b9aa-9cd6343ea23f)
    ![Screenshot 2025-04-17 at 5 07 53 PM](https://github.com/user-attachments/assets/5fc312b4-1fde-4ee0-a555-a39cc9eea41f)
    ![Screenshot 2025-04-17 at 5 08 27 PM](https://github.com/user-attachments/assets/e41732bb-96c0-4888-8f7e-dc61f8e7bb42)
    ![Screenshot 2025-04-17 at 5 08 47 PM](https://github.com/user-attachments/assets/b1c6d105-8ea4-4149-a111-22169f6f43b5)

* **CHATBOT INTERACTION: Examples of how to interact with the AI-powered chatbot to ask questions and receive insightful answers.**
    ![Screenshot 2025-04-17 at 5 17 36 PM](https://github.com/user-attachments/assets/a0fbcbd7-839f-4733-9629-d1bd02dbcb72)
    ![Screenshot 2025-04-17 at 5 18 44 PM](https://github.com/user-attachments/assets/e2f7f561-04d3-4a01-91a2-28565973b1b9)
    ![Screenshot 2025-04-17 at 5 19 43 PM](https://github.com/user-attachments/assets/73277e4b-3be9-4761-a36c-38c4a68b76e2)

## ⚙️ Installation Guide

Follow these steps to get the AI Sales Analyst up and running on your local machine:

1.  **Clone the Repository:** Obtain the project source code from GitHub.
    ```bash
    git clone [https://github.com/jainil5/ai-sales-analyst.git](https://github.com/jainil5/ai-sales-analyst.git)
    ```

2.  **Navigate to the Backend Directory:** Change your current directory to the backend folder.
    ```bash
    cd backend
    ```

3.  **Install Backend Dependencies:** It's recommended to create a virtual environment to manage project dependencies.
    ```bash
    # Create a virtual environment (optional but recommended)
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # venv\Scripts\activate  # On Windows

    # Install the required Python packages from the requirements file
    pip install -r requirements.txt
    ```
    *(Note: Make sure you have a `requirements.txt` file in your `backend` directory listing dependencies like Flask, PyTorch, pandas, etc.)*

4.  **Run the Backend Server:** Start the Flask development server.
    ```bash
    python flask_app.py
    ```
    *(Ensure your `flask_app.py` file contains the necessary Flask application setup.)*

5.  **Open the Frontend:** Navigate to the `frontend` directory in your project. Locate the main HTML file (e.g., `index.html`) and open it in your web browser.

    ```bash
    cd ../frontend
    # Now open the relevant HTML file (e.g., index.html) in your browser.
    # You can usually do this by simply double-clicking the file.
    ```

**Important Considerations:**

* **API Endpoints:** The frontend likely interacts with the backend API endpoints (e.g., `/api/sales-data`, `/api/chatbot`). Ensure that the backend server is running correctly on the specified host and port (typically `http://127.0.0.1:5000` by default for Flask development).
* **Data Source:** The backend application must be configured to access your sales data. Review the backend code (`flask_app.py` or related files) to understand how it fetches and processes the data.
* **Chatbot Model:** The PyTorch-powered chatbot requires a trained model. Ensure that the necessary model files and loading mechanisms are correctly implemented in the backend.

## 🚀 Getting Started

Once you have the application running, you can:

* **Explore the Dashboard:** Navigate through the different sections of the sales metrics dashboard to visualize your key performance indicators.
* **Interact with the Chatbot:** Type your sales-related questions into the chatbot interface and see the intelligent responses.
* **(Optional) Dive into the Code:** If you are a developer, explore the backend and frontend code to understand the architecture and potentially contribute to the project.

## 🤝 Contributing

Contributions to the AI Sales Analyst project are welcome! If you have ideas for new features, bug fixes, or improvements, please feel free to:

1.  Fork the repository.
2.  Create a new branch for your feature or fix.
3.  Commit your changes.
4.  Push to the branch.
5.  Submit a pull request.

