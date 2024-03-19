from datetime import datetime


def title():
    print('The Timer Program')


def timer():
    input('\nPress Enter to start . . . ')
    start_time = datetime.now()
    print('Start time: ', start_time)

    input('\nPress Enter to stop . . . ')
    stop_time = datetime.now()
    print('Stop time: ', stop_time)

    elapsed_time = get_elapsed_time(start_time, stop_time)
    return elapsed_time


def get_elapsed_time(start_time, stop_time):
    elapsed_time = stop_time - start_time
    return elapsed_time


def main():
    title()
    elapsed_time = timer()

    print('ELAPSED TIME\nTime: ', elapsed_time)


if __name__ == '__main__':
    main()
