import requests
from config import ALPHAVANTAGE_API_KEY

def validate_ticker(symbol):
    BASE_URL = "https://www.alphavantage.co/query"

    params = {
        "function": "SYMBOL_SEARCH",
        "keywords": symbol,
        "apikey": ALPHAVANTAGE_API_KEY,
    }

    resp = requests.get(BASE_URL, params=params)
    data = resp.json()

    if "bestMatches" in data and len(data["bestMatches"]) > 0:
        matches = data["bestMatches"]
        print(matches)
        if len(matches) == 1:
            return matches[0]
        else:
            if len(matches) > 1 and float(matches[0]['9. matchScore']) == 1.0000:
                return matches[0]
            else:
            # if multiple matches are found, where top matchScore is not 1.0, then let user choose
                print(f"Which of these ticker symbol are you interested in?")
                for i, sym in enumerate(matches):
                    print(f"{i}. {sym['1. symbol']} ({sym['2. name']})")
                while True:
                    try:
                        choice = int(input("Please enter the number corresponding to the desired ticker symbol: "))
                        if 0 <= choice <= len(matches) - 1:
                            return matches[choice]
                        else:
                            print("Invalid choice. Please try again")
                    except ValueError:
                        print("Invalid input. Please enter a number")
    else:
        return None

user_input = input("Please enter the ticker symbol: ")
output = validate_ticker(user_input)

print(output)
