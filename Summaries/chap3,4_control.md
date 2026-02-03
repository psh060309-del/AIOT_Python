# 📂 [Chap 3 & 4] 제어문 (Control Statements)

## ⚖️ [Chap 3] 조건문 (Conditionals)

프로그램의 흐름을 조건에 따라 분기하는 문장입니다.

### 1. if-elif-else 문

조건식의 결과(참/거짓)에 따라 실행할 문장을 결정합니다.

```python
if 조건식:
    문장1
elif 조건식:
    문장2
else:
    문장n
```

---

### 2. match-case 문

특정 변수의 값에 따라 여러 케이스 중 하나를 선택하여 실행합니다.

```python
match 변수:
    case 1:
        문장1
    case 2:
        문장2
    case _:
        문장3  # 아무 케이스에도 해당하지 않을 때 (기본값)
```

---

### 3. 조건 연산자 (삼항 연산자)

**형식**

```python
변수 = x if x > y else y
```

**의미**
`x > y`가 참이면 `x`, 거짓이면 `y`를 변수에 대입합니다.

---

## 🔁 [Chap 4] 반복문 (Loops)

특정 문장들을 반복해서 실행할 때 사용합니다.

### 1. 횟수 반복: for 문

반복을 시작하기 전에 반복 횟수를 미리 아는 경우에 사용합니다.

#### 리스트 활용

```python
for 변수 in 리스트:
    문장1
    문장2
```

#### range() 함수 활용

```python
for 변수 in range(종료값):
    문장

for 변수 in range(start, stop, step):
    문장  # start <= 변수 < stop (종료값은 포함되지 않음)
```

#### 예시 (역순 반복)

```python
for i in range(10, 0, -1):
    print(i, end=" ")
# 결과: 10 9 8 7 6 5 4 3 2 1
```

---

### 2. 조건 반복: while 문

특정 조건이 성립되는 동안 계속해서 문장을 반복 실행합니다.

```python
while 조건식:
    문장1
    문장2
else:
    문장  # 조건식이 거짓이 되어 루프를 빠져나올 때 실행
```

---

### 3. 무한 루프와 break, continue 🛑

* **무한 루프**: `while True:` 처럼 조건이 항상 참인 경우
* **break**: 현재 반복을 완전히 중단하고 루프를 빠져나옴
* **continue**: 현재 반복의 남은 부분을 건너뛰고 다음 반복 시작

#### 활용 예시

```python
while True:
    if 조건1:
        break     # 반복을 중단
    if 조건2:
        continue  # 다음 반복을 시작
```
