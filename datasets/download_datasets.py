import urllib.request 
import urllib.parse
import gzip
import shutil
import os


'''
File URL list must be regenerated regularly, copied and pasted in. These links automatically expire.
The following datasets were used:
https://worksheets.codalab.org/worksheets/0x62eefc3e64e04430a1a24785a9293fff
    {SQuAD 2 train, dev}
'''


files = [
    "https://storageclwsprod1.blob.core.windows.net/bundles/0x3782ee0e5ed044d7a7e70d12553baf12/contents.gz?se=2025-11-06T17%3A40%3A36Z&sp=rt&sv=2019-12-12&sr=b&rscd=inline%3B%20filename%3D%22train-v2.0.json%22&rsce=gzip&rsct=application/json&sig=0uXjPXQNw4drqg9aZz6HPwNqL2PWyS21SQy6oFyI2QM%3D",
    "https://storageclwsprod1.blob.core.windows.net/bundles/0xb30d937a18574073903bb38b382aab03/contents.gz?se=2025-11-06T17%3A40%3A58Z&sp=rt&sv=2019-12-12&sr=b&rscd=inline%3B%20filename%3D%22dev-v2.0.json%22&rsce=gzip&rsct=application/json&sig=MX2qHDYMZDl2/iQUxNVUvEK%2BKHKEOBX79F%2BrAauu1So%3D",
]

def download(files):
    for url in files:
        filename = "downloaded_file.json"
        if "filename%3D%22" in url:
            filename = urllib.parse.unquote(url.split("filename%3D%22")[-1].split("%22")[0])

        compressed_filename = filename + ".gz"

        print(f"Downloading {filename}")

        #first, download the file. It will be compressed as a gzip.
        with urllib.request.urlopen(url) as response, open(compressed_filename, "wb") as out_file:
            out_file.write(response.read())

        #gzip -> json
        with gzip.open(compressed_filename, "rb") as f_in, open(filename, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)

        #delete the gzip
        os.remove(compressed_filename)

download(files)