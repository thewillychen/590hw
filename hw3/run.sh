#!/bin/bash

echo "ASCII COMPRESS"
./ascii_compress < input_tiny_original.txt > ascii_tiny.ascii
./ascii_compress < input_small_original.txt > ascii_small.ascii
./ascii_compress < input_large_original.txt > ascii_large.ascii

echo "DIFF: "
diff ascii_tiny.ascii input_tiny.ascii
diff ascii_small.ascii input_small.ascii
diff ascii_large.ascii input_large.ascii
echo "Done"

echo "COMPRESS"
./compress < input_tiny_original.txt > tiny.comp
./compress < input_small_original.txt > small.comp
./compress < input_large_original.txt > large.comp

echo "DIFF: "
diff tiny.comp input_tiny.comp
diff small.comp input_small.comp
diff large.comp input_large.comp
echo "Done"

echo "ASCII DECOMPRESS"
./ascii_decompress < input_tiny.ascii > ascii_tiny.txt
./ascii_decompress < input_small.ascii > ascii_small.txt
./ascii_decompress < input_large.ascii > ascii_large.txt

echo "DIFF: "
diff ascii_tiny.txt input_tiny_original.txt 
diff ascii_small.txt input_small_original.txt 
diff ascii_large.txt input_large_original.txt
echo "Done"

echo "DECOMPRESS"
./decompress < input_tiny.comp > tiny.txt
./decompress < input_small.comp > small.txt
./decompress < input_large.comp > large.txt

echo "DIFF: "
diff input_tiny_original.txt tiny.txt
diff input_small_original.txt small.txt
diff input_large_original.txt large.txt
echo "Done"
