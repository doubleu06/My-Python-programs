import os
import shutil

# 1. get the folder path
folderToBeSorted = ''   # type the path of the folder to be sorted

# 2. make a new folder
newFolderPath = ''   # type the path of the folder where the new folder will be created

if not os.path.exists(newFolderPath):
    os.mkdir(newFolderPath)
else:
    print('folder exists.')
    exit()

# 3. walk in the folder
for path,folders,files in os.walk(folderToBeSorted):
    #print(path)
    # 4. handle each sub folder separately
    if '\\' in path:
        newPath = path.replace('\\','/')
        sourcedir = newPath
    else:
        sourcedir = path
    #print(sourcedir)

    for file in os.listdir(sourcedir):
        extensions = ['jpeg','jpg','png','txt','epub','pdf','mp3','mp4','wav','exe','py',
                    'srt','doc','docx','apk','mkv','rar','memo','zip','html','xhtml','JPG',
                    'PDF','m4a','xlsx','vcf','aac','xls','MP3','pptx']

        # 5. find the extensions
        if '.' in file:
            splitingName = file.split('.')

            # 6. make separate folder for extensions
            if splitingName[-1] in extensions:
                if  not os.path.exists(newFolderPath + splitingName[-1] + ' files'):
                    os.mkdir(newFolderPath + splitingName[-1] + ' files')
            else:
                if not os.path.exists('D:/new/misc files'):
                    os.mkdir(newFolderPath + 'misc files')

            # 7. move the files in the respective folders
            if splitingName[-1] in extensions:
                if not os.path.exists(newFolderPath + splitingName[-1] + ' files' + '/' + file):
                    shutil.move(sourcedir + '/' + file, newFolderPath + splitingName[-1] + ' files')
                else:
                    print('file exists.')
            else:
                if not os.path.exists(newFolderPath + 'misc files' + '/' + file):
                    shutil.move(sourcedir + '/' + file, newFolderPath + 'misc files')
                else:
                    print('file exists.')

# 8. handle the exceptions


