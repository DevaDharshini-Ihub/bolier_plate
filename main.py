from config import API_URL, API_KEY
from utils import get_data_from_api

def main():
    # Fetch data from the API
    data = get_data_from_api(API_URL, API_KEY)
    if data:
        print("Data fetched successfully!")
        print(data)
    else:
        print("No data found.")

if __name__ == '__main__':
    main()
