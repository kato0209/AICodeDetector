

    try:
        # Validate the certificate URL
        if not signature_chain_url.startswith("https://s3.amazonaws.com/echo.api/"):
            return False

        # Download the certificate
        with urllib.request.urlopen(signature