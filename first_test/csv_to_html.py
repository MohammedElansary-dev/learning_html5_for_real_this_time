import csv
import html
import argparse

def csv_to_html_tbody(csv_file, delimiter=',', quotechar='"'):
    """
    Convert CSV file to HTML5 <tbody> content
    :param csv_file: File object or path to CSV file
    :param delimiter: CSV field delimiter
    :param quotechar: CSV quote character
    :return: HTML string containing <tbody> content
    """
    tbody_rows = []
    
    with open(csv_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
        for row in reader:
            # Escape HTML special characters and create table cells
            cells = ''.join(f'<td>{html.escape(cell)}</td>' for cell in row)
            tbody_rows.append(f'<tr>{cells}</tr>')
    
    return f'<tbody>\n' + '\n'.join(tbody_rows) + '\n</tbody>'

def main():
    parser = argparse.ArgumentParser(description='Convert CSV to HTML5 table body')
    parser.add_argument('input', help='Input CSV file path')
    parser.add_argument('output', help='Output HTML file path')
    parser.add_argument('--delimiter', default=',', help='CSV delimiter character')
    parser.add_argument('--quotechar', default='"', help='CSV quote character')
    
    args = parser.parse_args()
    
    tbody_content = csv_to_html_tbody(
        args.input,
        delimiter=args.delimiter,
        quotechar=args.quotechar
    )
    
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(tbody_content)
    
    print(f'Successfully converted {args.input} to {args.output}')

if __name__ == '__main__':
    main()