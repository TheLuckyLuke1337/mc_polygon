from sys import argv

from mc_poly import generate_and_display_trace as run

if __name__ == '__main__':
    n = argv[1]
    L = argv[2]
    try:
        rotation = float(argv[3])
    except IndexError:
        rotation = 0
    if not n in ('o',):
        n = int(n)
    L = float(L)
    run(n, L, rotation)
