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
        a = list(map(int, io.readline().strip().split()))
        b = list(map(int, io.readline().strip().split()))
        # Añadir a la lista de casos
        tc.append((n,k,a,b))

    # Retornar todos los casos analizados
    return tc

# Función para resolver un caso
def solve_testcase(t):
    # Obtener los datos del caso
    (n, k, a, b) = t

    a.sort()
    b.sort()

    
    mini = k*min(a)
    a.remove(min(a))
    mini+= k*min(a)
    m = a[n-2]*b[n-2] + a[n-3]*b[n-3]
    
    ans = [mini, m]
    return ans

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