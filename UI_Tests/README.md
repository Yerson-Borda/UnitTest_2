<div align="center">
  <h1>Largest Rectangle in Histogram with e2e/UI tests</h1>
</div>

This project implements a web-based calculator using Flask for calculating the largest rectangle area in a histogram, and it includes Selenium-based end-to-end tests to validate the web interface.

## Solution Requeriments

- `Flask`
- `Selenium`
- `Chrome WebDriver (for Selenium)`

## Project Structure

- `app.py: Flask application that implements the web interface.`
- `solution.py: Contains the algorithm for calculating the largest rectangle area.`
- `templates/index.html: HTML template for the web interface.`
- `test_e2e.py: Selenium-based end-to-end tests to verify the web application.`

### Tests
- `test_e2e.py: Contains two main test cases:`
    - `test_largest_rectangle_area: Validates the calculation of largest rectangle area.`
    - `test_invalid_input: Checks error handling for invalid input.`

## Usage
1) Run the Flask Application: ```python app.py```bash
2) Access the Application: Open your web browser and go to ```http://127.0.0.1:5000/``` to use the application.
3) Run Selenium Tests:Ensure the Flask application (app.py) is running, then run the Selenium end-to-end tests ```python test_e2e.py```