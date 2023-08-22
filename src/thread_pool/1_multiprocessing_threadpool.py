from multiprocessing.pool import ThreadPool
import time


def task(n):
    print(f"Task {n} started")
    time.sleep(2)
    print('\n')
    print(f"Task {n} completed")
    return f"Task {n} result"


def main():
    with ThreadPool(processes=3) as pool:
        results = pool.map(task, [1, 2, 3])

    print("\nAll tasks completed:")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
