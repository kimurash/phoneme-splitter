$basename = "C0003"
$date     = "230718"

rye run python .\src\convert.py $basename $date

Copy-Item -Path ".\wav\speech.txt" -Destination ".\wav\$basename.txt"

perl .\segment_julius.pl

rye run python .\src\split.py

Remove-Item -Path ".\wav\$basename*"
