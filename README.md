# 객체지향프로그래밍(Object Oriented Programing, OOP)
<!--
## (4학년) 중기청 200만원 장학금 지원 및 취업지원사업 (참여신청중! 선착순!)
> * https://github.com/JNUAca/go
> * 참여신청: https://forms.gle/qnfsxRzCAfwAG4gi8
>

## 우리는 왜 대학에 가는가.
* https://www.youtube.com/watch?v=nttlAfVQT6w&t=367s

## 취업 및 행사정보: 바울랩 카카오 오픈 단톡방2
* https://open.kakao.com/o/gKG3e0sb

## 온라인 강의

* 2장 OOP를 공부하는 이유
> (2장_1) https://youtu.be/sDPNKiHSAMc <br/>
> (2장_2) https://youtu.be/0b7wbUk7-lE <br/>

* 3장 추상화에서 객체지향 프로그래밍까지
> (3장_1) https://youtu.be/iadue3RQ8Ak <br/>
> (3장_2) https://youtu.be/y_MmWnunqy0 <br/>

* 4장 OOP에 익숙해지기 
> (4장_1) https://youtu.be/B7fdoV0zGiI <br/>
> (4장_2) https://youtu.be/6lOMhJ00B9o <br/>
> (4장_3) https://youtu.be/Cak8y8_biAg <br/>

* 5장 상속으로 코드 재사용하기
> (5장_1) https://youtu.be/uHc7b1w1sVk <br/>
> (5장_2) https://youtu.be/MaHqYJlMCAM <br/>
> (5장_3) https://youtu.be/jdl7XliObFU <br/>

* 6장 응용 프레임워크와 가상 함수의 만남
> (6장_1) https://youtu.be/2HZbu-kT5yc <br/>
> (6장_2) https://youtu.be/UeQmaqZC5Cc <br/> 
> (6장_3) https://youtu.be/0vyq1WQGJ-k <br/>
> (6장_4) https://youtu.be/o7UY5CuANaw <br/>
> (6장_5) https://youtu.be/CjVQ87VHlpc <br/>
> (6장_6) https://youtu.be/WTZGc9dmpsM <br/>

* 7장 레퍼런스와 포인터, 그리고 함수 호출 방법
> (7장_1) https://youtu.be/dLNcdIq1_Ok <br/>
> (7장_2) https://youtu.be/HANwstfJd2M <br/>
> (7장_3) https://youtu.be/l3y4buQPM8Y <br/>

* 8장 멤버 함수 자세히 살펴보기
> (8장_1) https://youtu.be/uYmmlP-OL5Y <br/>
> (8장_2) https://youtu.be/cuq0C4uSXnk <br/>
> (8장_3) https://youtu.be/tex5K4PkUrg <br/>
> (8장_4) https://youtu.be/tU_duXcDN04 <br/>
> (8장_5) https://youtu.be/HKagXTm_2kU <br/>
> (8장_6) https://youtu.be/SGFIcuDMpBU <br/>

* 9장 템플릿과 가상 함수 자세히 살펴보기
> (9장_1) https://youtu.be/gQT1XTxd-vU <br/>
> (9장_2) https://youtu.be/hZKtAIAOzIs <br/>
> (9장_3) https://youtu.be/8DV1SP6JA9I <br/>

* 10장 예외처리
> (10장_1) https://youtu.be/boX-lCOM_tk <br/>
> (10장_2) https://youtu.be/dms33rwmQlw <br/>

* 1장 몰라도 일단 짜보는 객체지향 프로그램
> (1장_1) https://youtu.be/Uewy8P4o5Wg <br/>
> (1장_2) https://youtu.be/ofAqCkBshIs <br/>
> (1장_3) https://youtu.be/Iya407K-tBs <br/>
> (1장_4) https://youtu.be/tzFWGwbYUjI <br/>
> (1장_5) https://youtu.be/D5Ltnjtrtuc <br/>
> (1장_6) https://youtu.be/xBqH3VBcuf4 <br/>
> (1장_7) https://youtu.be/iAnqPTwaH7g <br/>
> (1장_8) https://youtu.be/CfA1NQojdq8 <br/>

* 11장 객체지향 프로그래밍 실전 연습과 UML 모델링
> (11장_1) https://youtu.be/p66_72jO2l8 <br/>
> (11장_1) https://youtu.be/mQ9_YXd46-I <br/>
> (11장_1) https://youtu.be/NxJkwIo6OjY <br/>
> (11장_1) https://youtu.be/3fY4jayQi3Y <br/>
> (11장_1) https://youtu.be/DxeFsakotc0 <br/>
> (11장_1) https://youtu.be/fRt3dsiEAZ4 <br/>
> (11장_1) https://youtu.be/9RTShBX3k1U <br/>

## 머신러닝으로 배우는 응용 프레임워크 
> (성별 인식 코드) https://www.kaggle.com/yungbyun/female-male-classification-ml-simple/edit/run/30600474 <br/>
> (붓꽃 인식) https://www.kaggle.com/ash316/ml-from-scratch-with-iris <br/>

```python
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def who_are_you(self):
        pass

class Derived(Base):
    def who_are_you(self):
        print("I am Derived")

gildong = Derived()
gildong.who_are_you()

