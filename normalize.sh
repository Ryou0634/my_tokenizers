#!/bin/bash

file=$1
ln=$2
echo "file: "${file}", -l: "${ln}

# 1) Remove non-printing characters
perl mosesdecoder/scripts/tokenizer/remove-non-printing-char.perl < ${file} > ${file}.sed.uni
echo "remove-non-printing-char.perl done"

# 3) Replace unicode punctuations
#perl ../mosesdecoder/scripts/tokenizer/replace-unicode-punctuation.perl < ${file}.sed > ${file}.sed.uni
#echo "replace-unicode-punctuation.perl done"

# 4) Normalize punctuations
perl mosesdecoder/scripts/tokenizer/normalize-punctuation.perl -l ${ln} < ${file}.sed.uni > ${file}.sed.uni.norm
echo "normalize-punctuation.perl done"

# 5-1) Escape special characters
# perl ../mosesdecoder/scripts/tokenizer/escape-special-chars.perl < ${file}.sed.uni.norm > ${file}.sed.uni.norm.esc
# echo "escape-special-chars.perl done"
# 5-2)
perl mosesdecoder/scripts/tokenizer/deescape-special-chars.perl < ${file}.sed.uni.norm > ${file}.sed.uni.norm.desc
echo "descape-special-chars.perl done"

# 5) Replace the other characters
cat ${file}.sed.uni.norm.desc | \
    sed -e 's/ampamp;/\&/g' | \
    sed -e 's/\&#160;//g' | \
    sed -e 's/amp#160;//g' | \
    sed -e 's/\&nbsp;//g' | \
    sed -e 's/ampnbsp;//g' | \
    sed -e 's/\&#45;/\-/g' | \
    sed -e 's/amp#45;/\-/g' | \
    sed -e 's/\&quot;/\"/g' | \
    sed -e 's/ampquot;/\"/g' | \
    sed -e 's/ //g' | \
    sed -e 's/�//g' | \
    sed -e 's/ ?$/?/g' | \
    sed -e 's/. ?$/./g' | \
    sed -e "s/\\\u0027/\'/g" | \
    sed -e "s/\\\//g" | \
    sed -e "s/googletag.cmd.push (function () { googletag.display ('Mpu'); });//g" > ${file}.sed.uni.norm.desc.rep
echo "Replace html reps done"

#rm ${file}.sed
rm ${file}.sed.uni
rm ${file}.sed.uni.norm
rm ${file}.sed.uni.norm.desc
mv ${file}.sed.uni.norm.desc.rep ${file}.normalized


# Option: Count the word freq
# cat ${file} | gawk -F " " '{for(i=1;i<=NF;i++){count[$i]++;}};END{for(i in count){print count[i] "\t" i}}' | sort -n -r -k 1,2 | less
