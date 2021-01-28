#Пункт 1
ls -la /etc
ls -la /proc
ls -la /home
cat /etc/passwd
cat /etc/networks
#Пункт 2
echo Hello World > Markov_file1
echo Hello Teacher >Markov_file2
cat Markov_file1 Markov_file2 >> Markov_result
#Пункт 3
mkdir Markov
mv Markov_result ~/Markov
rm Markov_file1
rm Markov_file2
rm -R ~/Markov
#Пункт 4
ls -ld .?* | wc -l
#Пункт 5
cd /etc
ls -a | cat ?* 2> ~/err.txt
wc -l ~/err.txt
cd ~
#Пункт 6: Поэкспериментировал не знаю как в рамкх одного скрипта это отразить. 
#Если необходимы доказательства, могу предоставить скриншоты.
#Пункт 7: не совсем понял задание. Для меня было достаточно:
lsof /dev
#Пункт 8
mkdir ~/MyFoto
cd ~/MyFoto
mkdir -p ~/MyFoto/20{00..20}/{01..12}
#Пункт 9
for y in {2000..2020}
do
	for m in {01..12}
	do
		for d in {01..30}
		do 
			for n in {01..05}
			do
				echo $y$m$d$n > $y$m$d$n.txt
			done
		done
	done
done
for y in {2000..2020}
do
	for m in {01..12}
	do
		mv $y$m*.txt ~/MyFoto/$y/$m
	done
done
cd ~
rm -R ~/MyFoto
#Пункт 10 
ls -la /etc | cut -d' ' -f1 | sed -e '1,3d' | sort | uniq |wc -l