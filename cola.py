from collections import deque

cola = (["ana", "carlos"])

cola.append("jorge")
cola.append("andres")
print("cola actual", cola)

atendido = cola.popleft()
print(f"se atendio a: {atendido}")

print("cola restante: ", cola)

atendido = cola.popleft()
print(f"se atendio a: {atendido}")
print("cola restante: ", cola)