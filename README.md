# CNN-based Plant Fungal Infections Detection

This project, named **PlantGuard**, develops a system to detect fungal diseases in crops using **Computer Vision** (Convolutional Neural Networks) and predict disease outbreaks using **Time Series Forecasting** (LSTM). The goal is to enable early detection and forecasting to reduce pesticide use in agriculture. The frontend is built with Flask, HTML, Tailwind CSS (via CDN), AOS for animations, and Feather Icons, featuring a responsive interface for image uploads and prediction visualization.

GitHub Repository: [https://github.com/victordeman/CNN-based-plant-fungal-infections-detection.git](https://github.com/victordeman/CNN-based-plant-fungal-infections-detection.git)

## Project Structure

```
CNN-based-plant-fungal-infections-detection/
├── data/
│   ├── raw/                  # Raw datasets (e.g., PlantVillage images, weather data)
│   ├── processed/            # Processed data (e.g., augmented images, cleaned time series)
│   └── uploads/              # Uploaded images for predictions
├── models/                   # Trained models and checkpoints
├── src/
│   ├── computer_vision/      # CNN-related code for disease detection
│   ├── time_series/          # Time series forecasting code (LSTM)
│   └── utils/                # Utility functions (data preprocessing, visualization)
├── frontend/
│   ├── templates/            # HTML templates for Flask frontend (index.html)
│   └── static/
│       ├── css/              # CSS styles (placeholder for custom styles)
│       └── js/               # JavaScript for frontend interactivity
├── notebooks/                # Jupyter notebooks for experimentation
├── docs/                     # Documentation (e.g., project reports, abstracts)
├── tests/                    # Unit tests for code
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── app.py                    # Flask application entry point
├── train_cnn.py              # Script to train CNN model
├── train_lstm.py             # Script to train LSTM model
└── predict.py                # Script for inference (disease detection and forecasting)
```

## Prerequisites

- Python 3.8+
- Access to a GPU (recommended for training) or use Google Colab
- Datasets:
  - [PlantVillage Dataset](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset) for leaf images
  - Weather data (e.g., OpenWeatherMap API or NOAA datasets)
- Git (for cloning the repository)
- Web browser for Flask frontend

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/victordeman/CNN-based-plant-fungal-infections-detection.git
   cd CNN-based-plant-fungal-infections-detection
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   From the root directory, install all required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Datasets**:
   - Download the PlantVillage dataset and place it in `data/raw/`.
   - Obtain weather data (e.g., via OpenWeatherMap API) and save in `data/raw/`.

5. **Prepare Data**:
   - Run preprocessing scripts in `src/utils/` to process images and time series data:
     ```bash
     python src/utils/preprocess_images.py
     python src/utils/preprocess_timeseries.py
     ```

## Running the Project

1. **Train the CNN Model** (for disease detection):
   ```bash
   python train_cnn.py
   ```
   - Outputs trained model to `models/cnn_model.pth`.

2. **Train the LSTM Model** (for outbreak forecasting):
   ```bash
   python train_lstm.py
   ```
   - Outputs trained model to `models/lstm_model.pth`.

3. **Run Inference**:
   Use the prediction script to detect diseases and forecast outbreaks:
   ```bash
   python predict.py --image_path data/raw/sample_image.jpg --timeseries_path data/processed/weather_data.csv
   ```

4. **Launch the Flask Frontend**:
   ```bash
   python app.py
   ```
   - Access the web interface at `http://localhost:5000`.
   - Upload a leaf image in the "Disease Detection" section to get predictions.
   - View forecasting results in the "Disease Forecast" section (full implementation pending).

## Development Notes

- **Frontend**: The Flask frontend (`frontend/templates/index.html`) uses Tailwind CSS (via CDN), AOS for animations, and Feather Icons. The JavaScript in `frontend/static/js/main.js` handles image uploads and previews. Complete the backend routes in `app.py` to integrate with CNN and LSTM models for predictions.
- **Testing**: Run unit tests in the `tests/` directory using:
  ```bash
  python -m unittest discover tests
  ```
- **Documentation**: Refer to `docs/` for detailed reports or abstracts.

## Contributing

Contributions are welcome! Please fork the repository, create a branch, and submit a pull request.

## Contact

For questions, contact the project maintainer at [contact@plantguard.ai](mailto:contact@plantguard.ai).

---

*Generated by setup_project.sh on Tue Sep 16 06:31:06 AM CEST 2025*
