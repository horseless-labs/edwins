from docx.api import Document

src_file = "data/test.docx"
document = Document(src_file)

form = ""
for table in document.tables:
    #print("NEW TABLE")
    for row in table.rows:
        #print("|".join([cell.text for cell in row.cells]))
        form += "|".join([cell.text for cell in row.cells]) + '\n'
print(form)