from random import randint

def generate_file(start, stop, r, n):
    with open(f'17-{n}.txt', 'w') as f:
        for i in range(r):
            x = randint(start, stop + 1)
            f.write(f'{x}\n')

        return f

result = generate_file(0, 10001, 10000, 9)
print(result)
