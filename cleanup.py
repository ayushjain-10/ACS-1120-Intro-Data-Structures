import re
import argparse

def cleanup(text):
    # Remove unwanted punctuation
    text = re.sub(r'[_*]+', '', text)

    # Remove "JP" and "DM" and "NP"
    text = re.sub(r'JP', '', text)
    text = re.sub(r'DM', '', text)
    text = re.sub(r'NP', '', text)
    text = re.sub(r'IM', '', text)
    text = re.sub(r'Q3', '', text)
    text = re.sub(r'AM', '', text)
    text = re.sub(r'RB', '', text)
    text = re.sub(r'youtube', '', text)
    text = re.sub(r'Youtube', '', text)
    

    # Remove colon
    text = re.sub(r':', '', text)
    
    # Convert HTML character codes to ASCII
    text = re.sub(r'&#[0-9]+;', lambda match: chr(int(match.group(0)[2:-1])), text)
    
    # Normalize punctuation
    text = re.sub(r'[‘’“”]', "'", text)
    text = re.sub(r'[“”]', '"', text)
    
    return text

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str, help='Input file path')
    parser.add_argument('--output_file', '-o', type=str, help='Output file path', default=None)
    args = parser.parse_args()
    
    # Read input file
    with open(args.input_file, 'r') as f:
        text = f.read()
    
    # Clean up text
    text = cleanup(text)
    
    # Write output file
    if args.output_file is not None:
        with open(args.output_file, 'w') as f:
            f.write(text)
    else:
        print(text)
