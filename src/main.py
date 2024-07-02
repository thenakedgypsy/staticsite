from generator import PageGenerator

def main():
    generator = PageGenerator()
    generator.generatePage("content/index.md", "template.html" , "public/index.html")

main()
