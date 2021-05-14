def get_cur_file_path():
    import os
    return os.path.dirname(__file__)


def get_cur_prj_path():
    import os
    return os.path.abspath(os.curdir)


def write_file(file_path: str, content: bytes):
    with open(file_path, 'wb') as f:
        f.write(content)
        f.close()


def read_file(file_path: str):
    # buf = bytearray(os.path.getsize(file_path))
    with open(file_path, 'rb') as f:
        buf = f.read()
        f.close()
    return buf
