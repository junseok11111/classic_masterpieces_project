### 1. 목표 서비스 및 사용 기술

- 목표
    - TMDB API를 사용한 horror 장르의 영화 데이터 수집 및 영화 데이터 기반 추천 서비스 구현
    - 유저간 소통 할 수 있는 커뮤니티 기능 구현
    - 평점순, 장르별 추천 알고리즘 구현
    - 서비스 관리 및 유지 보수
- 사용 기술
    - python
    - Django 3.2.18
    - Vue 2

---

### 2. 팀원 정보 및 업무 분담

- 공통
    - 영화 추천 사이트 서비스의 전반적인 구성

- 분업
    - 강경인
        - front-end (Vue)
        - 서비스 디자인
        - 발표 자료 제작 및 발표
    - 김준석
        - back-end (Django)
        - 장르별 추천 알고리즘 구현

---

### 3. ERD 모델링

![ERD.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d4478925-6a8c-4d91-8f4e-33896dbdb2c8/ERD.png)

---

### 4. 영화 추천 알고리즘 및 서비스 주요 기능

- 영화 추천 알고리즘
    - 평점순, 장르별 추천 방식이 구현되어 있다.
    - 평점순 추천 방식의 경우, DB에 저장된 모든 영화 데이터에 대하여 vote_count가 5000이상인 영화에 대해 vote_average를 내림차순으로 정렬하여 상위 18개의 영화를 반환한다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1496fc6b-e575-4fae-b298-841a36502608/Untitled.png)
    
    ![Image Pasted at 2023-5-26 00-15.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f749e1d4-6a4d-4ced-9a52-3d4de227c862/Image_Pasted_at_2023-5-26_00-15.png)
    
    - 장르별 추천 방식의 경우, 공포 영화가 가지고 있는 여러 장르 태그에 대해 Thriller, Mystery, Action, SF 4가지의 각 장르에 대하여 각각 추천
    - 해당하는 장르의 번호를 포함하는 영화데이터를 필터링한 후, 평점순으로 내림차순 정렬하여 제공
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/088918df-512c-41c6-92f0-9977a5b84192/Untitled.png)
    
    ![Image Pasted at 2023-5-26 00-21.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ca5bde79-a4be-41c3-a962-e9c0a0995a88/Image_Pasted_at_2023-5-26_00-21.png)
    
    - 공포/스릴러의 경우, 해당 장르만 가진 영화에 대해서만 추천
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d0ca2e10-7d2d-4be0-ac0f-17cd5d0dc9de/Untitled.png)
    
- 영화 주요 기능
    1. 영화 정보 페이지
        - 각 영화에 대한 예고편, 포스터, 제목, 평점, 개요, 출연진에 대한 정보 제공
            - 예고편은 Youtube API룰 사용하여 재생
        - 사용자가 작성 가능한 영화 한줄평
    
    1. 영화 커뮤니티 페이지 구현
        - 상단바의 Article을 클릭하면 영화 커뮤니티로 이동
        - 영화 리뷰 & 공포 사연을 자유롭게 올릴 수 있는 커뮤니티
        - 각 게시글 목록에는 제목, 작성자, 작성시간 정보가 제공
            
            ![Image Pasted at 2023-5-26 00-23.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/323143bb-ddf7-4911-9c11-060c8e83c9f7/Image_Pasted_at_2023-5-26_00-23.png)
            
        - 게시글에 대한 댓글 작성 가능
        
    2. 게임 기능 구현
        1. 상단바의 Game을 클릭하면 게임으로 이동
        2. 랜덤하게 보이는 배우 이미지에 대하여, 귀신 역할을 했는지 true,false를 선택하는 게임
        3. 게임이 실패할 경우 강제로 404 페이지로 이동 
        4. 이 때, 마우스를 따라다니는 작은 유령 생성

---

### 5. 후기

- 강경인
    
    이번에 프론트엔드 부분을 맡아서 해보았는데 생각 보다. 교과서를 통해서 배운것을 사용하는 데
    어려움이 많았다. 그리고 일일이 디자인 하는 것과 디자인을 컨셉에 맞게 구상하는 것이 생각보다 큰일 임을 느낄 수 있었다.
    목표치의 달성에는 어려움이 있었으나, 앞으로 어떠한 것을 준비해야할 지 공부 해볼 수 있었다.
    
- 김준석
    - 프로젝트를 처음 진행하면서, 제대로 알지 못했던 것들에 대한 구분이 명확해졌던 것 같습니다. 모르는 부분은 다시 공부하고 알았던 부분은 좀 더 응용해가면서 프로젝트를 해나가다 보니 프로젝트 하기 전보다실력이 상승한 것 같습니다.