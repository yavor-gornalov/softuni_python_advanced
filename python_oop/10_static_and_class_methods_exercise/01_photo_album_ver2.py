from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = self.create_empty_matrix(self.pages)
        self.__next_index = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE))

    @property
    def page_index(self):
        return self.__next_index // self.PHOTOS_PER_PAGE

    @property
    def slot_index(self):
        return self.__next_index % self.PHOTOS_PER_PAGE

    def add_photo(self, label: str):
        if self.page_index >= self.pages:
            return "No more free slots"

        self.photos[self.page_index].append(label)
        result = f"{label} photo added successfully on page {self.page_index + 1} slot {self.slot_index + 1}"
        self.__next_index += 1
        return result

    def display(self):
        result = ["-----------"]
        for idx in range(self.pages):
            if self.photos[idx]:
                result.append(" ".join(["[]" for _ in range(len(self.photos[idx]))]))
            else:
                result.append("")
            result.append("-----------")
        return "\n".join(result)

    # HELPERS:
    @staticmethod
    def create_empty_matrix(count):
        matrix = []
        [matrix.append([]) for _ in range(count)]
        return matrix


album = PhotoAlbum(3)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
