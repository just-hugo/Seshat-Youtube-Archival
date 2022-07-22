from weasyprint import HTML, CSS

HTML('https://www.google.com/').write_pdf('/Users/hugo/Downloads/google.pdf',
    stylesheets=[CSS(string='body { font-family: serif !important }')])