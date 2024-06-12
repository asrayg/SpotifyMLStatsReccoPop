# Spotify Stats, Recommendations, and Popularity Analysis

This project aims to create a comprehensive application where users can check their Spotify stats, receive personalized song recommendations, and explore popular tracks. The application leverages machine learning to analyze song features and recommend tracks, while also providing insightful statistics and visualizations based on Spotify's data.

## Table of Contents

- [Abstract](#abstract)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Future Directions](#future-directions)
- [Contributing](#contributing)
- [License](#license)

## Abstract

The Spotify Stats, Recommendations, and Popularity Analysis project combines multiple functionalities into a single application. Users can log in with their Spotify account to:
- View detailed statistics about their listening habits.
- Receive personalized song recommendations based on both lyrical and audio features.
- Explore popular tracks and artists over various time periods.

The backend is built using Flask, and the frontend (to be developed) will offer an intuitive and interactive user interface.

## Features

### Current Features
- **User Authentication**: OAuth authentication with Spotify.
- **Statistics Fetching**: Retrieve top tracks and artists over different time ranges.
- **Song Recommendations**: Use machine learning to recommend songs based on lyrical and audio features.
- **Popularity Analysis**: Analyze and model the popularity of Spotify tracks using audio features.

### Machine Learning Aspects
1. **Data Preprocessing**:
    - Cleaning and preprocessing lyrics.
    - Extracting audio features using the Spotify API.

2. **Feature Engineering**:
    - Combining text (GloVe embeddings) and audio features.

3. **Model Training**:
    - k-Nearest Neighbors (k-NN) for song recommendations.
    - Hyperparameter tuning with GridSearchCV.

4. **Recommendation System**:
    - Generating song recommendations and creating Spotify playlists.

## Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/SpotifyMLStatsReccoPop.git
    cd spotify-stats-recommender
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Spotify Developer Account**:
    - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
    - Create a new application to get your `Client ID` and `Client Secret`.

5. **Create a `.env` file** in the project root directory and add your Spotify credentials:
    ```dotenv
    SPOTIPY_CLIENT_ID=your_spotify_client_id
    SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
    SPOTIPY_REDIRECT_URI=http://localhost:5000/callback
    ```

6. **Run the Flask app**:
    ```bash
    python app.py
    ```

7. **Access the application** at `http://localhost:5000`.

## Usage

- Navigate to the base URL (`http://localhost:5000`) to log in with your Spotify account.
- After logging in, access various endpoints to view stats, get recommendations, and explore popular tracks.

### Example Commands
```bash
python recommender_system.py  # To run the song recommender system
jupyter notebook SpotifyPopularityModels.ipynb  # To explore popularity analysis
```

## Future Directions

### Frontend Development
- Develop an intuitive frontend to display user statistics, recommendations, and popular tracks interactively.

### Additional Features
- **Real-time Analysis**: Implement real-time tracking of listening habits.
- **Personalization**: Allow users to personalize analysis by selecting specific genres, artists, or time periods.
- **Interactive Visualizations**: Enhance visualizations to provide more detailed insights.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements, bug fixes, or other improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to contribute to the project or provide feedback!
```
