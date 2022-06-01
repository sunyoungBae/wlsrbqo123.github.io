this는 함수를 호출할 때 결정됩니다.

# 전역 공간에서의 this : 전역 객체
런타임 환경에 따라 전역 객체가 다릅니다.
* 브라우저 환경 : `window`
* Node.js 환경 : `global`

> 전역변수를 선언하면 JS 엔진은 이를 전역객체의 프로퍼티로 할당한다.

# 메서드로서 호출할 때 그 메서드 내부에서의 this
## 함수 vs 메서드
* 함수 : 그 자체로 독립적인 기능을 수행
* 메서드 : 자신을 호출한 대상 객체에 관한 동작을 수행

> JS는 상황별로 this 키워드에 다른 값을 부여하게 함으로써 이를 구현했습니다.

```javascript
var func = function(x) {
    console.log(this, x);   // Window { ... } 1
};
func(1);

var obj = {
    methos: func
};
obj.method(2)   // { method: f } 2
obj['method'](2)   // { method: f } 2 // 대괄호 표기법도 동일
```

함수/메서드로서 호출 구분 방법: 함수 앞에 점 여부로 구분
* 함수로서 호출 : 함수 호출시 함수 이름 앞에 객체가 명시되어 있지 않은 경우
* 메서드로서 호출 : 함수 호출시 함수 이름 앞에 객체가 명시되어 있는 경우

## 메서드 내부에서의 this
this : 호출한 주체에 대한 정보
* 호출 주체는 함수명 앞의 객체
  * 점 표기법의 경우 마지막 점 앞에 명시된 객체

```javascript
var obj = {
    methodA: function() {console.log(this);},
    inner: {
        methodB: function() {console.log(this);}
    }
};
obj.methodA(); // { methodA: f, inner: {...} }

obj.inner.methodB();  // { methodB: f }
```

# 함수로서 호출할 때 그 함수 내부에서의 this

## 함수 내부에서의 this : 전역 객체
* 함수로서 호출할 경우 this가 지정되지 않습니다.
* 2장에서 실행 컨텍스트를 활성화할 당시에 this가 지정되지 않는 경우 this는 전역 객체를 바라본다고 했씁니다.

## 메서드의 내부함수에서의 this
함수를 실행하는 당시의 주변 환경은 중요하지 않고, 오직 **해당 함수의 구문 앞에 점 또는 대괄호 표기 여부로 판단**합니다.

```javascript
var obj1 = {
    outer: function() {
        console.log(this);  // (1)
        var innerFunc = function () {
            console.log(this);  // (2) (3)
        }
        innerFunc();

        var obj2 = {
            innerMethod: innerFunc
        };
        obj2.innerMethod();
    }
};
obj1.outer();
```
결과 : obj1 > 전역 객체 > obj2

## 메서드의 내부 함수에서의 this를 우회하는 방법
호출 주체가 없을 때 자동으로 전역객체를 바인딩하지 않고 호출 당시 주변 환경의 this를 그대로 상속받아 사용할 수 있을 까?

=> ES5에서는 변수를 활용하면 가능
* outer 스코프에서 self라는 변수에 this를 저장하고, 이를 innerFun2에서 사용

```javascript
var obj = {
    outer: function() {
        console.log(this);              // { outer: f }
        var innerFunc1 = function() {
            console.log(this);          // Window { ... }
        };
        innerFunc1();

        var self = this;    // *
        var innerFun2 = function() {
            console.log(self);          // { outer: f }
        };
        innerFun2();
    }
};
obj.outer();
```

## this를 바인딩하지 않는 함수 : ES6의 화살표 함수
화살표 함수는 실행 컨텍스트를 생성할 때 this 바인딩 과정 자체가 빠지게 되어, **상위 스코프의 this를 그대로 활용** 가능하다.

```javascript
var obj = {
    outer: function() {
        console.log(this);          // { outer: f }
        var innerFunc = () => {
            console.log(this);      // { outer: f }
        };
        innerFunc();
    }
};
obj.outer();
```

# 콜백 함수 호출시 그 함수 내부에서의 this
콜백 함수의 정의와 동작 원리 등에 대해서는 4장에서 다룹니다.

여기서는 this가 어떤 값을 참조하는지만 간단히 확인하고 넘어가겠습니다.

콜백함수
* 함수 A의 제어권을 다른 함수(또는 메서드) B에게 넘겨주는 경우 함수 A를 콜백함수라고 합니다.
* 이때 함수 A는 함수 B의 내부 로직에 따라 실행되며, this 역시 함수 B 내부 로직에서 정한 규칙에 따라 값이 결정 됩니다.

**콜백함수에서 this**
* 기본적으로 this가 전역객체를 참조
* 제어권을 받은 함수에서 콜백 함수에 별도로 this가 될 대상을 지정한 경우에는 그 대상을 참조

```javascript
setTimeout(function() {console.log(this;)}, 300);   // 전역 객체

[1, 2, 3, 4, 5].forEach(function (x) {
    console.log(this, x);                           // 전역 객체, 배열의 각 요소
});

document.body.innerHTMl += '<button id="a">클릭</button>';
document.body.querySelector('#a')
    .addEventListener('click', function(e) {
        console.log(this, e);                       // 지정한 엘리먼트(#a), 클릭 이벤트에 관한 정보 객체
    });
```

* setTimeout, forEach 메서드 : 콜백 함수 호출시 this를 지정X
* addEventListener 메서드 : 콜백 함수 호출시 자신의 this를 상속하도록 정의

# 생성자 함수 내부에서의 this
생성자 함수
* 어떤 공통된 성질을 지니는 **객체들을 생성하는 데 사용하는 함수**
* JS에서는 함수에 생성자로서의 역할을 함께 부여
  * `new` 명령어와 함께 함수를 호출하면 해당 함수가 생성자로 동작

**생성자 함수로서 호출된 경우, 내부에서의 this는 곧 새로 만들 구체적인 인스턴스 자신이 됩니다.**
1. 생성자의 prototype 프로퍼티를 참조하는 __proto__라는 프로퍼티가 있는 객체(인스턴스) 생성
2. 미리 준비된 공통 속성 및 개성을 해당 객체(this)에 부여

```javascript
var Cat = function (name, age) {
    this.bark = '야옹';
    this.name = name;
    this.age = age;
};

var choco = new Cat('초코', 7); // 생성자 함수 호출시 내부에서의 this는 choco 인스턴스
var nabi = new Cat('나비', 5); // 생성자 함수 호출시 내부에서의 this는 nabi 인스턴스
console.log(choco, nabi);

// 결과
// Cat { bark: '야옹', name: '초코', age: 7 }
// Cat { bark: '야옹', name: '나비', age: 5 }
```

# 정리
this 바인딩
* 전역 공간에서의 this : 전역 객체
* 메서드 내부에서의 this : 호출한 객체(마지막 점 앞에 명시된 객체)
* 메서드의 내부 함수에서의 this : 전역 객체
* 함수 내부에서의 this : 전역 객체
* 콜백 함수 호출시 그 함수 내부에서의 this
  * 기본적으로 this가 전역객체를 참조
  * 제어권을 받은 함수에서 콜백 함수에 별도로 this가 될 대상을 지정한 경우에는 그 대상을 참조
* 생성자 함수 내부에서의 this : 곧 새로 만들 구체적인 인스턴스 자신

메서드의 내부 함수에서의 this를 우회하는 방법
* ES5 : 메서드에서 self라는 변수에 this를 저장하고, 이를 메서드의 내부 함수에서 사용
* ES6 : 화살표 함수
