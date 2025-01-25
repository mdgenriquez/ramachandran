import numpy as np

def load_monomer(content):
    """
    Carga un monómero desde un contenido en formato XYZ.
    """
    lines = content.splitlines()
    atom_count = int(lines[0].strip())
    structure = lines[2:]  # Ignorar la cabecera
    return atom_count, structure

def construct_polymer(atom_count, structure, n):
    """
    Construye un polímero concatenando `n` unidades del monómero.
    """
    polymer = []
    offset = np.array([0.0, 0.0, 0.0])  # Vector inicial de desplazamiento
    delta = 1.5  # Distancia entre monómeros (ajustable)

    for i in range(n):
        for line in structure:
            atom, x, y, z = line.split()
            x, y, z = float(x), float(y), float(z)
            new_position = np.array([x, y, z]) + offset
            polymer.append(f"{atom} {new_position[0]:.3f} {new_position[1]:.3f} {new_position[2]:.3f}")
        offset += np.array([delta, 0, 0])  # Incrementar en el eje X
    return polymer

def save_polymer(polymer):
    """
    Genera un archivo XYZ en texto para descargar.
    """
    output = f"{len(polymer)}\nGenerated polymer chain\n"
    output += "\n".join(polymer)
    return output
