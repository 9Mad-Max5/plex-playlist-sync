import os
import toml

from pps.config.helpers import UserInputs


def is_running_in_docker():
    if os.path.exists("/proc/1/cgroup"):
        with open('/proc/1/cgroup', 'r') as f:
            for line in f:
                if 'docker' in line:
                    return True
    return False

def get_environment_variables():
    if is_running_in_docker():
        PLEX_URL = os.getenv("PLEX_URL")
        PLEX_TOKEN = os.getenv("PLEX_TOKEN")
        PLEX_USERNAME = os.getenv("PLEX_USERNAME")
        PLEX_PASSWORD = os.getenv("PLEX_PASSWORD")
        SERVER_NAME = os.getenv("PLEX_SERVER_NAME")
        WRITE_MISSING_AS_CSV = os.getenv("WRITE_MISSING_AS_CSV", "0") == "1"
        APPEND_SERVICE_SUFFIX = os.getenv("APPEND_SERVICE_SUFFIX", "1") == "1"
        ADD_PLAYLIST_POSTER = os.getenv("ADD_PLAYLIST_POSTER", "1") == "1"
        ADD_PLAYLIST_DESCRIPTION = os.getenv("ADD_PLAYLIST_DESCRIPTION", "1") == "1"
        APPEND_INSTEAD_OF_SYNC = os.getenv("APPEND_INSTEAD_OF_SYNC", False) == "1"
        WAIT_SECONDS = int(os.getenv("SECONDS_TO_WAIT", 43200))
        SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
        SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
        SPOTIFY_USER_ID = os.getenv("SPOTIFY_USER_ID")
        SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
        SPOTIFY_DAILY_MIXES = os.getenv("SPOTIFY_DAILY_MIXES").split(",")
        DEEZER_USER_ID = os.getenv("DEEZER_USER_ID")
        DEEZER_PLAYLIST_ID = os.getenv("DEEZER_PLAYLIST_ID")
        user_inputs = UserInputs(
            plex_url=PLEX_URL,
            plex_token=PLEX_TOKEN,
            plex_username=PLEX_USERNAME,
            plex_password=PLEX_PASSWORD,
            server_name=SERVER_NAME,
            write_missing_as_csv=WRITE_MISSING_AS_CSV,
            append_service_suffix=APPEND_SERVICE_SUFFIX,
            add_playlist_poster=ADD_PLAYLIST_POSTER,
            add_playlist_description=ADD_PLAYLIST_DESCRIPTION,
            append_instead_of_sync=APPEND_INSTEAD_OF_SYNC,
            wait_seconds=WAIT_SECONDS,
            spotify_client_id=SPOTIFY_CLIENT_ID,
            spotify_client_secret=SPOTIFY_CLIENT_SECRET,
            spotify_user_id=SPOTIFY_USER_ID,
            spotify_redirect_uri=SPOTIFY_REDIRECT_URI,
            spotify_daily_mixes=SPOTIFY_DAILY_MIXES,
            deezer_user_id=DEEZER_USER_ID,
            deezer_playlist_ids=DEEZER_PLAYLIST_ID,
        )
    else:
        i_toml = toml.loads(open('inputs.toml').read())
        user_inputs = UserInputs(
            plex_url=i_toml["plex"]["url"],
            plex_token=i_toml["plex"]["token"],
            plex_username=i_toml["plex"]["username"],
            plex_password=i_toml["plex"]["password"],
            server_name=i_toml["plex"]["server_name"],
            write_missing_as_csv=i_toml["general"]["write_missing_as_csv"],
            append_service_suffix=i_toml["general"]["append_service_suffix"],
            add_playlist_poster=i_toml["general"]["add_playlist_poster"],
            add_playlist_description=i_toml["general"]["add_playlist_description"],
            append_instead_of_sync=i_toml["general"]["append_instead_of_sync"],
            wait_seconds=i_toml["general"]["wait_seconds"],
            spotify_client_id=i_toml["spotify"]["lient_id"],
            spotify_client_secret=i_toml["spotify"]["lient_secret"],
            spotify_user_id=i_toml["spotify"]["spotify_user_id"],
            spotify_redirect_uri=i_toml["spotify"]["spotify_redirect_uri"],
            spotify_daily_mixes=i_toml["spotify"]["spotify_daily_mixes"],
            deezer_user_id=i_toml["deezer"]["user_id"],
            deezer_playlist_ids=i_toml["deezer"]["playlist_ids"],
        )

    return user_inputs
