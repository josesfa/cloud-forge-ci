def sumar(a: int, b: int) -> int:
    return a + b


def interpretar_entero(texto: str) -> int:
    return int(texto)

def ejecutar_comando(comando: str) -> int:
    import subprocess

    resultado = subprocess.call(comando, shell=True)
    return resultado