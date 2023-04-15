from flask import Flask, request, render_template
from PyPDF2 import PdfReader

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def count_pages():
    if request.method == 'POST':
        pdf_file = request.files['pdf_file']
        pdf_reader = PdfReader(pdf_file)
        print(pdf_reader.pages)
        num_pages = len(pdf_reader.pages)
        
        return render_template('result.html', num_pages=num_pages)
    else:
        return render_template('upload.html')

if __name__ == '__main__':
    app.run()
