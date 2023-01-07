from google_reverse_search import *

def main() -> None:    
    print(search_with_query(query="astronomy"))
    print(search_with_url(url="https://picsum.photos/100"))
    print(search_with_file(file_path="C:/Downloads/rezerorealize.jpg",num=20))
    pass

main()