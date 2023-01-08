# Google-Reverse-Image-Search

## Installation
Download the `main` folder (or just `main/google_reverse_search.py`) into your local directory

Run the command in your local terminal (ideally also through a virtual environment - follow this guide https://docs.python.org/3/library/venv.html#creating-virtual-environments)
```ps1
# assuming your virtual env has been set up
>> pip install -r requirements.txt
>> playwright install chromium
```

#### Note : Only works on Chrome (for now)

## Usage

Import all functions from the file with 
```py
from google_reverse_search import *
```

Then start anywhere with the three basic functions

```py
print(search_with_query(query="your query"))
print(search_with_url(url="https://link/to/photo"),num=5)
print(search_with_file(file_path="C:/path/to/file",num=20))
```

## Examples
All three functions will return the images in a similar manner

### Code
```py
res:dict = search_with_query(query="boats",num=3)
print(res)
```

### Results
_Formatted for better viewing_
```ps1
Connected...
Navigating...
Getting results...
Formatting results...
{'title': 'boats', 
    'data': [
        {'link': 'https://www.discoverboating.com/sites/default/files/small-boats_1.jpg', 'name': 'The Ultimate Guide to Small Boats | Discover Boating', 'dimensions': [1200, 795]}, 
        {'link': 'https://d1nkxkz7ge96ao.cloudfront.net/eyJidWNrZXQiOiJzbW4tbWFpbi1zaXRlLWJ1Y2tldCIsImtleSI6ImltYWdlc1wvaW1hZ2luXC9McktPcmhFcE5FN0FNV3lFQUxRMUpFOE0wTjVsc1VkekxsNU9ZcEZsLmpwZyIsImVkaXRzIjp7InJlc2l6ZSI6eyJ3aWR0aCI6MjYwMCwiaGVpZ2h0IjoxMzAwLCJmaXQiOiJjb3ZlciJ9fX0=', 'name': "Family-Friendly Offshore Center Consoles & Bay Boats from 20' to 35' |  Sportsman Boats", 'dimensions': [2600, 1300]}, 
        {'link': 'https://cdn.britannica.com/27/166127-050-5E3F9372/salmon-fishing-boat-Alaska.jpg', 'name': 'Boat | Definition, History, Types, & Facts | Britannica', 'dimensions': [1600, 1075]}
    ]
}
```

## Bugs and Issues
#### Please raise any issues you have on the `Issues` forum, and I'll take a look (hopefully)

