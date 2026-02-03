# 📂 [chap 3 & 4] 제어문 (Control Statements)

## ⚖️ 1. 조건문 (Conditionals)

### 1.1 if-else 문
- 가장 기본적인 조건문으로, 조건식의 참/거짓에 따라 실행할 문장을 결정합니다.
```python
if 조건식:
    문장1
elif 조건식:
    문장2
else:
    문장n

match 변수:
    case 1:
        문장1
    case 2:
        문장2
    case _:  # 아무 케이스에도 해당하지 않을 때 (Wildcard)
        문장3
