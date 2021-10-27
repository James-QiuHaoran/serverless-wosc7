default:
	g++ -o memBw memBw.c
	g++ -fopenmp -o cpu cpu.cpp -lpthread -lgomp
	g++ -o l3 l3.c -lrt

clean:
	rm memBw
	rm cpu
	rm l3
