# Simple task runner
.PHONY: etl jolts cps mart clean

etl: jolts cps

jolts:
	python src/etl/jolts.py

cps:
	python src/etl/cps_published.py

mart:
	duckdb :memory: -c ".read src/sql/schema.sql" -c "COPY mart_macro TO 'data_mart/mart_macro.csv' (HEADER, DELIMITER ',');"

clean:
	rm -f data_clean/*.csv data_mart/*.csv
