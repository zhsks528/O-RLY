# O-RLY
## branch

### 1. branch 만들기

**브랜치의 목록을 볼 때**

git branch![](F:\바탕화면\1-1.PNG)

**브랜치를 생성할 때**

git branch "새로운 브랜치 이름"

**브랜치를 전환(체크아웃)할 때**

git checkout "전환하려는 브랜치 이름"

**브랜치를 삭제할 때**

git branch -d

**병합하지 않은 브랜치를 강제 삭제할 때**

git branch -D

**브랜치를 생성하고 전환까지 할 때**

git checkout -b "생성하고 전환할 브랜치 이름"



### 2. branch 정보확인

**브랜치 간에 비교할 때**

git log "비교할 브랜치 명 1"..."비교할 브랜치 명 2"

**브랜치 간의 코드를 비교 할 때**

git diff "비교할 브랜치 명 1"..."비교할 브랜치 명 2"



**로그에 모든 브랜치를 표시하고, 그래프로 표현하고, 브랜치명을 표시할 때**

git log --branches --graph --decorate![](F:\바탕화면\branch.PNG)



**로그에 모든 브랜치를 표시하고, 그래프로 표현하고, 브랜치 명을 표시하고, 한줄로 표시할 때**

git log --branches --graph --decorate --oneline![](F:\바탕화면\3.PNG)



### 3. branch병합

