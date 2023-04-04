from docx.api import Document

src_file = "data/test.docx"

def open_document(src_file):
    try:
        document = Document(src_file)
    except FileNotFoundError:
        print(f"The file '{src_file}' could not be found")
    except Exception as e:
        print(f"An error occurred while trying to open {src_file}: {e}")
    else:
        print(f"Opening {src_file}")
        return document

def parse(document):
    form = ""
    for table in document.tables:
        #print("NEW TABLE")
        for row in table.rows:
            #print("|".join([cell.text for cell in row.cells]))
            form += "|".join([cell.text for cell in row.cells]) + '\n'
    return form

if __name__ == '__main__':
    doc = open_document(src_file)
    
    if doc:
        form = parse(doc)