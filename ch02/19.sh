cut -f 1 popular-names.txt | sort | uniq -c | sort -rn > rank.txt
