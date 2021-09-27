# Git-GitHub
Organize what i have learned git, github
git hub pull 내용 Vs code 에서 관리법 정리
1. Initial Repository click, 로컬 Repository 관리 가능하게 된다. 
2. Repository 주소 복사 후 
3. Remote setting 명령어 : git remote add origin 주소
4. remote 잘 설정되었는지 확인, git remote -v
5. commit 대상 설정 후 commit 
6. Push : git push origin master 
7. 확인 

- > 제거: ****git remote remove origin****
- > 폴더 이름 변경 : git mv [기본 폴더명] [변경할 폴더명]
- > ![image](https://user-images.githubusercontent.com/63999666/134844430-0523f302-3643-4642-8cd1-35f34909a4f2.png)

**- > 만약 **error: failed to push some refs to 이라는 에러가 발생한다면****, 
- > [원인] 이는 원격저장소(github)에 내 로컬(내컴퓨터)에는 없는 파일이 있을 때 내 파일을 push 할 면 발생하는 오류이다.
이럴땐 원격저장소에서 내 로컬에 저장하지 않은 파일을 pull한 후 원격저장소에 다시 push를 해야한다.
- [명령]  git pull {원격저장소별칭 보통 origin이라고 함} master
- [명령] git push {원격저장소 별칭 보통 origin} master


**- > **만약 fatal: not a git repository(or any of the parent directorties):.git 이라는 에러가 발생한다면,****
- > [원인] 현재 폴더에 git 에 대한 정보를 담은 파일이 없기 때문에 발생하는 에러.
- > 해결책 git init 으로 git 복원

# Git-Hub -git 협업 명령어(복귀)
## Feature Branch WorkFlow
Feature Branch Workflow의 핵심 컨셉은 기능별 브랜치를 만들어서 작업하는 것이다. 
다수의 팀 구성원이 메인 코드 베이스(master)를 중심으로 해서 안전하게 새로운 기능을 개발 할 수 있다. 
-> 소규모 인원의 프로젝트 적합 

###  중앙 원격 저장소, 자신의 원격 저장소, 로컬 저장소의 개념 
- 중앙 원격 저장소
여러 명이 같은 프로젝틀을 관리하는 데 사용하는 그룹 계정의 중립된 원격 저장소 
  Organiziaion을 만드는 방법은 github페이지 오른쪽 위에 있는 

- 자신의 원격 저장소
romote repository라고 부른다 
파일이 github 전용 서버에서 관리되는 원격 저장소 

- 로컬 저장소
local reposiotory 라고 불린다
내 PC에 파일이 저장되는 개인 전용 저장소, 지역 저장소 

### 명령어 

git clone [중앙 URL] -> local

fetch와 pull의 차이 
fetch : 원격 저장소의 데이터를 로컬에 가져오기만 하기 
pull: 원격 저장소의 내용을 가져와 자동으로 병합 작업을 실행 
즉, 단순히 원격 저장소의 내용을 확인만 하고 로컬 데이터와 병합은 하고 싶지 않은 경우
fetch 


git checkout -b [branch name]

위의 명령어는 아래의 두 명령어를 합한 것
git branch [branch name]
git checkout [branch name]

git commit -a -m "Write commit message"

위의 명령어는 아래의 두 명령어를 합한 것
git add . # 변경된 모든 파일을 스테이징 영역에 추가
git add [some-file] # 스테이징 영역에 some-file 추가
git commit -m "Write commit message" # local 작업폴더에 history 하나를 쌓는 것


- 커밋을 완료했다면, 내가 작업한 내용을 포함한 브랜치(feature/login branch)를 중앙 원격 저장소에 올린다.
이는 로컬 저장소의 백업 역할을 할 뿐만 아니라, 다른 팀 구성원들이 나의 작업 내용과 진도를 확인할 수도 있어 좋은 습관이라 할 수 있다.

- u 옵션: 새로운 기능 브랜치와 동일한 이름으로


// 로컬의 기능 브랜치를 중앙 원격 저장소 (origin)에 올린다.
git push -u origin feature/login branch

// -u 옵션으로 한 번 연결한 후에는 옵션 없이 아래의 명령만으로 기능 브랜치를 올릴 수 있다.
git push -origin feature/login branch

+풀 리퀘스트(Pull requests)란?
기능 개발을 끝내고 master에 바로 병합(merge)하는 것이 아니라, 브랜치를 중앙 원격 저장소에 올리고 master에 병합(merge)해달라고 요청하는 것

중앙 원격 저장소와 자신의 로컬 저장소를 동기화하기 위해 로컬 저장소의 branch를 master branch로 이동한다.
// 로컬 저장소의 branch를 master branch로 이동
$ git checkout master

중앙 원격 저장소의 코드 베이스에 새로운 커밋이 있다면 다음과 같이 가져온다.
중앙 원격 저장소(origin)의 메인 코드 베이스가 변경되었으므로, 프로젝트 참여하는 모든 개발자가 자신의 로컬 저장소를 동기화해서 최신 상태로 만들어야 한다.

git pull origin master


참고자료: https://gmlwjd9405.github.io/2017/10/27/how-to-collaborate-on-GitHub-1.html



