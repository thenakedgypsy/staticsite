import os
import shutil
from markdownConverter import MarkdownConverter


class PageGenerator():

    def copyToDir(self, fromPath,toPath):
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
        
    def generatePage(self,fromPath,templatePath,toPath):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        fromPath = os.path.join(base_dir,fromPath)
        templatePath = os.path.join(base_dir, templatePath)
        toPath = os.path.join(base_dir, toPath)
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


