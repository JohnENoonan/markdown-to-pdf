"""
Render a pdf from a markdown file using the github styling
"""

import requests
import json
import os
import argparse
import subprocess
import contextlib
import shutil
import tempfile
from htmlFormat import formatHTML



@contextlib.contextmanager
def pushd(new_dir):
	"""
	move into a director using the `with` statement
	"""
	previous_dir = os.getcwd()
	os.chdir(new_dir)
	try:
		yield
	finally:
		os.chdir(previous_dir)

def getHTML(text: str):
	"""
	Send a POST request to GitHub via API 
	text: markdown to write
	"""
	payload = {'text': text, 'mode':"markdown"}
	headers = {	'Accept': 'application/vnd.github.v3+json' }
	response = requests.post('https://api.github.com/markdown', headers=headers, data=json.dumps(payload))

	if response.status_code == 200:
		return formatHTML(response.text)
	else:
		print("Error: Request returned '{}'".format(response.status_code))
		return formatHTML("")

def render(html: str, css: str, root: str, outfile: str, chrome_path: str):
	"""
	Render out a pdf file 
	html: string of the html to render
	css: path to the css file
	root: directory where the markdown file is
	outfile: file to write out as
	chrome_path: path to chrome.exe
	"""
	print(f"Render out to {outfile}")
	tmp = tempfile.NamedTemporaryFile(delete=False)
	html_tmp_file = tempfile.NamedTemporaryFile(dir=root, delete=False, suffix=".html")
	css_tmp_file = os.path.abspath(os.path.join(root, "github-markdown.css"))
	try:
		# make temporary html
		with open(html_tmp_file.name, 'w') as tmp:
			tmp.write(html)
		dont_delete = False
		# if the local css file already exists don't delete it when we are done
		if os.path.exists(css_tmp_file):
			dont_delete = True
		else:
			# make temporary css local to the input file
			with open(css_tmp_file, 'w') as tmp:
				shutil.copy(css, css_tmp_file)
		# export pdf using chrome
		response = subprocess.call([chrome_path, "--headless", "--disable-gpu", "--no-pdf-header-footer",
									f'--print-to-pdf={outfile}', html_tmp_file.name])
	finally:
		html_tmp_file.close()
		os.remove(html_tmp_file.name)
		if not dont_delete:
			os.remove(css_tmp_file)

def main():
	parser = argparse.ArgumentParser(description="Convert a markdown file to a PDF using the github markdown styling.",
									 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('file', help='input file name', type=str)
	parser.add_argument('export', help='file to write out', type=str)
	parser.add_argument('--chromepath', help="Path to chrome.exe", 
						dest="chrome_path", type=str, default="C:/Program Files/Google/Chrome/Application/chrome.exe")
	args = parser.parse_args()

	root, filename = os.path.split(os.path.abspath(args.file))
	css = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),"github-markdown.css"))
	print(css)
	outfile = os.path.abspath(args.export)
	# move into the working directory so that relative image paths work
	with pushd(root):
		with open(filename, 'r') as infile:
			html = getHTML(infile.read())
			render(html, css, root, outfile, args.chrome_path)

if __name__ == '__main__':
	main()