import os
import sys
import time
from pathlib import Path

# Guard imports for optional third-party dependencies so missing packages
# produce an actionable runtime error (instead of editor-import warnings).
try:
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth, SpotifyOauthError
except Exception as e:  # pragma: no cover
    raise ImportError(
        "Missing required package 'spotipy'. Install with: pip install spotipy\n"
        "Also ensure 'python-dotenv' is installed: pip install python-dotenv\n"
        f"Original import error: {e}"
    )

try:
    from dotenv import load_dotenv
except Exception as e:  # pragma: no cover
    raise ImportError(
        "Missing required package 'python-dotenv'. Install with: pip install python-dotenv\n"
        f"Original import error: {e}"
    )


# === PROJECT CONFIG ===
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"
TOKEN_CACHE_DIR = BASE_DIR / ".cache"
TOKEN_CACHE_FILE = TOKEN_CACHE_DIR / "spotify_token_cache"

# === LOAD ENV ===
if not ENV_PATH.exists():
    raise FileNotFoundError(f"❌ Missing .env file at {ENV_PATH}")
print(f"🔍 Looking for .env at: {ENV_PATH}")

load_dotenv(dotenv_path=ENV_PATH)
print("Loaded ID:", os.getenv("SPOTIPY_CLIENT_ID"))
print("Environment variables loaded.")

# === VALIDATE REQUIRED VARIABLES ===
REQUIRED_ENV_VARS = ["SPOTIPY_CLIENT_ID", "SPOTIPY_CLIENT_SECRET", "SPOTIPY_REDIRECT_URI"]
missing = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]
if missing:
    raise EnvironmentError(f"❌ Missing required environment variables: {', '.join(missing)}")


def get_spotify_client(
    retries: int = 3,
    delay: int = 3
):
    """
    Authenticate and return a Spotify client using OAuth2.
    Handles caching, refresh, and retry logic.

    Returns:
        spotipy.Spotify: Authenticated Spotify client.
    """

    # === REQUESTED SCOPES (FULL ACCESS FOR PERSONALIZATION & PLAYLISTS) ===
    scope = (
        "user-library-read "
        "user-read-recently-played "
        "user-top-read "
        "playlist-read-private "
        "playlist-read-collaborative "
        "playlist-modify-private "
        "playlist-modify-public "
        "user-read-playback-state "
        "user-modify-playback-state "
        "user-read-currently-playing "
        "user-read-email "
        "user-read-private"
    )

    for attempt in range(1, retries + 1):
        try:
            # Ensure cache directory exists and use a file for cache (Spotipy expects a file path)
            try:
                TOKEN_CACHE_DIR.mkdir(parents=True, exist_ok=True)
            except Exception:
                pass

            redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
            print("\U0001f50d Using redirect URI:", redirect_uri)
            print("\U0001f4be Token cache file:", str(TOKEN_CACHE_FILE))

            auth_manager = SpotifyOAuth(
                client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
                redirect_uri=redirect_uri,
                scope=scope,
                cache_path=str(TOKEN_CACHE_FILE),
            )

            sp = spotipy.Spotify(auth_manager=auth_manager)

            # ✅ Sanity check: ensure valid token
            current_user = sp.current_user()
            print(f"✅ Spotify authentication successful. Logged in as: {current_user.get('display_name', 'Unknown User')}") # type: ignore

            # 🎯 Debug: Display the active scopes for verification
            print("🎯 Active Spotify scopes:", auth_manager.scope)

            return sp

        except SpotifyOauthError as e:
            print(f"⚠️ Spotify OAuth error on attempt {attempt}: {e}")
            if attempt < retries:
                print(f"🔁 Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("❌ Failed after multiple attempts. Please verify credentials and redirect URI.")
                sys.exit(1)

        except Exception as e:
            print(f"❌ Unexpected authentication error: {e}")
            sys.exit(1)


