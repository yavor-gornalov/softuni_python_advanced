from typing import List

from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album):
        for current_album in self.albums:
            if current_album.name == album.name:
                return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        album_to_remove = None
        for current_album in self.albums:
            if current_album.name == album_name:
                album_to_remove = current_album
                break
        if not album_to_remove:
            return f"Album {album_name} is not found."
        if album_to_remove.published:
            return "Album has been published. It cannot be removed."
        self.albums.remove(album_to_remove)
        return f"Album {album_name} has been removed."

    def details(self):
        result = [f"Band {self.name}"]
        [result.append(a.details()) for a in self.albums]
        return "\n".join(result)
