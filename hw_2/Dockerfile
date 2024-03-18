FROM python


RUN apt-get update \ 
    && apt-get install -y texlive-latex-base \
    && git clone https://github.com/olegbaryshnikov/python_course\
    && cd python_course \
    && python3 -m pip install -r requirements.txt \
    && python3 -m build ./hw_2 \
    && cp -r ./hw_2/dist/ ./hw_2/artifacts/dist/ \
    && python3 -m pip install ./hw_2/dist/latex_gen-0.0.1-py3-none-any.whl \
    && python3 -m latex_gen -i hw_2/Lenna.png -s ./hw_2/artifacts \
    && pdflatex --output-directory=./hw_2/artifacts/ ./hw_2/artifacts/latex.tex