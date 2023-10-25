import fitz
import os
import PyPDF2

input_path = '230907208.pdf'
output_path = 'images'

# Create the output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

# Open the PDF file
with open(input_path, 'rb') as pdf_file:
    # Read the PDF file
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Get the total number of pages in the PDF
    num_pages = len(pdf_reader.pages)

    # Iterate through all pages
    for page_number in range(num_pages):
        # Extract text from the current page
        # page = pdf_reader.getPage(page_number)
        page = pdf_reader.pages[page_number]
        page_text = page.extract_text()

        # Save the text to a file for each page
        text_file_path = os.path.join(output_path, f'output_page_{page_number}.txt')
        with open(text_file_path, 'w', encoding='utf-8') as text_file:  # Specify 'utf-8' encoding
            text_file.write(page_text)

# Open the PDF file with fitz
pdf_doc = fitz.open(input_path)

# Iterate through all pages and save images
for page_number in range(pdf_doc.page_count):
    # Get a list of images on the current page
    page_images = pdf_doc.get_page_images(page_number)

    # Save each image to a file
    for image in page_images:
        image_xref = image[0]
        pixmap = fitz.Pixmap(pdf_doc, image_xref)
        image_file_path = os.path.join(output_path, f'page_{page_number}_image_{image_xref}.png')
        pixmap.save(image_file_path)
        pixmap = None

    # Print the number of images detected on the current page
    num_images = len(page_images)
    print(f'{num_images} images detected on page {page_number} of the PDF.')

# Close the PDF document
pdf_doc.close()
