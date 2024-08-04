# Setup Instructions

## Prerequisites

- Python 3.x
- Git

## Steps

1. Clone the repository:
   
   ```sh
   git clone https://github.com/AllyElvis/aenzbi-odoo.git
   cd aenzbi-odoo
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Run the application:

   ```sh
   python app.py
   ```

## Running Tests

To run the tests, use the following commands:

```sh
python -m unittest discover -s tests/unit
python -m unittest discover -s tests/integration
python -m unittest discover -s tests/uat
```
