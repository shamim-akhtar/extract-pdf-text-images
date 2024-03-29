# Extract Text and Images from a PDF File
<p align='left'>
  <a href="https://www.linkedin.com/in/shamim-akhtar/">
    <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&flat-square&logo=linkedin&logoColor=white" />
  </a>
  <a href="mailto:shamim.akhtar@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?flat-square&logo=gmail&logoColor=white" />        
  </a>
  <a href="https://www.facebook.com/faramiraSG/">
    <img src="https://img.shields.io/badge/Facebook-1877F2?flat-square&logo=facebook&logoColor=white" />        
  </a>
</p>

## Code Explanation
The code is a Python script (Jupyter Notebook) that extracts text and images from a PDF file. It imports three libraries: 
* fitz, 
* os, and 
* PyPDF2. 

It then sets the input and output paths, opens the PDF file and reads it using PyPDF2, and extracts the text from the first page of the PDF. The extracted text is saved to a file in the specified output folder. The script then opens the PDF file again using fitz, gets a list of images on the first page of the PDF, saves each image to a file in the specified output folder, and prints the number of images detected on the first page of the PDF.

To use the code, you must replace the **input_path** variable with the PDF file path you want to extract text and images. You should also set the **output_path** variable to the folder where you want the output files to be saved. After running the Python script, it will extract the text and images from the PDF and save them to files in the specified output folder.

## Usage Instructions
### To use the code, follow these instructions:
1. Install the required libraries: fitz, os, and PyPDF2. You can install them using pip in your command prompt or terminal.
2. Save the code as a Python script in a folder on your computer.
3. Replace the input_path variable with the PDF file path you want to extract text and images.
4. Set the output_path variable to the folder where you want the output files to be saved.
5. Run the script using Python. You can do this by navigating to the folder where the script is saved in your command prompt or terminal and running python scriptname.py. > Replace scriptname.py with the name of the script you saved in step 2.
6. Check the output folder to verify the text and images were extracted successfully.

**Note** that the code is only designed to extract text and images from the first page of the PDF. To extract text and images from other pages, you must modify the code accordingly.
