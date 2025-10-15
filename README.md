# Spotify Music Recommender System 🎵

A machine learning-powered music recommendation system that suggests songs based on audio features and user preferences using Spotify's Web API.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange)
![Spotify API](https://img.shields.io/badge/Spotify-API-brightgreen)

## ✨ Features

- **Smart Recommendations**: Content-based filtering using audio features
- **Spotify Integration**: Direct connection to Spotify's extensive music database
- **Audio Analysis**: Utilizes tempo, danceability, energy, and other musical attributes
- **User-Friendly Interface**: Easy-to-use application
- **Personalized Suggestions**: Recommendations tailored to individual music tastes

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Spotify Developer Account
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Ndofhiwa/spotify-recommender.git
cd spotify-recommender

2. Create and activate virtual environment

python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Set up Spotify API credentials

    Go to Spotify Developer Dashboard

    Create a new app and get your Client ID and Client Secret

    Add redirect URI: http://localhost:8888/callback or http://127.0.0.1:8501/callback

    Create a .env file in the project root:

SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_CLIENT_SECRET=your_client_secret_here
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback

Usage

Run the application:

streamlit run main.py


📁 Project Structure

spotify-recommender/
├── main.py                 # Main application file
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignore rules
├── Recommender/           # Main package
│   ├── __init__.py
│   ├── analytics.py       # Data analysis and recommendations
│   └── spotify_api.py     # Spotify API interactions
├── data/                  # Data storage
│   ├── raw/              # Raw data files
│   └── processed/        # Processed data
└── assets/               # Images and documentation assets


🔧 Configuration
Spotify API Setup

    Visit Spotify Developer Dashboard

    Click "Create App"

    Fill in app name and description

    Add redirect URIs:

        http://localhost:8888/callback

        http://127.0.0.1:8501/callback

    Copy Client ID and Client Secret to your .env file

Environment Variables

Create a .env file with:

SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback


🎯 How It Works

    Data Collection: Fetches track data and audio features from Spotify API

    Feature Engineering: Processes audio characteristics (tempo, energy, danceability, etc.)

    Similarity Calculation: Uses machine learning algorithms to find similar tracks

    Recommendation Generation: Suggests songs based on feature similarity

📊 Audio Features Used

    Acousticness: Confidence measure of whether track is acoustic

    Danceability: How suitable a track is for dancing

    Energy: Perceived intensity and activity

    Instrumentalness: Predicts whether track contains no vocals

    Liveness: Detects presence of audience in recording

    Loudness: Overall loudness in decibels

    Speechiness: Detects presence of spoken words

    Tempo: Overall estimated tempo in BPM

    Valence: Musical positiveness conveyed by track

🛠️ Technologies Used

    Python 3.8+ - Core programming language

    Spotipy - Spotify Web API wrapper

    Pandas - Data manipulation and analysis

    Scikit-learn - Machine learning algorithms

    Plotly - Interactive data visualization

    NumPy - Numerical computing

🤝 Contributing

We welcome contributions! Please feel free to submit pull requests or open issues for bugs and feature requests.
Contribution Guidelines

    Fork the repository

    Create a feature branch (git checkout -b feature/AmazingFeature)

    Commit your changes (git commit -m 'Add some AmazingFeature')

    Push to the branch (git push origin feature/AmazingFeature)

    Open a Pull Request


🙏 Acknowledgments

    Spotify for providing the comprehensive Web API

    Spotipy library developers for the excellent Python wrapper

    Machine learning community for open-source algorithms and tools



Enjoy discovering new music! 🎧

