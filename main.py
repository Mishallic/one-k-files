import sys
from datetime import datetime
from os import listdir, popen, mkdir, path

def arrangeFiles(verbose):
    distDir = 'languages'
    if not distDir in listdir('.'):
        mkdir(distDir)

    targetDir = 'files'
    targetFiles = listdir(targetDir)

    for file in targetFiles:
        try:
            language = file.split('-')[0]
            distLanguages = listdir(distDir)                    # repeated with each file for integrity

            if not language in distLanguages:                   # create a language directory if it doesn't exist
                languagePath = path.join(distDir, language)
                mkdir(languagePath)

            filePath = path.join(targetDir, file)               # file to copy
            fileDist = path.join(distDir, language, file)       # distenation
            copyCmd = f'cp {filePath} {fileDist}'
            popen(copyCmd)

        except Exception as e:
            if verbose:
                f = open("errLog.txt", "a")
                time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                err = f'[{time}] {file} [ERR]: {str(e)}\n'
                f.write(err)
                f.close()


if __name__ == '__main__':
    verbose = '-verbose' in sys.argv
    arrangeFiles(verbose)