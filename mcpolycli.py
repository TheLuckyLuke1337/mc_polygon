from sys import argv

from mc_poly import run

if __name__ == '__main__':
    n = argv[1]
    L = argv[2]
    if n != 'o':
        n = int(n)
    L = int(L)
    run(n, L)
