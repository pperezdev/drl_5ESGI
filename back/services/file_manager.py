class FileManager:
    def open_file(self, path:str) -> str:
        data = ""
        with open(path, 'r') as f:
            data += f.read()
        return data