from datetime import datetime

class ArchiveItem:
    def __init__(self, uid: str, title: str, year: int):
        self.uid = uid
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.uid} {self.title} {self.year}"

    def __eq__(self, other):
        return self.uid == other.uid

    def is_recent(self, n: int) -> bool:
        return (datetime.year - self.year) <= n

class Book(ArchiveItem):
    def __init__(self, uid: str, title: str, year: int, author: str, pages: int):
        super().__init__(uid, title, year)
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Book -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Author: {self.author}, Pages: {self.pages}"

class Article(ArchiveItem):
    def __init__(self, uid: str, title: str, year: int, journal: str, doi: str):
        super().__init__(uid, title, year)
        self.journal = journal
        self.doi = doi

    def __str__(self):
        return f"Article -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Journal: {self.journal}, DOI: {self.doi}"

class Podcast(ArchiveItem):
    def __init__(self, uid: str, title: str, year: int, host: str, duration: int):
        super().__init__(uid, title, year)
        self.host = host
        self.duration = duration

    def __str__(self):
        return f"Podcast -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Host: {self.host}, Duration: {self.duration} mins"

def save_to_file(items: list, filename: str):
    with open(filename, 'w') as f:
        for item in items:
            if isinstance(item, Book):
                f.write(f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n")
            elif isinstance(item, Article):
                f.write(f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n")
            elif isinstance(item, Podcast):
                f.write(f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n")

def load_from_file(filename: str) -> list:
    items = []
    with open(filename, 'r') as f:
        for line in f:
            data = line.strip().split(',')
            if data[0] == 'Book':
                items.append(Book(data[1], data[2], int(data[3]), data[4], int(data[5])))
            elif data[0] == 'Article':
                items.append(Article(data[1], data[2], int(data[3]), data[4], data[5]))
            elif data[0] == 'Podcast':
                items.append(Podcast(data[1], data[2], int(data[3]), data[4], int(data[5])))
    return items

def main():
    items = [
        Book("B001", "Deep Learning", 2018, "Ian Goodfellow", 775),
        Book("B002", "Python Programming", 2023, "John Smith", 500),
        Article("A101", "Quantum Computing", 2022, "Nature", "10.1234/qc567"),
        Article("A102", "AI Ethics", 2024, "Science", "10.1234/ai789"),
        Podcast("P301", "TechTalk AI", 2023, "Jane Doe", 45),
        Podcast("P302", "Future of Computing", 2024, "Bob Wilson", 60)
    ]

    save_to_file(items, "archive.txt")

    loaded_items = load_from_file("archive.txt")

    print("All Items:")
    for item in loaded_items:
        print(item)

    print("\nRecent Items:")
    for item in loaded_items:
        if item.is_recent(5):
            print(item)

    print("\nArticles with DOI starting '10.1234':")
    for item in loaded_items:
        if isinstance(item, Article) and item.doi.startswith("10.1234"):
            print(item)

if __name__ == "__main__":
    main()
