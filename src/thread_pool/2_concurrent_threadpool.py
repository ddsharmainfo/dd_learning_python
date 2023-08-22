import concurrent.futures
import time


def task(n):
    print(f"Task {n} started")
    time.sleep(2)
    print(f"Task {n} completed")
    return f"Task {n} result"


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        future1 = executor.submit(task, 1)
        future2 = executor.submit(task, 2)
        future3 = executor.submit(task, 3)

        results = [future.result() for future in concurrent.futures.as_completed([future1, future2, future3])]

        print("All tasks completed:")
        for result in results:
            print(result)


if __name__ == "__main__":
    main()
