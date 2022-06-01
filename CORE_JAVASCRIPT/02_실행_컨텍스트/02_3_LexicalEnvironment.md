# environmentRecord와 호이스팅
## environmentRecord
* 현재 컨텍스트와 관련된 코드의 식별자 정보들이 저장
    * 식별자
    * 컨텍스트를 구성하는 함수에 지정된 매개변수 식별자
    * 선언한 함수가 있을 경우, 그 함수 자체
    * var로 선언된 변수의 식별자
    * ...등
* 컨텍스트 내부 전체를 처음부터 끝까지 쭉 훑어나가며 순서대로 수집
* 따라서 코드가 실행되기 전에 이미 환경에 속한 코드의 변수명을 모두 알고 있다. => **호이스팅**이 발생하는 이유

## 호이스팅
* `자바스크립트 엔진은 식별자를 최상단으로 끌어올려 놓은 다음실제 코드를 실행한다.`라는 개념
* 변수 정보를 수집하는 과정을 이해하기 쉬운 방법으로 대체한 가상의 개념

### 호이스팅 규칙
**선언한 변수명만 끌어올리고 할당 과정은 원래 자리에 그대로 남겨둠**

예제1. 매개변수와 변수에 대한 호이스팅

아래 콘솔 결과를 예측하시오.
```javascript
function a() {
    var x = 1;
    console.log(x);
    var x;
    console.log(x);
    var x = 2;
    console.log(x);
}
```

-> 호이스팅을 마친 경우
```javascript
function a() {
    var x;
    var x;
    var x;

    x = 1;
    console.log(x);
    console.log(x);
    x = 2;
    console.log(x);
}
```

=> 콘솔 출력 : 1 > 1 > 2

예제2. 함수 선언의 호이스팅
: **함수 선언문은 선언문 전체(선언 + 할당)를 끌어올린다.**

아래 콘솔 결과를 예측하시오.
```javascript
function a() {
    console.log(b);
    var b = 'bbb';
    console.log(b);
    function b () { }
    console.log(b);
}
a();
```

-> 호이스팅을 마친 경우
```javascript
function a() {
    var b;
    function b() {} // 함수 선언은 전체를 끌어올립니다!!

    console.log(b);
    b = 'bbb';
    console.log(b);
    console.log(b);
}
a();
```

=> 콘솔 출력 : b함수 > 'bbb' > 'bbb'

### 함수 선언문과 함수 표현식
<table>
    <tr>
        <th></th>
        <th>함수 선언문</th>
        <th>함수 표현식</th>
    </tr>
    <tr>
        <td>정의</td>
        <td>function 정의부만 존재하고 별도의 할당 명령이 없는 것</td>
        <td>
            정의한 function을 별도의 변수에 할당하는 것
            <ul>
                <li>기명 함수 표현식 : 함수명을 정의한 함수 표현식</li>
                <li>익명 함수 표현식 : 함수명을 정의하지 않은 함수 표현식</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><b>호이스팅</b></td>
        <td>전체를 호이스팅</td>
        <td>변수 선언부만 호이스팅</td>
    </tr>
</table>

문법
```javascript
function a() {...}  // 함수 선언문. 함수명 a가 변수명
a();

var b = function () {...} // 익명 함수 표현식. 변수명 b가 함수명
b();

var c = function d () {...} // 기명 함수 표현식. 변수명은 c, 함수명은 d
c();
d();    // 에러!
```

호이스팅 예제
```javascript
console.log(sum(1, 2));
console.log(multiply(3, 4));

function sum(a, b) {    // 함수 선언문
    return a + b;
}

var multiply = function (a, b) {    // 함수 표현식
    return a * b;
}
```

-> 호이스팅을 마친 경우
```javascript
function sum(a, b) {    // 함수 선언문
    return a + b;
}
var multiply;

console.log(sum(1, 2));
console.log(multiply(3, 4));

multiply = function (a, b) {    // 함수 표현식
    return a * b;
}
```

=> 콘솔 출력 : 3, multiply is not a function

=> `선언한 후에 호출할 수 있다(함수 표현식)`라는 생각으로 코딩하는 것이 에러를 덜 발생시키는 코딩 습관이다.

* 중복 선언시 함수 선언문을 사용하면 같은 유효범위 내에서 맨마지막에 선언된 함수만 사용되기 때문에 이를 인지하고 있지않으면 에러를 일으킬 수 있다.

# 스코프, 스코프 체인, outerEnvironmentReference

## 스코프 : 식별자(변수)에 대한 유효 범위
* A의 외부에서 선언한 변수는 A의 외부 + A의 내부에서도 접근이 가능하지만, A의 내부에서 선언한 변수는 오직 A의 내부에서만 접근 할 수 있다.
* **ES5**까지의 자바스크립트는 **오직 함수**에 의해서만 스코프 생성 가능

## 스코프 체인 : 스코프를 안에서부터 바깥으로 차례로 검색해 나가는 것
LexicalEnvironment > outerEnvironmentReference를 사용

생성
* outerEnvironmentReference는 **현재 호출된 함수가 선언될 당시의 LexicalEnvironment를 참조**한다.
  * 선언 당시 : 콜 스택 상에서 어떤 실행 컨텍스트가 활성화된 상태
  * 연결 리스트 형태를 띔

* 예를 들어 A 함수 내부에 B 함수를 선언하는 경우
  * B 함수의 LexicalEnvironment > outerEnvironmentReference는 A 함수의 LexicalEnvironment를 참조
  * A 함수의 LexicalEnvironment > outerEnvironmentReference는 전역 컨텍스트의 LexicalEnvironment를 참조

식별자(변수) 찾기 : 여러 스코프에서 동일한 식별자를 선언한 경우
* **스코프 체인 상에서 가장 먼저 발견된 식별자**에만 접근 가능

## 전역변수와 지역변수
* 전역 변수 : 전역 스코프에서 선언한 변수
* 지역 변수 : 함수 내부에서 선언한 변수

코드의 안정성을 위해 가급적 전역변수 사용을 최소화해야한다.
