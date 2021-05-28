file_name = "/Users/akshayokali/akshaynayanravi/my_workspace/file_content_rendering_app/file_content_rendering_app/app/text_files/file1.txt"


with open(file_name, 'r') as f:
    print(file_name)
    text = f.read()
    print(text)
