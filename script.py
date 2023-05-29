import pandas as pd

# xlsx 파일 읽기
df = pd.read_excel("data.xlsx")

# 문자열 값을 숫자로 매핑하기 위한 딕셔너리 생성
mapping = {"전혀 중요하지 않음": 1, "중요하지 않음": 2, "보통": 3, "중요함": 4, "매우 중요함": 5}

# 각 column의 평균 계산을 위해 문자열 값을 숫자로 변환
df = df.apply(lambda x: x.map(mapping) if x.dtype == "O" else x)

# 각 column의 평균 계산
mean_values = df.mean()

# 각 column의 표준 편차 계산
stddev_values = df.std()

# 결과 출력
for column, mean, stddev in zip(df.columns, mean_values, stddev_values):
    print(f"Column: {column}")
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {stddev}")
    print()
