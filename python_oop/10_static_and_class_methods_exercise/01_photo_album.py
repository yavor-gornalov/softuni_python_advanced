class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = PhotoAlbum.empty_matrix(pages)

    @staticmethod
    def empty_matrix(rows):
        matrix = []
        [matrix.append([]) for _ in range(rows)]
        return matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
        if photos_count % PhotoAlbum.PHOTOS_PER_PAGE == 0:
            return cls(photos_count // PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(photos_count // PhotoAlbum.PHOTOS_PER_PAGE + 1)

    def __get_page_with_empty_slot(self):
        page = 0
        while page < self.pages:
            if len(self.photos[page]) < self.PHOTOS_PER_PAGE:
                return page
            page += 1

    def add_photo(self, label: str):
        page = self.__get_page_with_empty_slot()
        if page is None:
            return "No more free slots"
        self.photos[page].append(label)
        slot = len(self.photos[page])
        return f"{label} photo added successfully on page {page + 1} slot {slot}"

    def display(self):
        result = "-----------\n"
        for page in self.photos:
            photos_str = '[] ' * len(page)
            result += (f"{photos_str.strip()}\n"
                       f"-----------\n")
        return result


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
