import os

def extract_title(dir, file):
    with open(f"{dir}/{file}", "r") as adoc:
        line = adoc.readline()
        while line:
            if (line.startswith("= ")):
                title = line
                break
            return adoc.readline()
    return file

def add_articles():
    dir = 'articles'
    files = os.listdir(dir)
    files.sort()

    with open("README.adoc", "a") as f:
        for file in files:
            line = extract_title(dir, file)
            
            # f.write(f'include::{dir}/{file}[leveloffset=+2]\n')
            f.write(f'* link:{dir}/{file.replace(".adoc", ".html")}[{line.strip()[2:]}]\n')

        
if __name__ == "__main__":
    add_articles()