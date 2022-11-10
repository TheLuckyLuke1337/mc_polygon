from sys import argv

from mc_poly import run

if __name__ == '__main__':
    n = int(argv[1])
    L = int(argv[2])
    run(n, L)
