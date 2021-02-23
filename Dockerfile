FROM python
ADD . /Python
RUN pip install bs4
RUN pip install requests
RUN pip install matplotlib
CMD ["python3", "iplscores.py"]
