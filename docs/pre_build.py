import os


def add_articles():
    dir = 'articles'
    files = os.listdir(dir)

    with open("README.adoc", "a") as f:
        for file in files:

            f.write(f'include::{dir}/{file}[leveloffset=+1]\n')

        
if __name__ == "__main__":
    add_articles()