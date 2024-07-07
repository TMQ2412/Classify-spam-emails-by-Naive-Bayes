from . import *
import os
# "Tên giải thuật": {
#     "fields": ["Tên đặc trưng 1", "Tên đặc trưng 2", "Tên đặc trưng 3", "Tên đặc trưng 4"],
#     "path": os.path.join(os.path.dirname(__file__), "tên file.py"),
# },
ALGORITHMS = {

    "Naive Bayes": {
        "fields": ["Outlook", "Temperature", "Humidity", "Wind"],
        "path": os.path.join(os.path.dirname(__file__), "naive_bayes.py"),
    },
    
}
