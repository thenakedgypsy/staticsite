from generator import PageGenerator

def main():
    
    generator = PageGenerator()
    generator.generatePagesRecursive("content", "template.html" , "public")

main()
