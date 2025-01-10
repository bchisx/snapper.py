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
    repeat_count = int(config.get('repeat_count', 1))  # Default to 1 if not specified
    repeat_interval = int(config.get('repeat_interval', 1))  # Default to 1 second if not specified

    while True:
        for _ in range(repeat_count):
            take_screenshot()
            time.sleep(repeat_interval)
        time.sleep(interval)
