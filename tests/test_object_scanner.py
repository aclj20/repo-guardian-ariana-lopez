from guardian.object_scanner import *
import pytest

def test_objeto_valido(tmp_path):
    # Arrange
    contenido = b"hello world\n"
    header = b"blob " + str(len(contenido)).encode() + b"\0"
    full = header + contenido
    sha = hashlib.sha1(full).hexdigest()
    obj_path = tmp_path / ".git" / "objects" / sha[:2] / sha[2:]
    obj_path.parent.mkdir(parents=True, exist_ok=True)
    obj_path.write_bytes(zlib.compress(full))

    # Act
    resultado = read_loose(obj_path)

    # Assert
    assert resultado.tipo == "blob"
    assert resultado.size == len(contenido)
    assert resultado.sha == sha

def test_ruta_invalida(tmp_path):
    # Arrange
    archivo = tmp_path / "sin_formato" / "archivo"
    archivo.parent.mkdir(parents=True)
    archivo.write_bytes(b"cualquier cosa")

    # Act & Assert
    with pytest.raises(ValueError, match="Ruta no coincide con formato Git loose object"):
        read_loose(archivo)


def test_cabecera_malformada(tmp_path):
    # Arrange
    contenido = b"contenido invalido"
    full = b"blob42\0" + contenido  # sin espacio entre tipo y size
    sha = hashlib.sha1(full).hexdigest()
    path = tmp_path / ".git" / "objects" / sha[:2] / sha[2:]
    path.parent.mkdir(parents=True)
    path.write_bytes(zlib.compress(full))

    # Act & Assert
    with pytest.raises(ValueError, match="Cabecera malformada"):
        read_loose(path)

def test_tamano_inconsistente(tmp_path):
    # Arrange
    contenido = b"hola"
    header = b"blob 999\0"
    full = header + contenido
    sha = hashlib.sha1(full).hexdigest()
    path = tmp_path / ".git" / "objects" / sha[:2] / sha[2:]
    path.parent.mkdir(parents=True)
    path.write_bytes(zlib.compress(full))

    # Act & Assert
    with pytest.raises(ValueError, match="Tamaño inconsistente"):
        read_loose(path)

def test_sha_incorrecto(tmp_path):
    # Arrange
    contenido = b"alterado"
    header = b"blob 8\0"
    full = header + contenido
    sha_falso = "deadbeef" * 5  # 40 hex ficticio
    path = tmp_path / ".git" / "objects" / sha_falso[:2] / sha_falso[2:]
    path.parent.mkdir(parents=True)
    path.write_bytes(zlib.compress(full))

    # Act & Assert
    with pytest.raises(ValueError, match="SHA no coincide"):
        read_loose(path)

def test_tipo_desconocido(tmp_path):
    # Arrange
    contenido = b"abc"
    header = b"unknown 3\0"
    full = header + contenido
    sha = hashlib.sha1(full).hexdigest()
    path = tmp_path / ".git" / "objects" / sha[:2] / sha[2:]
    path.parent.mkdir(parents=True)
    path.write_bytes(zlib.compress(full))

    # Act
    resultado = read_loose(path)

    # Assert
    assert resultado.tipo == "unknown"
    assert resultado.size == 3
