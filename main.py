import os
import requests
import zipfile

url = "https://upload.itcollege.ee/~aleksei/random_files_without_extension.zip"
zip_path = "random_files.zip"
response = requests.get(url)
with open(zip_path, "wb") as file:
    file.write(response.content)


with zipfile.ZipFile(zip_path, "r") as myzip:
    myzip.extractall("random_files")


jpeg_signature = b'\xFF\xD8'

with os.scandir("random_files/random_files") as it:
    for entry in it:
        with open(entry.path, "rb") as file:
            file_signature = file.read(2)

        if file_signature == jpeg_signature:
            if not entry.path.endswith(".jpeg"):
                new_file_path = entry.path + ".jpeg"
                os.replace(entry.path, new_file_path)
        else:
            os.remove(entry.path)

print("end")