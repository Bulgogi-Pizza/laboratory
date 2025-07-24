import pandas as pd
import glob
import re

# --- 1. 데이터 불러오기 및 파싱 ---
file_list = glob.glob('performance_summary_report_*.md')
all_data = []

print(f"{len(file_list)}개의 결과 파일을 찾았습니다.")

for f_path in file_list:
  # 파일명에서 시나리오(multi, normal, single)와 실행 번호 추출
  match = re.search(r'report_(multi|normal|single)_(\d+)\.md', f_path)
  if not match:
    continue
  scenario, run = match.groups()

  with open(f_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    # 테이블 데이터 라인만 추출 (헤더, 구분선 제외)
    table_lines = [line for line in lines if line.strip().startswith(
      '|') and '---' not in line and '시나리오' not in line]

    for line in table_lines:
      parts = [p.strip() for p in line.split('|')][1:-1]
      if len(parts) != 5:
        continue

      test_case, tps, latency, cpu, memory = parts

      # 숫자만 추출 (단위 제거)
      tps_val = pd.to_numeric(re.sub(r'[^0-9.]', '', tps), errors='coerce')
      latency_val = pd.to_numeric(re.sub(r'[^0-9.]', '', latency),
                                  errors='coerce')
      cpu_val = pd.to_numeric(re.sub(r'[^0-9.]', '', cpu), errors='coerce')
      memory_val = pd.to_numeric(re.sub(r'[^0-9.]', '', memory),
                                 errors='coerce')

      all_data.append({
        'scenario': scenario,
        'run': int(run),
        'test_case': test_case,
        'TPS': tps_val,
        'Latency (ms)': latency_val,
        'CPU (%)': cpu_val,
        'Memory (KB)': memory_val,
      })

if not all_data:
  print("처리할 데이터를 찾지 못했습니다. 파일명을 확인해주세요.")
  exit()

df = pd.DataFrame(all_data)

# --- 2. 시나리오별 평균 계산 ---
avg_df = df.groupby(['scenario', 'test_case']).mean().drop(columns='run').round(
  2)
print("\n시나리오별 평균값 계산 완료.")

# --- 3. HTML 보고서 생성 ---

# 피벗 테이블 생성
tps_pivot = avg_df['TPS'].unstack(level='scenario')
latency_pivot = avg_df['Latency (ms)'].unstack(level='scenario')
cpu_pivot = avg_df['CPU (%)'].unstack(level='scenario')
memory_pivot = avg_df['Memory (KB)'].unstack(level='scenario')

html = """
<html>
<head>
<title>성능 테스트 종합 결과</title>
<style>
    body { font-family: sans-serif; margin: 2em; }
    h1, h2 { color: #333; }
    table { border-collapse: collapse; width: 100%; margin-bottom: 2em; }
    th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
    th { background-color: #f2f2f2; }
    tr:nth-child(even) { background-color: #f9f9f9; }
    .bar-container { width: 100px; background-color: #eee; display: inline-block; vertical-align: middle; height: 1em; border-radius: 3px; }
    .bar { height: 100%; background-color: #4CAF50; border-radius: 3px; }
</style>
</head>
<body>
<h1>📊 성능 테스트 종합 결과</h1>
<p>각 시나리오별 5회 실행의 평균값입니다.</p>
"""


def generate_table_with_bars(pivot_table, title):
  html_table = f"<h2>{title}</h2>"
  # NaN 값을 0으로 채우고, 최대값 계산
  pivot_table_filled = pivot_table.fillna(0)
  max_val = pivot_table_filled.max().max()

  # HTML 테이블 생성 시작
  html_table += "<table><thead><tr><th>Test Case</th>"
  for col in pivot_table.columns:
    html_table += f"<th>{col}</th>"
  html_table += "</tr></thead><tbody>"

  for index, row in pivot_table.iterrows():
    html_table += f"<tr><td>{index}</td>"
    for col in pivot_table.columns:
      val = row[col]
      if pd.isna(val):
        html_table += "<td>N/A</td>"
      else:
        # 막대 그래프 길이 계산
        bar_width = (val / max_val) * 100 if max_val > 0 else 0
        html_table += f"""
                <td>
                    {val:,.2f}
                    <div class="bar-container">
                        <div class="bar" style="width: {bar_width}%;"></div>
                    </div>
                </td>
                """
    html_table += "</tr>"

  html_table += "</tbody></table>"
  return html_table


html += generate_table_with_bars(tps_pivot, "🚀 TPS (초당 요청 수) 비교")
html += generate_table_with_bars(cpu_pivot, "⚙️ 총 CPU 사용량 (%) 비교")
html += generate_table_with_bars(latency_pivot, "⏱️ 평균 Latency (ms) 비교")
html += generate_table_with_bars(memory_pivot, "🧠 총 메모리 사용량 (KB) 비교")

html += "</body></html>"

# 파일로 저장
with open('final_summary.html', 'w', encoding='utf-8') as f:
  f.write(html)

print("\n보고서 생성 완료: final_summary.html 파일을 확인하세요.")