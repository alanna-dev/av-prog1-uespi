# Equipe: Alanna Gilcielle Mesquita de Farias e Maria Graziela Brito de Souza


def alternate(n, seq):
    unpaired = True
    m = 1
    for i in range(1, n):
        if unpaired:
            if seq[i] % 2 == 0:
                unpaired = False
                m += 1
        else:
            if seq[i] % 2 != 0:
                unpaired = True
                m += 2
    return m if unpaired else "NAO"


n = int(input('informe N: '))
if n > 1:
    seq = [int(x) for x in input('informe a sequencia: ').strip().split()]
    print(alternate(n, seq))
    print('%')
else:
    raise ValueError('Invalid value for N')

    
