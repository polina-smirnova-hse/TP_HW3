if [ "$1" == "build_generator" ]; then
docker build -t generat ./generator
elif [ "$1" == "run_generator" ]; then
docker run --rm -v "$(pwd)/data:/app/data" generat
elif [ "$1" == "create_local_data" ]; then
python3 generator/generate.py local_data
fi