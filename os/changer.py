import os

file_path = input('Please write the path of file: ')

if file_path.endswith('.pptx'):
    pdf_file = file_path[0:-6] + '.pdf'
    with open(pdf_file, 'a') as f:
        pass

    # opened = True
    # i = 0
    # while opened:
    #     if os.path.exists(pdf_file):
    #         i += 1
    #     else:
    #         if i = 0:
    #             with open 

