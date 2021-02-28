import os, shutil

path = input('Please write the path of folder: ')
audio_list = ['.mp3', '.m4a', '.wav', '.flac']
video_list = ['.mp4', '.mkv', '.MKV', '.mpeg']
documents_list = ['.html', '.htm', ',doc', '.pdf', '.txt']
codes_list = ['.py', 'sml']
images_list = ['.jpg', '.jpeg', '.png', '.tif', '.gif', '.svg', '.webp', '.raw']

lists = os.listdir(path)

for item in lists:
    for audio_ext in audio_list:
        if item.endswith(audio_ext):
            if os.path.exists('Audio') == False: 
                os.mkdir('Audio')
            shutil.move(item,os.path.join(path,f'Audio\{item}'))

    for documents_ext in documents_list:
        if item.endswith(documents_ext):
            if os.path.exists('Documents') == False: 
                os.mkdir('Documents')
            shutil.move(item,os.path.join(path,f'Documents\{item}'))

    for video_ext in video_list:
        if item.endswith(video_ext):
            if os.path.exists('Video') == False: 
                os.mkdir('Video')
            shutil.move(item,os.path.join(path,f'Video\{item}'))

    for codes_ext in codes_list:
        if item.endswith(codes_ext):
            if os.path.exists('Codes') == False: 
                os.mkdir('Codes')
            shutil.move(item,os.path.join(path,f'Codes\{item}'))

    for images_ext in images_list:
        if item.endswith(images_ext):
            if os.path.exists('Images') == False: 
                os.mkdir('Images')
            shutil.move(item,os.path.join(path,f'Images\{item}'))

    
        

