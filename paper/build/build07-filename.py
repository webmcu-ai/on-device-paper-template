import subprocess
import os
import sys
import asyncio

async def myBuildPdfDirectly(myInputFile):
    # Configuration
    myOutputFolderName = "output"
    
    # Validate input file exists
    if not os.path.exists(myInputFile):
        print(f"Error: File '{myInputFile}' not found!")
        return False
    
    # Validate it's a .tex file
    if not myInputFile.endswith('.tex'):
        print(f"Error: '{myInputFile}' is not a .tex file!")
        return False
    
    myBaseName = os.path.splitext(myInputFile)[0]
    myCurrentDir = os.path.dirname(os.path.abspath(__file__))
    myOutputDir = os.path.join(myCurrentDir, myOutputFolderName)
    
    if not os.path.exists(myOutputDir):
        os.makedirs(myOutputDir)
    
    try:
        print(f"Running pdflatex on {myInputFile}...")
        
        # We run it twice to resolve citations/references
        for myIteration in range(2):
            print(f"Pass {myIteration + 1}...")
            subprocess.run([
                "pdflatex",
                "-interaction=nonstopmode", # Don't stop for every tiny error
                f"-output-directory={myOutputFolderName}",
                myInputFile
            ], check=True)
        
        print(f"\nSuccess! Your PDF is in the '{myOutputFolderName}' folder.")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False
    except FileNotFoundError:
        print("Error: 'pdflatex' not found. Is MiKTeX installed and in your PATH?")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file.tex>")
        print("Example: python script.py arxiv_paper.tex")
        sys.exit(1)
    
    myInputFile = sys.argv[1]
    asyncio.run(myBuildPdfDirectly(myInputFile))