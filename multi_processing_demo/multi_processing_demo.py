from multiprocessing import Pool


def calculate_square_of(int_x):
    return int_x * int_x


if __name__ == '__main__':
    print('Hello parallel processing world')
    pool = Pool(5)
    pool_result = pool.map(calculate_square_of, range(5))
    print(pool_result)
