
# CNIX v2.0 - Moroccan Card ID Software Reader/Scanner

Welcome to CNIX v2.0, a comprehensive solution for reading and processing Moroccan ID cards. This software utilizes advanced image processing and optical character recognition (OCR) techniques to extract, validate, and manage data from ID cards and images containing numerical information.

## Features

### ID Card Scanning
- **Front/Back Detection**: Automatically determine if the scanned image is of the front or back of the ID card using face detection with OpenCV.
- **Data Extraction**: Extract and filter essential data from the ID card, such as name, CIN, date of birth, etc.

### Snipping Tool
- **Image Snipping**: Capture portions of the screen where the desired number is displayed.
- **OCR Processing**: Use OCR to extract numbers from the snipped image.
- **Length Validation**: Validate the extracted number based on the specified length.

### Data Management
- **Save/Load Data**: Save extracted data to a JSON file or load data from a JSON file.
- **SQLite Database Integration**: Save data to an SQLite database for persistent storage.
- **Search and Autocomplete**: Search for records using a search bar with autocomplete functionality based on the database (CIN).
- **Autofill**: Autofill forms using data retrieved from the database.

## Used Libraries

- **OpenCV**: For image processing and face detection.
- **pytesseract**: For optical character recognition (OCR).

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/cnix-v2.0.git
    cd cnix-v2.0
    ```

2. Install required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the application:
    ```sh
    python main.py
    ```

## Usage

1. **ID Card Scanning**:
    - Launch the application and select the option to scan an ID card.
    - Upload an image of the ID card.
    - The software will determine if the image is the front or back of the card, extract the relevant data, and display it.

2. **Snipping Tool**:
    - Select the snipping tool option.
    - A new window will open, allowing you to drag a rectangle over the area containing the number.
    - The software will use OCR to extract the number and validate it based on the length provided.

3. **Data Management**:
    - Save extracted data to a JSON file for later use.
    - Load data from a JSON file to resume your work.
    - Save data to the SQLite database for persistent storage.
    - Use the search bar to find records quickly, with autocomplete suggestions based on existing database entries.
    - Autofill forms using data retrieved from the database.

## Contributing

We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to get involved.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

We would like to thank all the contributors and the open-source community for their valuable work and resources.

---

For more details and updates, visit our [GitHub repository](https://github.com/yourusername/cnix-v2.0).
