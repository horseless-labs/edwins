from docx.api import Document

src_file = "data/test.docx"

def open_document(src_file):
    try:
        doc = Document(src_file)
    except FileNotFoundError:
        print(f"The file '{src_file}' could not be found")
    except Exception as e:
        print(f"An error occurred while trying to open {src_file}: {e}")
    else:
        print(f"Opening {src_file}")
        return doc

def extract_fields(document):
    form = ""
    for table in document.tables:
        #print("NEW TABLE")
        for row in table.rows:
            #print("|".join([cell.text for cell in row.cells]))
            ueg = "|".join([cell.text for cell in row.cells])
            if ueg.endswith("|"):
                ueg += "NA\n"
            else:
                ueg += '\n'
            form += ueg
    return form

"""
Noticing now that the extracted fields so far do not include check boxes.
TODO:
    - Add ability to extract check boxes to `extract_fields()`
    - Add a dictionary
"""
def parse_fields(field_str):
    rows = field_str.split('\n')
    print(rows)

    text_areas = []
    for row in row:
        if "|" not in row:
            text_areas.append(row)
            continue

if __name__ == '__main__':
    doc = open_document(src_file)
    
    if doc:
        form = extract_fields(doc)
        #parse_fields(form)
        print(form)