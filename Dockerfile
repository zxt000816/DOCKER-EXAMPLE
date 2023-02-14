FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y \
    git python3-opencv \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir torch==1.10.1+cu111 torchvision==0.11.2+cu111 torchaudio==0.10.1 -f https://download.pytorch.org/whl/cu111/torch_stable.html
RUN pip install --no-cache-dir jupyter
RUN pip install --no-cache-dir matplotlib 
RUN pip install --no-cache-dir numpy
RUN pip install --no-cache-dir scikit-learn
RUN pip install --no-cache-dir termcolor
RUN pip install --no-cache-dir pandas
RUN pip install --no-cache-dir plotly
RUN pip install --no-cache-dir scipy
RUN pip install --no-cache-dir seaborn


WORKDIR /app

EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
