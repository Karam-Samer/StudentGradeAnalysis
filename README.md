# Student Grade Analysis System

A comprehensive Python-based tool designed to analyze student exam results, visualize grade distributions, and utilize machine learning for grade prediction.

> [!IMPORTANT]
> **Data Privacy Disclaimer**: This project utilizes **100% FICTIONAL / MOCK DATA**.
> No real student information, names, seat numbers, or scores are included or processed in this repository. All datasets (labeled as `*_NotReal.xlsx`) were randomly generated for educational and portfolio demonstration purposes only. Any resemblance to actual persons is purely coincidental.

## 📖 Project Description

This application serves as a console-based utility for measuring and analyzing student performance metrics. It supports two distinct grading schemas ("Old System" and "New System") and provides educators with instant access to student records, statistical summaries, and visual insights. Furthermore, it demonstrates the application of **Machine Learning** in ed-tech by using Logistic Regression to analyze the relationship between percentages and grade outcomes.

## ✨ Key Features

- **Dual System Support**: Seamlessly processes data from both "Old" and "New" educational systems.
- **Privacy-First Design**: Built to operate entirely on anonymized/mock datasets.
- **Instant Search**: Look up student records by **Name** (Arabic text supported) or **Seat Number**.
- **Automated Grading**: Algorithms automatically calculate percentages and assign letter grades (A-F).
- **Visual Analytics**: Generates Pie Charts to visualize the overall distribution of grades across the cohort.
- **Predictive Modeling**: Implements a Logistic Regression model to predict grade categories based on performance scores.

## 🛠️ Technologies Used

- **Python**: Core logic and application flow.
- **Pandas**: Advanced data manipulation and Excel I/O.
- **NumPy**: Numerical operations and statistical calculations.
- **Matplotlib**: Data visualization and plotting.
- **Scikit-learn**: Machine learning model implementation (Logistic Regression).
- **Arabic-reshaper & Python-bidi**: Correct rendering of Arabic text in the terminal.

## 🚀 How the Program Works

1.  **Data Loading**: The script attempts to read from the mock data files:
    -   `OldSystem_NotReal.xlsx`
    -   `NewSystem_NotReal.xlsx`
2.  **System Selection**: The user creates a session by selecting the grading system to analyze.
3.  **Search Interface**: A loop prompt allows the user to query individual records:
    -   *Input*: Search by Name or Seat Number.
    -   *Output*: Displays Name, Seat No., Total Score, Percentage, and Grade.
4.  **Analytics Dashboard**: Upon exiting the search loop:
    -   A **Pie Chart** renders to show grade distribution.
    -   A **Logistic Regression** model trains on the dataset and outputs a prediction accuracy score.

## 💻 How to Run the Project

### Prerequisites
Make sure you have Python installed. Install the necessary dependencies:

```bash
pip install pandas numpy matplotlib scikit-learn arabic-reshaper python-bidi openpyxl
```

### Installation & Execution
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Karam-Samer/StudentGradeAnalysis.git
    cd student-grade-analysis
    ```
2.  **Verify Data Files**:
    Ensure the mock data files (`OldSystem_NotReal.xlsx` and `NewSystem_NotReal.xlsx`) are present in the directory.
3.  **Run the Script**:
    ```bash
    python graduate.py
    ```

## 🔮 Future Improvements

-   **Graphical User Interface (GUI)**: Implement a desktop UI using PyQt or Tkinter for easier navigation.
-   **PDF Reporting**: Add functionality to export individual student result cards as PDF files.
-   **Database Integration**: Migrate the backend from Excel files to a relational database (SQL) for scalability.
-   **Web App**: Convert the console script into a Flask or Django web application.
