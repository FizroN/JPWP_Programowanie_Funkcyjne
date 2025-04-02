def Headers(paragraph):
    return paragraph.startswith("##") 

def Paragraph_Length_Valid(paragraph):
    words = paragraph.split()
    return len(words) >= 50

def Keywords(akapit, keyword):
    return keyword in akapit

def Check_Document(document, slowo_kluczowe):
    header_count = 0
    keyword_found = False
    for paragraph in document:
        if Headers(paragraph):
            header_count += 1
        if Keywords(paragraph, slowo_kluczowe):
            keyword_found = True
    for paragraph in document:
        if not Paragraph_Length_Valid(paragraph):
            print(f"Akapit jest za krótki: {paragraph}")
            return False
    if header_count < 3:
        print("Brak wystarczającej liczby nagłówków!")
        return False
    if not keyword_found:
        print("Brak słowa kluczowego w dokumencie!")
        return False
    return True

document = [
    "## Nagłówek 1",
    "To jest akapit, który zawiera mniej niż 50 słów.",
    "## Nagłówek 2",
    "To jest akapit z wystarczającą liczbą słów, bo zawiera więcej niż 50 słów. Jest długi i zawiera wiele słów.",
    "## Nagłówek 3",
    "Ten akapit zawiera słowo kluczowe - ważne.",
]

keyword = input("Słowo do wyszukania: ")
print("Dokument jest poprawny!" if Check_Document(document, keyword) else "Dokument zawiera błędy!")
