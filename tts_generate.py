import os
import csv
import languages

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", type = str, help="File name to read", required=True)
    parser.add_argument("-l", "--language", type = str, help="Language")
    parser.add_argument("-v", "--voice", type = str, help="Voice")
    parser.add_argument("-d", "--directory", type = str, help="Directory to store the files")

    args = parser.parse_args()

    fname = args.filename
    lang = args.language
    if not lang:
        languages.list_languages()
        print()
        lang = input("Enter language: ")
    voice = args.voice
    if not voice:
        languages.list_voices(lang)
        print()
        voice = input("Enter voice: ")
    directory = args.directory
    if not directory:
        directory = lang
    
    try:
        os.makedirs(directory)
    except Exception as e:
        pass
    
    csv.register_dialect('semicolon', delimiter=';')
    with open(fname, 'r') as data:
        for line in csv.DictReader(data, dialect='semicolon'): 
            print(line[lang])
            languages.text_to_wav(voice, line[lang], directory+"/"+line["file_name"].strip())
