def get_data_from_api(api_url, api_key):
    # Instead of making an API request, return mock data
    print(f"Mock API call to: {api_url}")
    print(f"Using API key: {api_key}")
    return {
        "status": "success",
        "data": {
            "message": "This is mock data for testing your boilerplate."
        }
    }
