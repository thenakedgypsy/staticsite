import os
import shutil


class pageGenerator():

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