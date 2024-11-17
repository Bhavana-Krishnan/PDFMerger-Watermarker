# PDF Merger and Watermarker

This project provides tools for working with PDFs:
1. **PDF Merger**: Combines multiple PDF files into one consolidated PDF.
2. **PDF Watermarker**: Applies a watermark to one or more PDF files.

---

## Features

- **PDF Merger**:
  - Combines multiple PDFs in the order specified.
  - Outputs a single file named `super.pdf`.

- **PDF Watermarker**:
  - Applies a watermark to all pages of the input PDFs.
  - Outputs a new watermarked file for each input file.

---

## Requirements

- **Python**: Version 3.8 or higher.
- **PyPDF2**: Version 3.0.1 or higher. Install using pip:
  ```bash
  pip install PyPDF2
  ```

---

## File Structure

```
pdfmerger_watermarker/
│
├── pdf_merger.py         # Script for merging PDFs
├── watermark.py          # Script for adding watermarks to PDFs
├── README.md             # Project documentation
├── example_output/       # Directory for storing example outputs
│   ├── super.pdf             # Example merged PDF (output of pdf_merger.py)
│   └── super_watermarked_output.pdf  # Example watermarked PDF
├── dummy.pdf             # Example input file
├── tilted.pdf            # Example input file
├── twopager.pdf          # Example input file
├── water.pdf             # Watermark file (single-page PDF)

```

---

## Usage

### 1. **PDF Merger**

#### Command:
```bash
python .\pdf_merger.py <pdf1> <pdf2> <pdf3> ...
```

#### Example:
```bash
python .\pdf_merger.py .\dummy.pdf .\twopager.pdf .\tilted.pdf
```

#### Output:
- A merged PDF named `super.pdf` is created in the current directory.

#### Explanation:
- The input PDFs `dummy.pdf`, `twopager.pdf`, and `tilted.pdf` are merged in the order specified.
- The merged PDF is saved as `super.pdf`.

---

### 2. **PDF Watermarker**

#### Command:
```bash
python .\watermark.py <watermark.pdf> <input1.pdf> <input2.pdf> ...
```

#### Example:
```bash
python .\watermark.py .\water.pdf .\super.pdf
```

#### Output:
- A watermarked PDF named `super_watermarked_output.pdf` is created in the current directory.

#### Explanation:
- The watermark file `water.pdf` is applied to all pages of `super.pdf`.
- The output file is saved with `_watermarked_output` appended to the original file name.

---

## Example Workflow

1. **Merge PDFs**:
   - Run the following command:
     ```bash
     python .\pdf_merger.py .\dummy.pdf .\twopager.pdf .\tilted.pdf
     ```
   - Output: A file named `super.pdf` containing all the input PDFs in order.

2. **Apply Watermark**:
   - Run the following command:
     ```bash
     python .\watermark.py .\water.pdf .\super.pdf
     ```
   - Output: A watermarked version of `super.pdf`, saved as `super_watermarked_output.pdf`.

---

## Example Output Directory

The `example_output` directory contains:
- `super.pdf`: Merged PDF from the example.
- `super_watermarked_output.pdf`: Watermarked version of `super.pdf`.

---

## Notes

- **Watermark File**: Ensure the watermark file (`water.pdf`) is a single-page PDF.
- **Output Naming**: Watermarked PDFs will have `_watermarked_output` added to their original name.
- **Compatibility**: The scripts are tested with **Python 3.8+** and **PyPDF2 3.0.1**. Older versions may not work correctly.
---

## Contact

For questions or suggestions, feel free to open an issue in the repository.

--- 
