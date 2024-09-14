import base64
import zlib
import gzip
import sys

def is_zlib_compressed(data):
    try:
        # zlib decompress attempt
        zlib.decompress(data)
        return True
    except zlib.error:
        return False

def is_gzip_compressed(data):
    try:
        # gzip decompress attempt
        gzip.decompress(data)
        return True
    except (gzip.BadGzipFile, OSError):
        return False

def decompress_data(file_path):
    try:
        # read file
        with open(file_path, 'r') as file:
            base64_data = file.read().strip()

        # decode data
        decoded_data = base64.b64decode(base64_data)
        print(f"Base64 decoded data length: {len(decoded_data)} bytes")

        # check zlib then gzip then none
        if is_zlib_compressed(decoded_data):
            print("Data is zlib-compressed, decompressing...")
            decompressed_data = zlib.decompress(decoded_data)
            print("Successfully decompressed with zlib!")
            print(decompressed_data.decode('utf-8'))
        elif is_gzip_compressed(decoded_data):
            print("Data is gzip-compressed, decompressing...")
            decompressed_data = gzip.decompress(decoded_data)
            print("Successfully decompressed with gzip!")
            print(decompressed_data.decode('utf-8'))
        else:
            print("Data is not compressed. Proceeding with base64-decoded data.")
            print(decoded_data.decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decompress.py <file_path>")
    else:
        file_path = sys.argv[1]
        decompress_data(file_path)
