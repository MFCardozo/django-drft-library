FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

RUN addgroup  --system django && adduser --system  --ingroup django django

RUN mkdir -p /vol/static
RUN chown -R django:django /app /vol

RUN chmod +x /app/entrypoint.sh && chown django:django /app/entrypoint.sh
USER django


ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]