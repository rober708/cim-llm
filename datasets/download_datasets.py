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
    "example_url.com"
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