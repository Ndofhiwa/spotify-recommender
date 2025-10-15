<<<<<<< HEAD
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

📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments

    Spotify for providing the comprehensive Web API

    Spotipy library developers for the excellent Python wrapper

    Machine learning community for open-source algorithms and tools

<div align="center">

Enjoy discovering new music! 🎧
</div> ```
=======
markdown
# AI-Powered Spotify Music Recommendation System

---

## Abstract

This project implements a comprehensive music recommendation system that integrates with Spotify's API to provide personalized song suggestions and automated playlist generation. The system employs content-based filtering using audio features and cosine similarity metrics to recommend musically similar tracks. Built with Python and Streamlit, the application demonstrates modern web development practices, API integration, and machine learning implementation for practical music discovery.

## 1. Introduction

### 1.1 Project Overview
The Spotify Music Recommender is a web application that helps users discover new music based on their existing preferences. By analyzing audio characteristics and musical patterns, the system suggests songs that share similar acoustic properties, enabling personalized music exploration beyond traditional genre-based recommendations.

### 1.2 Problem Statement
With over 100 million tracks available on streaming platforms, users face overwhelming choice when searching for new music. Existing recommendation algorithms often rely heavily on collaborative filtering, which struggles with new or niche content. This project addresses these limitations through content-based analysis of intrinsic musical features.

### 1.3 Objectives
- Develop a content-based music recommendation engine using Spotify's audio features
- Create an intuitive user interface for music discovery and playlist management
- Implement secure OAuth 2.0 authentication with Spotify API
- Provide analytical insights into musical preferences and library characteristics
- Demonstrate scalable software architecture with proper separation of concerns

## 2. System Architecture

### 2.1 High-Level Architecture
The application follows a modular three-tier architecture:



Presentation Layer (Streamlit UI)
↓
Business Logic Layer(Recommendation Engine + API Handlers)
↓
Data Layer(Spotify API + Local CSV Database)



### 2.2 Technology Stack
- **Frontend**: Streamlit web framework
- **Backend**: Python 3.11+
- **Authentication**: Spotify Web API OAuth 2.0
- **Data Storage**: Local CSV files with Spotify audio features
- **Machine Learning**: Scikit-learn for similarity calculations
- **Visualization**: Plotly, Matplotlib, Seaborn

### 2.3 Component Architecture

#### 2.3.1 Core Modules

**Authentication Module** (`auth.py`, `login.py`)
- Handles Spotify OAuth 2.0 authentication flow
- Manages user sessions and token refresh
- Provides secure credential management

**Data Management Module** (`data.py`)
python
def load_songs_from_csv(csv_path=None, sp=None):
    """
    Load and preprocess music dataset from CSV
    Handles data validation, cleaning, and feature extraction
    """


Recommendation Engine (recommend.py)

python
def recommend_from_song(song_name, df, n=10):
    """
    Content-based recommendation using cosine similarity
    on standardized audio features
    """


Playlist Management (playlist_utils.py)

· Creates and manages Spotify playlists via API
· Handles batch operations and error recovery
· Implements search-based track identification

User Interface Module (ui.py)

· Component-based UI architecture
· Responsive design with Spotify-themed styling
· State management and user interaction handling

Analytics Module (analytics.py)

· Data visualization and insight generation
· Clustering analysis and statistical summaries
· Recommendation performance tracking

3. Algorithm Design and Implementation

3.1 Recommendation Algorithm

3.1.1 Feature Selection

The system utilizes Spotify's comprehensive audio features:

· Danceability: Rhythmic suitability (0.0 to 1.0)
· Energy: Intensity and activity measure (0.0 to 1.0)
· Valence: Musical positiveness (0.0 to 1.0)
· Acousticness: Confidence of acoustic nature (0.0 to 1.0)
· Instrumentalness: Likelihood of no vocals (0.0 to 1.0)
· Tempo: Beats per minute (BPM)
· Loudness: Overall volume in decibels
· Speechiness: Presence of spoken words (0.0 to 1.0)

3.1.2 Similarity Calculation

python
def compute_similarity(target_features, all_features):
    # Standardize features
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(all_features)
    
    # Compute cosine similarity
    similarity_scores = cosine_similarity(
        target_features.reshape(1, -1), 
        features_scaled
    )
    return similarity_scores[0]


3.1.3 Algorithm Complexity

· Feature Scaling: O(n×d) where n is number of songs, d is features
· Similarity Computation: O(n×d) for cosine similarity
· Overall Complexity: O(n×d) suitable for datasets up to 10,000 songs

3.2 Data Structures Implementation

3.2.1 Efficient Data Handling

python
class MusicDataset:
    """Manages song data with efficient indexing"""
    def _init_(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.feature_matrix = self._extract_features()
        self.song_index = self._build_index()


3.2.2 Session State Management

python
# Track user interactions and recommendations
if 'recommendations_history' not in st.session_state:
    st.session_state.recommendations_history = []


4. User Interface Design

4.1 Interface Components

4.1.1 Sidebar Navigation

· User authentication status and profile
· Quick library statistics (total songs, artists)
· Navigation to analytics dashboard
· Logout functionality

4.1.2 Main Recommendation Interface

· Song selection dropdown with search functionality
· Real-time recommendation generation
· Interactive results display with similarity scores
· One-click playlist creation

4.1.3 Custom Playlist Creator

· Multi-song selection interface
· Playlist naming and description
· Batch addition to Spotify library

4.1.4 Analytics Dashboard

· Data distribution visualizations
· Feature correlation analysis
· Music clustering visualization
· Artist insights and trends

4.2 User Experience Features

· Responsive Design: Adapts to various screen sizes
· Loading States: Visual feedback during operations
· Error Handling: Graceful failure recovery
· Success Confirmation: Visual confirmation of actions

5. API Integration and Data Flow

5.1 Spotify Web API Integration

5.1.1 Authentication Flow


User Request → Spotify Authorization → Token Exchange → Session Establishment


5.1.2 API Endpoints Utilized

· Authorization: /authorize, /api/token
· User Data: /v1/me
· Playlist Management: /v1/users/{user_id}/playlists
· Search: /v1/search

5.2 Data Processing Pipeline

5.2.1 Recommendation Pipeline


Song Selection → Feature Extraction → Similarity Calculation → 
Result Filtering → Display Formatting → Playlist Creation


5.2.2 Data Validation

python
def validate_and_clean_csv(csv_path):
    """
    Ensures data quality through:
    - Missing value handling
    - Data type validation
    - Duplicate removal
    - Feature range verification
    """


6. Implementation Details

6.1 Core Functionality

6.1.1 Song Recommendation

python
def recommend_from_song(song_name, df, n=10):
    # Locate target song
    target_idx = df[df['song'] == song_name].index[0]
    
    # Extract and scale features
    features = extract_audio_features(df)
    scaled_features = scale_features(features)
    
    # Compute similarities and return top N
    similarities = cosine_similarity(
        scaled_features[target_idx:target_idx+1], 
        scaled_features
    )[0]
    
    return get_top_similar(similarities, df, n, exclude_idx=target_idx)


6.1.2 Playlist Creation

python
def create_playlist_from_recommendations(sp, user_id, base_song, recommendations):
    """
    Creates Spotify playlist from recommendations
    Handles track URI resolution and batch addition
    """


6.2 Error Handling and Edge Cases

6.2.1 Common Scenarios Handled

· Missing or corrupted audio features
· Spotify API rate limiting
· Network connectivity issues
· Invalid user credentials
· Empty recommendation results

7. Performance Analysis

7.1 Computational Efficiency

7.1.1 Time Complexity

· Data Loading: O(n) for n songs
· Recommendation Generation: O(n×d) for n songs, d features
· Playlist Creation: O(m) for m recommended songs

7.1.2 Memory Usage

· Dataset Storage: O(n×d) for song features
· Similarity Matrix: O(n) for storage
· Session Data: O(k) for k user interactions

7.2 Scalability Considerations

7.2.1 Current Limitations

· In-memory processing limits dataset size
· Linear similarity computation for large libraries
· Spotify API rate limits (≈ 1,000 requests/hour)

7.2.2 Optimization Strategies

· Feature dimensionality reduction
· Approximate nearest neighbors algorithms
· Caching frequently accessed data
· Batch processing for large operations

8. Results and Evaluation

8.1 Functional Requirements Met

8.1.1 Core Features

· ✅ Personalized song recommendations
· ✅ Spotify playlist automation
· ✅ User authentication and security
· ✅ Data visualization and analytics
· ✅ Responsive web interface

8.1.2 User Experience

· ✅ Intuitive song selection interface
· ✅ Fast recommendation generation (< 5 seconds)
· ✅ Seamless Spotify integration
· ✅ Comprehensive error handling

8.2 Technical Achievements

8.2.1 Code Quality

· Modular architecture with clear separation of concerns
· Comprehensive error handling and validation
· Type hints and documentation throughout
· Session state management for user experience

8.2.2 Algorithm Effectiveness

· Content-based filtering avoids cold start problem
· Cosine similarity provides musically meaningful results
· Feature standardization ensures fair comparisons

9. Conclusion and Future Work

9.1 Project Summary

The Spotify Music Recommender successfully demonstrates the implementation of a content-based recommendation system using modern web technologies. The application provides practical music discovery tools while maintaining clean, maintainable code architecture.

9.2 Key Achievements

· Successful integration with Spotify Web API
· Effective content-based recommendation algorithm
· Professional-grade user interface
· Comprehensive analytics and visualization
· Robust error handling and user feedback

9.3 Future Enhancements

9.3.1 Algorithm Improvements

· Hybrid recommendation combining content and collaborative filtering
· Deep learning models for feature representation
· Real-time learning from user feedback
· Context-aware recommendations (time, mood, activity)

9.3.2 Feature Additions

· Social features and sharing capabilities
· Advanced filtering and sorting options
· Mobile application development
· Offline recommendation capability
· Multi-platform playlist synchronization

9.3.3 Technical Enhancements

· Database integration for larger libraries
· Cloud deployment and scaling
· Advanced caching strategies
· A/B testing framework for algorithm evaluation

10. References

1. Spotify Web API Documentation (2023). Spotify for Developers
2. Pedregosa et al. (2011). Scikit-learn: Machine Learning in Python
3. Streamlit Documentation (2023). Streamlit Inc.
4. McKinney, W. (2010). Data Structures for Statistical Computing in Python

---

Appendix A: Installation and Setup
Appendix B: API Configuration Guide
Appendix C: User Manual

>>>>>>> 22938ebec1077f619d5576d761094ff2efb7663f
