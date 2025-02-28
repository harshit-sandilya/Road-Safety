# Project Setup on Raspberry Pi 5

This guide provides steps to set up and run the project on a Raspberry Pi 5.

## Prerequisites

- Raspberry Pi 5
- Python 3 installed
- `pip` installed

## Setup Instructions

1. **Create a virtual environment**  
   Run the following command to create a virtual environment using Python's built-in `venv` module:
   ```sh
   python3 -m venv venv
   ```

2. **Activate the virtual environment**  
   ```sh
   source venv/bin/activate
   ```

3. **Install dependencies**  
   Install required packages from `requirements.txt`:
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the project**  
   Execute the main script:
   ```sh
   python main.py
   ```

## Deactivating the Virtual Environment

To exit the virtual environment, run:
```sh
deactivate
```

