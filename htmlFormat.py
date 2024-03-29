
HTML_HEADER = """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, minimal-ui">
		<title>GitHub Markdown CSS demo</title>
		<meta name="color-scheme" content="light dark">
		<link rel="stylesheet" href="github-markdown.css">
		<style>
			body {
				box-sizing: border-box;
				min-width: 200px;   
				max-width: 980px;
				margin: 0 auto;
				padding: 45px;
			}

			@media (prefers-color-scheme: dark) {
				body {
					background-color: #0d1117;
				}
			}
		</style>
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-fork-ribbon-css/0.2.3/gh-fork-ribbon.min.css">
		<style>
			.github-fork-ribbon:before {
				background-color: #121612;
			}
		</style>
	</head>
<body>
<article class="markdown-body">
"""

HTML_END = """
</article>
</body>
</html>
"""

def formatHTML(html: str):
	"""
	Format the html to include the github css file and the html from the github API
	html: the string contents in html format to make into a proper html document
	"""
	return "{}\n{}\n{}".format(HTML_HEADER, html, HTML_END)