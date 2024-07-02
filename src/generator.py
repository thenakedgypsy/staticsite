import os
import shutil
from markdownConverter import MarkdownConverter

class PageGenerator():

    def copyToDir(self, fromPath,toPath): #copies files to a directory
        if os.path.exists(toPath):
            shutil.rmtree(toPath)
        if os.path.exists(fromPath): 
            if not os.path.exists(toPath):
                os.makedirs(toPath)
            dirList = os.listdir(fromPath)
            for item in dirList:
                from_item = os.path.join(fromPath, item)
                to_item = os.path.join(toPath, item)
                if os.path.isfile(from_item):
                    shutil.copy(from_item, to_item)
                elif os.path.isdir(from_item):
                    self.copyToDir(from_item, to_item)       
        else:
            raise Exception("No Such Path")        
        
    def generatePage(self,fromPath,templatePath,toPath): #pushes .mds  to .htmls via path
        filename = os.path.basename(fromPath)
        name, ext = os.path.splitext(filename)
        newFilename = f"{name}.html"
        toPath = os.path.join(toPath, newFilename)
        if os.path.exists(toPath):
            os.remove(toPath)
        print(f"Generating page from {fromPath} to {toPath} using {templatePath}")
        with open(fromPath, "r") as file:
            markdown = file.read()
        with open(templatePath, "r") as file:
            template = file.read()
        converter = MarkdownConverter()
        title = converter.extract_title(markdown)
        html = converter.markdownToHTML(markdown)
        filledTemplate = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
        with open(toPath, "w") as dest:
            dest.write(filledTemplate)

    def generatePagesRecursive(self,fromPath,templatePath,toPath): # calls the above function recursively on a file structure
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        dirPathContent = os.path.join(base_dir,fromPath)
        templatePath = os.path.join(base_dir, templatePath)
        destDirPath = os.path.join(base_dir, toPath)
        dirList = os.listdir(dirPathContent)
        for item in dirList:
            pathToItem = os.path.join(dirPathContent, item)
            if os.path.isfile(pathToItem):
                if item.endswith(".md"):
                    self.generatePage(pathToItem,templatePath,destDirPath)
            elif os.path.isdir(pathToItem):
                newToPath = os.path.join(destDirPath, item)
                if not os.path.exists(newToPath):
                    os.makedirs(newToPath)
                self.generatePagesRecursive(pathToItem,templatePath,newToPath)





