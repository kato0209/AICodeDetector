

    """
    Execute the Discord webhook call
    """
    webhook_url = "YOUR_DISCORD_WEBHOOK_URL"
    data = {
        "content": "Hello, this is a message from your webhook!"
    }
    
    response = requests.post(webhook_url, json=data)
    
    if response.status_code == 204:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
