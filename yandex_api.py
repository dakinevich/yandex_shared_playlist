from yandex_music import Client
import re
from config import YM_TOKEN

client = Client(YM_TOKEN).init()

def is_yandex_music_track_link(text):
    pattern = r'https://music\.yandex\.ru/album/\d+/track/\d+'
    
    match = re.search(pattern, text)
    
    return match is not None

def extract_ids_from_url(url):
    pattern = r'https://music\.yandex\.ru/album/(\d+)/track/(\d+)'
    
    match = re.search(pattern, url)
    
    if match:
        album_id = match.group(1)
        track_id = match.group(2)
        return album_id, track_id
    else:
        return None, None

def add_track(playListId, url):
    
    album_id, track_id = extract_ids_from_url(url)
    tracks_ids = [str(track.id) for track in client.usersPlaylists(playListId).tracks]
    if track_id in tracks_ids:
        return False
    else:
        client.usersPlaylists(playListId).insert_track(track_id, album_id)
        return True

        
