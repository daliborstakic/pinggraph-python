import time
from pythonping import ping

hostname = '192.168.1.1'


def main():
    while True:
        response_list = ping(hostname, verbose=True)

        for response in response_list:
            print(response.time_elapsed_ms)

        time.sleep(1)


if __name__ == '__main__':
    main()
