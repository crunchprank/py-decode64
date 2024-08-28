import base64
import zlib
import gzip
import sys

def decompress_data(file_path):
    try:
        # read file
        with open(file_path, 'r') as file:
            compressed_data = file.read().strip()

        # decode data
        decoded_data = base64.b64decode(compressed_data)

        # decompress with zlib first
        try:
            decompressed_data = zlib.decompress(decoded_data)
            print("Successfully decompressed with zlib!")
            print(decompressed_data.decode('utf-8'))
        except zlib.error as e:
            print(f"zlib decompression failed: {e}")

            # if zlib fails, try gzip
            try:
                decompressed_data = gzip.decompress(decoded_data)
                print("Successfully decompressed with gzip!")
                print(decompressed_data.decode('utf-8'))
            except gzip.BadGzipFile as e:
                print(f"gzip decompression failed: {e}")
                
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decompress.py <file_path>")
    else:
        file_path = sys.argv[1]
        decompress_data(file_path)

