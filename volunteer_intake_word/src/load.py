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
        for row in table.rows:
            #ueg = "NEW TABLE\n"
            ueg = "|".join([cell.text for cell in row.cells])
            if ueg.endswith("|"):
                ueg += "NA\n"
            else:
                ueg += '\n'
            form += ueg
    return form

def extract_paragraphs(document):
    doc_length = len(document.paragraphs)
    paras = ""
    for p in range(doc_length):
        para = document.paragraphs[p]
        paras += para.text + '\n'
    return paras

"""
Noticing now that the extracted fields so far do not include check boxes.
TODO:
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

# My first way of approaching this takes the complete form and parses individual
# lines with underscores. Messy and unpythonic.
def parse_check_boxes(paragraphs):
    paragraphs = paragraphs.split('\n')
    boxes = []
    for para in paragraphs:
        if '_' in para and para.count('_') < 10:
            boxes.append(para)
    return boxes

# Reduces a list of check boxes to a small number of strings, one for each of the
# broader categories that they are found in on the volunteer intake form.
def reduce_boxes(boxes):
    selected_interests = boxes[:7]
    # Things like other_interests are not collected from checkboxes.

    oef = boxes[7:12]
    students_lives = boxes[12:19]
    class_education = boxes[19:23]
    facilities = boxes[23:32]
    clerical_advo = boxes[32:40]
    print(clerical_advo)

if __name__ == '__main__':
    doc = open_document(src_file)

    if doc:
        # Intermediate step
        paragraphs = extract_paragraphs(doc)

        # Check boxes
        boxes = parse_check_boxes(paragraphs)
        form = extract_fields(doc)
        #parse_fields(form)
        #print(form)
        #print(boxes)
        """
        for i in range(len(boxes)):
            print(f"{i}: {boxes[i]}")
        """
        reduce_boxes(boxes)