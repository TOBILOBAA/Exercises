from utils import unzip_with_7z
import string
zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
for first in string.ascii_lowercase:
    for second in string.ascii_lowercase:
        find_me = first + second
        secret_password = find_me + "bcmpda"
        sucess = unzip_with_7z(zip_file_path, dest_path, secret_password)
