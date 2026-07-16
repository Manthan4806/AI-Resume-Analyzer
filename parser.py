import fitz

def extract_text(uploaded_file):
    uploaded_file.seek(0)  # Reset file pointer

    pdf_bytes = uploaded_file.read()

    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    text = ""

    for page in doc:
        page_text = page.get_text("text")
        text += page_text + "\n"

    doc.close()

    return text.strip()