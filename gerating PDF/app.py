from flask import Flask, render_template, make_response
import pdfkit

app = Flask(__name__)

config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

@app.route("/<name>/<location>")
def home(name, location):
    res = render_template("index.html", name=name, location=location)
    pdf = pdfkit.from_string(res, False, configuration=config)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

    return response

if __name__ == "__main__":
    app.run(debug=True)
