# Docker, AWS 배포, 테스트를 위한 ToDoList

<div align="center">
<img width="340" alt="image" src="https://github.com/user-attachments/assets/d9ee9b34-8d9e-4fd8-bde2-038ebd6d946a">
<br>


</div>

> **개인 공부용 프로젝트** <br/> **개발기간: 2024.09 ~ 2024.10**



## 프로젝트 소개

사이드 프로젝트를 진행하며 단순한 구현에만 집중하다보니 테스트 및 AWS 배포 경험을 쌓기 위해 학습용 프로젝트로 진행하였습니다. 이 프로젝트를 통해 필요한 기술들을 종합적으로 실습해보면서 개발 역량을 키우는 것을 목표로 삶았습니다.

</br>

## 사용 기술 스택

| **분야**       | **기술 스택**                           |
| -------------- | --------------------------------------- |
| **백엔드**     | Django, Django Rest Framework           |
| **데이터베이스** | PostgreSQL                              |
| **To Study** | AWS, Docker, Pytest |

</br>

## 기능
 - 사용자 관리
     - 회원가입
     - 로그인
     - 로그아웃
 - Todo
     - CRUD
 - 테스트 코드
     - 더미 데이터를 이용한 API 테스트  

</br>

## **학습 내용 정리**

### **1. VPC**  
<div>
    <img src="https://github.com/user-attachments/assets/ebc61019-c04d-4d22-b3d4-50e6827685e9" width="500" />
</div>

- **역할**: 클라우드 환경에서 네트워크를 논리적으로 분리해 격리된 네트워크 제공  
- **보완점**: 애플리케이션 실행 서버 → **EC2**  
- **학습 링크**:  
    - [VPC란?](https://jongseoung.tistory.com/308)  
    - [VPC 네트워크 구성](https://jongseoung.tistory.com/309)  
    - [보안 그룹과 네트워크 ACL](https://jongseoung.tistory.com/310)  


### **2. EC2**  
<div>
    <img src="https://github.com/user-attachments/assets/f37171cb-1a59-4091-bf53-5f02b5e91e76" width="500" />
</div>

- **역할**: 가상의 서버를 제공해 애플리케이션 실행  
- **보완점**: 보안 강화 및 비용 절감 → **Bastion Host & NAT Instance**  
- **학습 링크**:  
    - [EC2란?](https://jongseoung.tistory.com/311)  
    - [EC2 인스턴스 생성 및 설정](https://jongseoung.tistory.com/312)  
    - [애플리케이션 빌드 및 배포](https://jongseoung.tistory.com/313) 
    - [EC2 사용자 데이터 재 실행](https://jongseoung.tistory.com/325) 


### **3. Bastion Host & NAT Instance**  
<div>
    <img src="https://github.com/user-attachments/assets/db3ea187-20c9-4ded-9deb-8eaf4371c49e" width="500" />
</div>

- **역할**: 외부에서 프라이빗 서브넷의 인스턴스로 접속하기 위한 보안 중계 서버  
- **보완점**: 프라이빗 서브넷은 직접적으로 API 요청을 받을 수 없음 → **로드 밸런싱, ELB 도입**  
- **학습 링크**:  
    - [Bastion Host](https://jongseoung.tistory.com/315)  
    - [NAT Instance](https://jongseoung.tistory.com/316)  


### **4. ELB (Elastic Load Balancer)**  
<div>
    <img src="https://github.com/user-attachments/assets/aa478d58-dca5-45e8-abf7-008295edc176" width="500" />
</div>

- **역할**: 들어오는 트래픽을 여러 인스턴스로 분산시켜 애플리케이션의 가용성을 높임  
- **보완점**: 트래픽 급증 대응 → **Auto Scaling Group 도입**  
- **학습 링크**:  
    - [ELB란?](https://jongseoung.tistory.com/317)  
    - [Application Load Balancer](https://jongseoung.tistory.com/318)  
    - [수평 확장](https://jongseoung.tistory.com/319)  


### **5. Auto Scaling Group (ASG)**  
<div>
    <img src="https://github.com/user-attachments/assets/33688655-e25a-4117-8019-4f168edcce82" width="500" />
</div>

- **역할**: 트래픽 변화에 따라 인스턴스 수를 자동으로 조절해 자원을 효율적으로 사용  
- **보완점**: 개별 인스턴스 데이터베이스 일관성 문제 해결, H2 데이터베이스는 인스턴스가 종료되면 데이터가 삭제됨 → **RDS 도입**  
- **학습 링크**:  
    - [ASG란?](https://jongseoung.tistory.com/320)  
    - [AMI & Launch Template](https://jongseoung.tistory.com/327)  
    - [오토 스케일링 구현](https://jongseoung.tistory.com/321)


### **6. RDS (Relational Database Service)**  
<div>
    <img src="https://github.com/user-attachments/assets/9adf246d-3401-419f-ad7c-114b8bed90ab" width="500" />
</div>

- **역할**: AWS에서 관리하는 고가용성 데이터베이스 제공  
- **보완점**: 파일 저장과 일관성 문제 해결 → **S3 도입**  
- **학습 링크**:  
    - [RDS란?](https://jongseoung.tistory.com/328)  
    - [Multi AZ 고가용성](https://jongseoung.tistory.com/331)  
    - [RDS Proxy](https://jongseoung.tistory.com/332)  
    - [인스턴스 생성 및 연결](https://jongseoung.tistory.com/326)
    - [읽기전용 데이터베이스](https://jongseoung.tistory.com/329)


### **7. S3 (Simple Storage Service)** 
<div>
    <img src="https://github.com/user-attachments/assets/d9ee9b34-8d9e-4fd8-bde2-038ebd6d946a" width="500" />
</div> 

- **역할**: 파일과 데이터를 저장하고 버전 관리 제공  
- **보완점**: 서비스 확장 → **마이크로 서비스 아키텍처 도입**  
- **학습 링크**:  
    - [S3란?](https://jongseoung.tistory.com/333)  
    - [버킷 생성 및 권한 설정](https://jongseoung.tistory.com/334)  
    - [스토리지 클래스와 Lifecycle](https://jongseoung.tistory.com/336)  
    - [CloudFront](https://jongseoung.tistory.com/337)  
    - [버전 관리](https://jongseoung.tistory.com/335)


### **8. Pytest** 
<div>
    <img src="https://github.com/user-attachments/assets/9fa3fcf6-81c6-4abd-8308-a267c1d7843a" width="500" />
</div> 

- **역할**: 
    - 애플리케이션의 품질 유지 
    - 버그 사전 예방
    - pytest-django: pytest와 django를 통합해 테스트 코드의 가독성과 확장성을 높여줌
    - factory-boy: 테스트 코드에서 사용할 객체를 쉽게 생성해주는 도구
    - Faker: 가짜 데이터, 더미데이터를 생성해주는 역할
- **학습 링크**:  
    - [Pytest](https://jongseoung.tistory.com/350)


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
