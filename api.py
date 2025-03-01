import requests

def fectch_random_user_api():
    url ="https://rapidapi.com/collection/list-of-free-apis"
    
    response = requests.get(url)
    data = response.json()

    if data ["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = username = user_data["location"]["country"]
        return username,country
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        username,country = 
        fectch_random_user_api()
        print(f"username:{username}\ncountry:{country}")
    except Exception as e:
        print(str(e)) 
if __name__ == "__main__":
    main()

