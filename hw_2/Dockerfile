FROM python

RUN apt-get update\ 
    && apt-get install texlive-latex-base\
    && cd python_course\
    && python3 -m build ./hw_2/latex_gen || exit\
    && python3 -m pip install ./hw_2/latex_gen/dist/latex_gen-0.0.1-py3-none-any.whl\
    && python3 -m latex-gen -i hw_2/Lenna.png -s ./hw_2/artifacts  \
    && pdflatex --output-directory=/python_course/hw_2/artifacts/ /python_course/hw_2/artifacts/latex.tex