# Docker, AWS 배포, 테스트를 위한 ToDoList

<div align="center">
<img width="329" alt="image" src="">

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fjong-seoung%2FTodoList.git&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</div>

# Docker, AWS 배포, 테스트를 위한 ToDoList

> **개인 공부용 프로젝트** <br/> **개발기간: 2024.09 ~ 2024.10**

## 프로젝트 소개

사이드 프로젝트를 진행하며 단순한 구현에만 집중하다보니 테스트 및 AWS 배포 경험을 쌓기 위해 학습용 프로젝트로 진행하였습니다. 이 프로젝트를 통해 필요한 기술들을 종합적으로 실습해보면서 개발 역량을 키우는 것을 목표로 삶았습니다.

## 시작 가이드

### Requirements

For building and running the application you need:

- [Python 3.11.6](https://www.python.org/downloads/release/python-3116/)

### Clone

```bash
$ git clone https://github.com/jong-seoung/TodoList.git
$ cd TodoList
```

### 가상환경 & 의존 파일 설치

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install psycopg2-binary
$ pip install -r requirements/dev.txt
```

#### Run
```bash
$ python manage.py runserver
```

---

## Stacks 

### Environment

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)

### Config

![python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### Development

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white)


### To Study
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=Pytest&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=AmazonWebservices&logoColor=white)

---

## 모노리식 아키텍처
1. VPC
    <img width="329" alt="VPC" src="">
    - 역할
        클라우드 환경에서 네트워크를 논리적으로 분리하여 격리된 네트워크를 제공
    - 보안점
        애플리케이션이 실행될 서버 -> EC2
2. EC2
    <img width="329" alt="EC2" src="">
    - 역할
        가상의 서버를 제공하여 애플리케이션을 실행
    - 보안점
        보안 강화 및 비용 절감 -> Bastion Host & NAT Instance
3. Bastion Host   
    <img width="329" alt="Bastion Host" src="">
    - 역할
        외부에서 프라이빗 서브넷의 인스턴스로 접속하기 위한 보안 중계 서버
    - 보안점
        프라이빗 서브넷은 직접적으로 API 요청을 받을 수 없다. -> 로드 밸런싱, Elastic Load Balancer
4. ELB(Elastic Load Balancer)
    <img width="329" alt="ELB" src="">
    - 역할
        들어오는 트래픽을 여러 인스턴스로 분산하여 애플리케이션의 가용성을 높임
    - 보안점
        수동으로 확장해 줘야한다 (트래픽이 언제 늘으날지 예측이 안되는데 수동 확장은 사실상 불가능) -> Auto Scailng Group
5. Auto Scailng Group
    <img width="329" alt="Auto Scailng Group" src="">
    - 역할
        트래픽 변화에 따라 인스턴스 수를 자동으로 저절하여 자원을 효율적으로 사용
    - 보안점
        데이터가 인스턴스의 개별 데이터 베이스에 저장되어 있으면 일관성이 없음
        H2 데이터베이스는 인스턴스가 종료되면 데이터가 삭제됨
6. RDS
    <img width="329" alt="RDS" src="">
    - 역할
    - 보안점
        파일 저장, 파일 데이터의 일관성 유지가 안됨 -> S3 도입

7. S3
    <img width="329" alt="S3" src="">
    - 역할
        파일과 데이터를 저장하고 버전 관리를 제공하는 객체 스토리지 서비스
---
