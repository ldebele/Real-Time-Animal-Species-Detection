# Animal-Species-Detection

## Table of Contents
- [Datasets](#datasets)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Web App](#web-app)
- [Contirbuting](#contributing)

## Datasets
The dataset used in this project consists of labeled images of 10 different animal classes: Buffalo, Cheetahs, Deer, Elephant, Fox, Jaguars, Lion, Panda, Rabbit, Raccon, Rhino, Squirrel, Tiger, Zebra. You can find the datasets: 
- [Dataset 1](https://www.kaggle.com/datasets/biancaferreira/african-wildlife)
- [Dataset 2](https://www.kaggle.com/datasets/brsdincer/danger-of-extinction-animal-image-set)
- [Dataset 3](https://www.kaggle.com/datasets/antoreepjana/animals-detection-images-dataset )

## Project Structure
    ├── config
    │   └── custom.yaml    
    ├── data
    │   ├── images         
    │   └── labels         
    ├── logs
    │   └── log.log      
    ├── notebooks
    │   └── yolov8.ipynb
    ├── runs
    │   └── detect
    │       ├── train
    │       └── val
    ├── scripts
    │   ├── app.py
    │   ├── convert_format.py
    │   └── train_test_split.py
    ├── README.md
    └── requirements.txt

## Getting Started
Follow theses steps to set up the environment and run the application.
1. Fork the repository [here](https://github.com/ldebele/animal-Species-Detection).
2. Clone the forked repository.
    ```bash
    git clone https://github.com/<YOUR-USERNAME>/Animal-Species-Detection
    cd Animal-Species-Detection
    ```

3. Create a python virtual environment.
    ``` bash
    python3 -m venv venv
    ```

4. Activate the virtual environment.

    - On Linux and macOS
    ``` bash
    source venv/bin/activate
    ```
    - On Windows
    ``` bash
    venv\Scripts\activate
    ```

5. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```
6. Run the application.
    ```python
    streamlit run './scripts/app.py'
    ```

## Web App
The trained model has been deployed on Hugging Face for practical use.
- you can access the deployed [web app](https://huggingface.co/spaces/ldebele/animal_detection_app)

## Contributing
Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or a pull request.