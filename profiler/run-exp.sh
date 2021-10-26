echo "128 - 2ps" >> results.csv
for i in {1..3}
do
        ./WorkloadInvoker -c workload_configs_base64-128-2ps.json; sleep 10; ./WorkloadAnalyzer;
done

echo "128 - 4ps" >> results.csv
for i in {1..1}
do
	./WorkloadInvoker -c workload_configs_base64-128-4ps.json; sleep 10; ./WorkloadAnalyzer;
done

echo "128 - 5ps" >> results.csv
for i in {1..1}
do
        ./WorkloadInvoker -c workload_configs_base64-128-5ps.json; sleep 10; ./WorkloadAnalyzer;
done

echo "128 - 6ps" >> results.csv
for i in {1..1}
do
        ./WorkloadInvoker -c workload_configs_base64-128-6ps.json; sleep 10; ./WorkloadAnalyzer;
done

echo "256 - 2ps" >> results.csv
for i in {1..2}
do
        ./WorkloadInvoker -c workload_configs_base64-256-2ps.json; sleep 10; ./WorkloadAnalyzer;
done

echo "256 - 4ps" >> results.csv
for i in {1..1}
do
        ./WorkloadInvoker -c workload_configs_base64-256-4ps.json; sleep 10; ./WorkloadAnalyzer;
done

echo "256 - 5ps" >> results.csv
for i in {1..1}
do
        ./WorkloadInvoker -c workload_configs_base64-256-5ps.json; sleep 10; ./WorkloadAnalyzer;
done

echo "256 - 6ps" >> results.csv
for i in {1..1}
do
        ./WorkloadInvoker -c workload_configs_base64-256-6ps.json; sleep 10; ./WorkloadAnalyzer;
done
