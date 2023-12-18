import pyminizip
import os
  



def zip(input_files, output, password, compress_level):
    # flat files
    pyminizip.compress_multiple(input_files, [], output, password, compress_level)


    # full directory structure
    # input_path = [os.path.join(os.getcwd(), 'test1.txt'), os.path.join(os.getcwd(), 'test2.txt')]

    # directory names per file
    # input_path = ["test1", "test2"]

    # with folder per filename
    # pyminizip.compress_multiple(input_files, input_path, output, password, compress_level)

def unzip(zip_file, password, unzip_dest=""):
    # if the dest directory for unzip is not set, then set it as the source zip file name
    if not unzip_dest:
        unzip_dest = zip_file.split(".zip")[0]

    if not os.path.exists(unzip_dest):
        os.makedirs(unzip_dest)

    pyminizip.uncompress(zip_file, password, unzip_dest, 0)


def main():
    input_files = ["test1.txt", "test2.txt"]
    zip_file = "zip.zip"
    password = "123"
    compress_level = 5
    zip(input_files, zip_file, password, compress_level)

    # unzip_dest = "unzip"
    # unzip(zip_file, password, unzip_dest)
    unzip(zip_file, password)

if __name__ == "__main__":
    main()