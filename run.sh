if [ "$1" == "build_generator" ]; then
docker build -t generat ./generator
elif [ "$1" == "run_generator" ]; then
docker run --rm -v "$(pwd)"/data:/app/data generat
elif [ "$1" == "create_local_data" ]; then
python3 generator/generate.py local_data
elif [ "$1" == "build_reporter" ]; then
docker build -t reporter ./reporter
elif [ "$1" == "run_reporter" ]; then
docker run --rm -v "$(pwd)"/data:/data reporter
elif [ "$1" == "structure" ]; then
ls -R .
elif [ "$1" == "clear_data" ]; then
find data -name "*.csv" -delete
find data -name "*.html" -delete
elif [ "$1" == "inside_generator" ]; then
docker run -it --entrypoint bash generat
ls -la /app/data
fi