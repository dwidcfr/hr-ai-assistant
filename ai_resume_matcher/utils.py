import fitz
import docx


def extract_text_from_file(uploaded_file):
    if uploaded_file is None:
        return ""

    if uploaded_file.type == "application/pdf":
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            return "\n".join([page.get_text() for page in doc])

    elif (
        uploaded_file.type
        == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ):
        document = docx.Document(uploaded_file)
        return "\n".join([para.text for para in document.paragraphs])

    elif uploaded_file.type.startswith("text/"):
        return uploaded_file.read().decode("utf-8")

    return ""
