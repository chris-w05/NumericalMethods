from fpdf import FPDF

def save_script_as_pdf(input_file, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Courier", size=8)  # Use 'Courier' for monospace, set size smaller

    line_height = pdf.font_size * 1.2  # Single line spacing

    with open(input_file, "r", encoding="utf-8", errors="replace") as file:
        for line in file:
            pdf.cell(0, line_height, txt=line.rstrip(), ln=True)

    pdf.output(output_file)
    print(f"PDF created successfully at {output_file}")

# Specify your file paths
folder = "HW4/"
fileName = "HW4q1"
input_file = folder + fileName + ".py"  
output_file = folder + fileName + ".pdf"  

save_script_as_pdf(input_file, output_file)