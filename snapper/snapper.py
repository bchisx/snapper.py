import subprocess
import time

def read_config():
    config = {}
    with open('config.txt', 'r') as file:
        for line in file:
            name, value = line.strip().split('=')
            config[name] = value
    return config

def take_screenshot():
    result = subprocess.run(['./take_screenshot.sh'], capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"Error taking screenshot: {result.stderr}")

if __name__ == "__main__":
    config = read_config()
    interval = int(config.get('interval', 300))  # Default to 300 seconds if not specified

    while True:
        take_screenshot()
        time.sleep(interval)
 

