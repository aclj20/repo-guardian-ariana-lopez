from pathlib import Path
import zlib
import re
import hashlib
from dataclasses import dataclass

GIT_LOOSE_PATH_RE = re.compile(
    r".*[/\\]\.git[/\\]objects[/\\]([0-9a-f]{2})[/\\]([0-9a-f]{38})$"
)

class GitObject:
    def __init__(self, tipo: str, size: int, contenido:bytes, sha:str):
        self.tipo = tipo
        self.size = size
        self.contenido = contenido
        self.sha = sha

def read_loose(path: Path) -> GitObject:

    match = GIT_LOOSE_PATH_RE.match(path.as_posix())
    if not match:
        raise ValueError("Ruta no coincide con formato Git loose object")
    
    sha_from_path = match.group(1) + match.group(2)

    try:
        raw = path.read_bytes()
        decompressed = zlib.decompress(raw)
    except Exception as e:
        raise ValueError(f"No se pudo descomprimir el objeto: {e}")
    
    try:
        header, content = decompressed.split(b'\0', 1)
        tipo, size_str = header.decode().split(' ')
        size = int(size_str)
    except Exception as e:
        raise ValueError(f"Cabecera malformada: {e}")

    
    if size != len(content):
        raise ValueError(f"Tamaño inconsistente: indicado={size}, real={len(content)}")

    
    computed = hashlib.sha1()
    computed.update(header + b'\0' + content)
    sha_actual = computed.hexdigest()

    if sha_actual != sha_from_path:
        raise ValueError(f"SHA no coincide: esperado={sha_from_path}, calculado={sha_actual}")

    return GitObject(tipo, size, content, sha_actual)




read_loose(Path(r"C:\Users\Camila Lopez\repo-guardian-ariana-lopez\.git\objects\12\0f5049fdc3942173710950c3fbebf7a36ef6cd"))