FROM python:3.11.6-slim

# 필수 패키지 설치 (apt 패키지와 pip 설치를 함께)
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    pip install --upgrade pip && \
    pip install psycopg2-binary

# Python 버퍼링 비활성화 (로그 실시간 출력)
ENV PYTHONUNBUFFERED=1

# 작업 디렉터리 설정
WORKDIR /app

# requirements 파일 복사 및 패키지 설치
COPY requirements/ requirements/
RUN pip install -r requirements/dev.txt

# 소스 코드 복사
COPY . .

# 포트 노출
EXPOSE 8000

# 컨테이너 실행 명령어
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
