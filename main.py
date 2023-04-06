from os import listdir, popen, mkdir, path

def arrangeFiles():
    distDir = 'languages'
    if not distDir in listdir('.'):
        mkdir(distDir)

    targetDir = 'files'
    targetFiles = listdir(targetDir)

    for file in targetFiles:
        language = file.split('-')[0]
        distLanguages = listdir(distDir)                    # repeated with each file for integrity

        if not language in distLanguages:                   # create a language directory if it doesn't exist
            languagePath = path.join(distDir, language)
            mkdir(languagePath)

        filePath = path.join(targetDir, file)               # file to copy
        fileDist = path.join(distDir, language, file)       # distenation

        copyCmd = f'cp {filePath} {fileDist}'
        popen(copyCmd)


if __name__ == '__main__':
    arrangeFiles()