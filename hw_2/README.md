
Use as package:
```
python3 -m latex_gen -i ./hw_2/Lenna.png -s ./hw_2/artifacts
pdflatex --output-directory=./hw_2/artifacts/ ./hw_2/artifacts/latex.tex
```

Run as Docker container:
```
cd python_course\hw_2
docker build --tag="my_docker_image" .
docker run my_docker_image
```