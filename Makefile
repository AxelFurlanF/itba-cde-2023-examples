init:
	composer-dev create \
	--from-image-version composer-2.4.0-airflow-2.4.3 --dags-path dags \
	itba-dev

start:
	composer-dev start itba-dev

stop:
	composer-dev stop itba-dev
