import os
import shutil

def copy_dir(sourcePath: str, targetPath:str):
    if not (os.path.exists(sourcePath) and os.path.exists(targetPath)):
        raise FileNotFoundError("Invalid file path")
    files: list[str] = os.listdir(sourcePath)
    for i in files:
        sourceFile = os.path.join(sourcePath, i)
        targetFile = os.path.join(targetPath, i)
        print(f"Copying {sourceFile} to {targetFile}")
        if os.path.isfile(sourceFile):
            shutil.copy(sourceFile, targetFile)
        elif os.path.isdir(sourceFile):
            os.mkdir(os.path.join(targetFile))
            copy_dir(sourceFile, targetFile)