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
        #n = int(io.readline())
        n,k = map(int, io.readline().strip().split())
        p = list(map(int, io.readline().strip().split()))
        # Añadir a la lista de casos
        tc.append((n,k,p))

    # Retornar todos los casos analizados
    return tc

# Función para resolver un caso
def solve_testcase(t):
    # Obtener los datos del caso
    (n,k,p) = t
    a = []
    b = []
    '''
    for i in range(0,n):
        a.append(i)
        b.append(i)
    '''

    a = list(range(0,n))
    b = a[:]

    for i in range(k):
        for j in range(n):
            b[p[j]] = a[j]

        a = b[:]   
    return a

# Resolución 
def solve(input, output):
    # Enumerar todos los casos
    for i, t in enumerate(parse_testcases(input)):
        # Imprimir la solución del caso
        print(f"Case #{i+1}:", *solve_testcase(t), file=output)

if __name__ == "__main__":
    fin = open(r'C:\Users\Andrey\Documents\python_projects\demos\Competitive programming\Code Reply\input.txt', "r")
    fout = open(r"C:\Users\Andrey\Documents\python_projects\demos\Competitive programming\Code Reply\output.txt", "w")
    solve(fin, fout)