get-src: get-moses get-kytea

get-moses:
	git clone https://github.com/moses-smt/mosesdecoder

get-kytea:
	wget http://www.phontron.com/kytea/download/kytea-0.4.7.tar.gz
	tar zxvf kytea-0.4.7.tar.gz
	rm kytea-0.4.7.tar.gz
	cd kytea-0.4.7; ./configure; make; make install
