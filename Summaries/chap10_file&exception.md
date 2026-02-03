# 📂 [Chap 10] 파일 처리 & 예외 처리

---

## 1️⃣ 파일(File)이란?

파일은 **프로그램 실행이 끝나도 데이터가 남아 있도록 저장하는 공간**이다.

* 메모리 변수 → 프로그램 종료 시 사라짐
* 파일 → 디스크에 저장되어 계속 유지됨

📌 파일 처리는

* 점수 저장
* 로그 기록
* 설정 값 저장
  같은 상황에서 필수

---

## 2️⃣ 파일 열기 / 닫기 (open / close)

```python
f = open("test.txt", "r")  # 파일 열기
f.close()                  # 파일 닫기
```

### 파일 열기 모드

| 모드 | 의미             |
| -- | -------------- |
| r  | 읽기 (파일 없으면 에러) |
| w  | 쓰기 (기존 내용 삭제)  |
| a  | 추가 (뒤에 이어서 작성) |
| r+ | 읽기 + 쓰기        |

⚠️ `w` 모드는 기존 파일 내용을 **전부 지움** → 시험 단골 주의

---

## 3️⃣ 파일 읽기

### (1) read() : 전체 읽기

```python
f = open("data.txt", "r")
data = f.read()
f.close()
```

### (2) readline() : 한 줄씩 읽기

```python
line = f.readline()
```

### (3) readlines() : 모든 줄을 리스트로

```python
lines = f.readlines()
```

📌 파일은 **한 번 읽으면 커서가 끝으로 이동**
→ 다시 읽으려면 reopen 필요

---

## 4️⃣ 파일 쓰기

```python
f = open("data.txt", "w")
f.write("Hello Python")
f.close()
```

여러 줄 쓰기:

```python
lines = ["A\n", "B\n", "C\n"]
f.writelines(lines)
```

📌 `write()`는 자동 줄바꿈 ❌ → `\n` 직접 써야 함

---

## 5️⃣ with 문 (파일 처리 필수 문법 ⭐)

```python
with open("data.txt", "r") as f:
    data = f.read()
```

✔ `close()` 자동 처리
✔ 예외 발생해도 파일 안전

👉 **실무·시험에서 가장 권장되는 방식**

---

## 6️⃣ 예외(Exception)란?

예외는 **프로그램 실행 중 발생하는 오류**이다.

예시:

* 파일이 없음 (`FileNotFoundError`)
* 0으로 나누기 (`ZeroDivisionError`)
* 자료형 오류 (`TypeError`)

📌 예외 처리를 안 하면 → 프로그램 바로 종료

---

## 7️⃣ try - except 기본 구조

```python
try:
    실행문
except 오류종류:
    오류 발생 시 실행
```

예시:

```python
try:
    x = int(input())
except ValueError:
    print("숫자를 입력하세요")
```

---

## 8️⃣ 여러 예외 처리

```python
try:
    a = 10 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없음")
except TypeError:
    print("타입 오류")
```

---

## 9️⃣ else / finally

```python
try:
    f = open("a.txt", "r")
except FileNotFoundError:
    print("파일 없음")
else:
    print("파일 열기 성공")
    f.close()
finally:
    print("무조건 실행")
```

* else : 예외 없을 때만 실행
* finally : 예외 여부 상관없이 항상 실행

---

## 🔟 파일 + 예외 처리 같이 쓰기 ⭐⭐⭐

```python
try:
    with open("score.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("파일이 존재하지 않습니다")
```

👉 **Chap 10의 핵심 조합**

---

