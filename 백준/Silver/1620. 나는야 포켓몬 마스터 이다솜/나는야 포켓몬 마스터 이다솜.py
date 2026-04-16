import sys

input = sys.stdin.readline


def solution():

    N, M = map(int, input().split())

    pokemon = ["missingNo"]
    poke_dict = {}
    for i in range(N):
        poke = input().strip()
        pokemon.append(poke)
        poke_dict[poke] = i+1

    for _ in range(M):
        q = input().strip()
        if q.isdigit():
            print(pokemon[int(q)])
        else:
            print(poke_dict[q])



if __name__ == "__main__":
    solution()
