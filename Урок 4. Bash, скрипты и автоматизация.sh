#Пункт 1, скрипт 1 sortFile.sh
#!/bin/bash/
echo -e "text1\n\ntext2" > sort.txt
sed '/^s/d' sort.txt | tr [:lower:] [:upper:] > sortResult.txt
#Пункт 2, скрипт 2 loginFailed.sh
#Для корректного отображения логов в реальном времени в окне консоли, используем 
#запуск скрипта "loginFailed.sh" в фоновом режиме.
./loginFailed.sh &
#!/bin/bash/
tail -f /var/log/auth.log | grep -i "failed"
#Пункт 3, скрипт 3 createFile.sh
#!/bin/bash/
for year in {2015..2020}
do
	for month in {01..12}
	do
		for day in {01..30}
		do
			for numb in {01..05}
			do
				mkdir -p ~/$year/$month
				echo Файл №$numb, создан $day.$month.$year > ~/$year/$month/$year$month$day$numb.txt
			done
		done
	done
done
#Пункт 4.
crontab -e
0 4 * * * sudo du -sm /home/* > /var/log/userProfileSize.log
