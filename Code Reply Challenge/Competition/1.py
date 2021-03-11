# Pytherife Teen 

import sys

# Analizar los datos del input 
def parse_testcases(io):
    # Leer el número de casos
    T = int(io.readline())
    tc = []

    # Para cada test case
    for _ in range(T):
        # Leer los datos del input
        n = int(io.readline())
        # a, b = map(int, io.readline().strip().split())
        a = list(map(int, io.readline().strip().split()))
        # Añadir a la lista de casos
        tc.append((n,a))

    # Retornar todos los casos analizados
    return tc

# Función para resolver un caso
def solve_testcase(t):
    # Obtener los datos del caso
    (n,a) = t

    i = 0
    j = 2
    cnt = 1
    m = min(a)
    while j < m:
        if a[i]%j !=0:
            j += 1
        else:
            if i == n-1:
                cnt+=1
                i=0
                j+=1
            else:
                i+=1

    return cnt


# Resolución 
def solve(input, output):
    # Enumerar todos los casos
    for i, t in enumerate(parse_testcases(input)):
        # Imprimir la solución del caso
        print(f"Case #{i+1}:", solve_testcase(t), file=output)

if __name__ == "__main__":
    fin = open(r'C:\Users\Andrey\Documents\python_projects\demos\Competitive programming\Code Reply\input.txt', "r")
    fout = open(r"C:\Users\Andrey\Documents\python_projects\demos\Competitive programming\Code Reply\output.txt", "w")
    solve(fin, fout)