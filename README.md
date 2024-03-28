# HULK - HTTP Unbearable Load King

HULK is a Python script designed for launching a Denial of Service (DoS) attack against a target web server. It simulates a flood of HTTP requests to overwhelm the server and make it unavailable to legitimate users.

## Table of Contents
- [How to Use](#how-to-use)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
  - [Example](#example)
  - [Note](#note)
- [How It Works](#how-it-works)
- [Disclaimer](#disclaimer)

## How to Use

### Prerequisites
- Python 3.x
- Standard Python libraries (`urllib`, `sys`, `threading`, `random`, `re`)

### Usage
1. Clone or download the HULK script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using the following command:

    ```
    python hulk.py <url> [safe]
    ```

    - `<url>`: The URL of the target website or server.
    - `[safe]` (optional): Adding "safe" after the URL will auto-shutdown the attack after DoS.

### Example
    ```
    python hulk.py http://example.com safe
    ```

This command will initiate a HULK attack on `http://example.com` and automatically shut down after DoS.

### Note
- Ensure to use this script responsibly and only on systems you have permission to test.
- Using this script to attack websites without authorization is illegal and unethical.

## How It Works

1. **HTTP Request Generation**: The script generates a flood of HTTP requests to overwhelm the target server. It uses random user agents, referers, and parameters to simulate legitimate traffic.

2. **Threading**: The script utilizes threading to enable concurrent execution of multiple HTTP requests, increasing the efficiency of the attack.

3. **Monitoring**: A monitoring thread continuously tracks the number of requests sent. If the "safe" mode is enabled and the server responds with an HTTP 500 error, indicating it's overwhelmed, the attack is automatically terminated.

## Disclaimer

- This script is intended for educational and testing purposes only.
- Use it responsibly and with proper authorization.
- The developer is not responsible for any misuse or damage caused by this script.
