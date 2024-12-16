# Docker, AWS 배포, 테스트를 위한 ToDoList

<div align="center">
<img width="340" alt="image" src="https://github.com/user-attachments/assets/4368aa80-d65a-4c84-9a03-2c519fa583db">
<br>
실습 이미지

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fjong-seoung%2FTodoList.git&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</div>

> **개인 공부용 프로젝트** <br/> **개발기간: 2024.09 ~ 2024.10**

## 목차
[프로젝트 소개](#프로젝트-소개)

[시작 가이드](#시작-가이드)

[기술 스택](#stacks)

[주요 기능](#주요-기능)

[이론 공부(모노리식 아키텍처)](#모노리식-아키텍처)

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

## 주요 기능
 - 사용자 관리
     - 회원가입
     - 로그인
     - 로그아웃
 - Todo
     - CRUD
 - 테스트 코드
     - 더미 데이터를 이용한 API 테스트       
---

## 모노리식 아키텍처

[블로그](https://jongseoung.tistory.com/338#VPC%20-%20%EB%B3%B4%EC%95%88%20%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%20%EA%B5%AC%EC%B6%95-1)

1. VPC

    <img width="329" alt="1  vpc" src="https://github.com/user-attachments/assets/ebc61019-c04d-4d22-b3d4-50e6827685e9">
    
    <p>역할</p>
    <p> - 클라우드 환경에서 네트워크를 논리적으로 분리하여 격리된 네트워크를 제공 </p>
    <p>보완점</p>
    <p> - 애플리케이션이 실행될 서버 -> EC2</p>
2. EC2
    
    <img width="329" alt="2  ec2" src="https://github.com/user-attachments/assets/f37171cb-1a59-4091-bf53-5f02b5e91e76">
    
    <p>역할</p>
    <p> - 가상의 서버를 제공하여 애플리케이션을 실행</p>
    <p>보완점</p>
    <p> - 보안 강화 및 비용 절감 -> Bastion Host & NAT Instance</p>
3. Bastion Host   
    
    <img width="329" alt="3  bastionhost" src="https://github.com/user-attachments/assets/db3ea187-20c9-4ded-9deb-8eaf4371c49e">
    
    <p>역할</p>
    <p> - 외부에서 프라이빗 서브넷의 인스턴스로 접속하기 위한 보안 중계 서버</p>
    <p>보완점</p>
    <p> - 프라이빗 서브넷은 직접적으로 API 요청을 받을 수 없다. -> 로드 밸런싱, Elastic Load Balancer</p>
4. ELB(Elastic Load Balancer)
    
    <img width="329" alt="4  alb" src="https://github.com/user-attachments/assets/aa478d58-dca5-45e8-abf7-008295edc176">
    
    <p>역할</p>
    <p> - 들어오는 트래픽을 여러 인스턴스로 분산하여 애플리케이션의 가용성을 높임</p>
    <p>보완점</p>
    <p> - 수동으로 확장해 줘야한다 (트래픽이 언제 늘으날지 예측이 안되는데 수동 확장은 사실상 불가능) -> Auto Scailng Group</p>
5. Auto Scailng Group
    
    <img width="329" alt="5 ASG" src="https://github.com/user-attachments/assets/33688655-e25a-4117-8019-4f168edcce82">
    
    <p>역할</p>
    <p> - 트래픽 변화에 따라 인스턴스 수를 자동으로 저절하여 자원을 효율적으로 사용</p>
    <p>보완점</p>
    <p> - 데이터가 인스턴스의 개별 데이터 베이스에 저장되어 있으면 일관성이 없음</p>
    <p> - H2 데이터베이스는 인스턴스가 종료되면 데이터가 삭제됨</p>
6. RDS
    
    <img width="329" alt="6 RDS" src="https://github.com/user-attachments/assets/9adf246d-3401-419f-ad7c-114b8bed90ab">
   
    <p>역할</p>
    <p> - AWS에서 운영부분을 관리하는 RDS</p>
    <p>보완점</p>
    <p> - 파일 저장, 파일 데이터의 일관성 유지가 안됨 -> S3 도입</p>

7. S3
   
    <img width="329" alt="7  S3" src="https://github.com/user-attachments/assets/d9ee9b34-8d9e-4fd8-bde2-038ebd6d946a">
   
    <p>역할</p>
    <p> - 파일과 데이터를 저장하고 버전 관리를 제공하는 객체 스토리지 서비스</p>
    <p>보완점</p>
    <p> - 서비스가 성장함에 따라 문제가 발생할 수 있음 -> 마이크로 서비스 아키텍처로 단점을 보완</p>
---
