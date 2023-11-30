$input_files = Get-ChildItem -Filter *.md
pandoc $input_files -o output.pdf