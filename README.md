# Markdown to PDF
Create a PDF from a markdown file using GitHub's styling.

## Install
run
```bash
pip install -r requirements.txt
```
Make sure to have Chrome installed on the computer as well.

## Usage
To create a pdf run
```bash
python mdToPdf.py <markdown_file.md> <outfile.pdf>
```

Because the pdf is rendered using Chrome you may need to supply the path to exe. The default value is `C:/Program Files/Google/Chrome/Application/chrome.exe` but if you have Chrome at a different location it can passed in as a CLI argument
```bash
python mdToPdf.py <markdown_file.md> <outfile.pdf> --chromepath "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
```
