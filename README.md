# CenLog
A program written in python to collect data of students in Computer Engineering in a mongodb database and perform CRUD operations of them

# Running Python Code in a Virtual Environment

This README provides a quick guide on how to set up and run Python code in a virtual environment.

## Prerequisites

- Python installed on your system.

## Setting Up a Virtual Environment

1. Open your terminal.

2. Navigate to the project directory where your Python code is located.

3. Create a virtual environment (replace "myenv" with your preferred environment name):

   ```bash
   python -m venv myenv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     myenv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source myenv/bin/activate
     ```

## Installing Dependencies

1. Make sure your virtual environment is active.

2. Install required dependencies using `pip`:

   ```bash
   pip install pymongo
   ```

## Running the Python Code

1. With the virtual environment active, run your Python script:

   ```bash
   python CenLog.py
   ```

## Deactivating the Virtual Environment

When you're done, deactivate the virtual environment:

```bash
deactivate
```

Your system will return to the global Python environment.

---

Feel free to adapt the names and paths to match your specific project. This README provides a simple step-by-step guide for running Python code in a virtual environment.
