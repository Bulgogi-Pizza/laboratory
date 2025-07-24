import pandas as pd
import glob
import re
import json

# --- 1. 데이터 불러오기 및 파싱 ---
file_list = glob.glob('performance_summary_report_*.md')
all_data = []

if not file_list:
  print("오류: 분석할 '.md' 결과 파일을 찾을 수 없습니다. 파일명을 확인해주세요.")
  exit()

print(f"{len(file_list)}개의 결과 파일을 찾았습니다...")

for f_path in file_list:
  match = re.search(r'report_(multi|normal|single)_(\d+)\.md', f_path)
  if not match:
    continue
  scenario, run = match.groups()

  with open(f_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    table_lines = [line for line in lines if line.strip().startswith(
      '|') and '---' not in line and '시나리오' not in line]

    for line in table_lines:
      parts = [p.strip() for p in line.split('|')][1:-1]
      if len(parts) != 5:
        continue

      test_case, tps, latency, cpu, memory = parts

      all_data.append({
        'scenario': scenario,
        'run': int(run),
        'test_case': test_case,
        'TPS': pd.to_numeric(re.sub(r'[^0-9.]', '', tps), errors='coerce'),
        'Latency (ms)': pd.to_numeric(re.sub(r'[^0-9.]', '', latency),
                                      errors='coerce'),
        'CPU (%)': pd.to_numeric(re.sub(r'[^0-9.]', '', cpu), errors='coerce'),
        'Memory (KB)': pd.to_numeric(re.sub(r'[^0-9.]', '', memory),
                                     errors='coerce'),
      })

df = pd.DataFrame(all_data).dropna()
df['run_label'] = 'Run ' + df['run'].astype(str)

# --- 2. 통계 요약 테이블 생성 ---
numeric_cols = ['TPS', 'Latency (ms)', 'CPU (%)', 'Memory (KB)']
summary_df = df.groupby(['scenario', 'test_case'])[numeric_cols].agg(
    ['min', 'max', 'mean']).round(2)
print("통계 요약 계산 완료...")

# --- 3. HTML 및 Chart.js 보고서 생성 ---
html_template = """
<html>
<head>
    <title>성능 테스트 상세 분석 보고서</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; margin: 2em; background-color: #f8f9fa; color: #212529; }}
        .container {{ max-width: 1200px; margin: auto; }}
        h1, h2, h3 {{ color: #000; border-bottom: 2px solid #dee2e6; padding-bottom: 0.5em; }}
        .scenario-section {{ background-color: #fff; border: 1px solid #dee2e6; border-radius: 8px; padding: 2em; margin-bottom: 2em; }}
        table {{ border-collapse: collapse; width: 100%; margin: 2em 0; font-size: 0.9em; }}
        th, td {{ border: 1px solid #ccc; padding: 10px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        tr:nth-child(even) {{ background-color: #f9f9f9; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 성능 테스트 상세 분석 보고서</h1>
        <p>각 시나리오별 5회 실행에 대한 개별 결과 및 통계 요약입니다.</p>
        {content}
    </div>
</body>
</html>
"""

content_html = ""
scenarios = ['normal', 'single', 'multi']
metrics = ['TPS', 'Latency (ms)', 'CPU (%)', 'Memory (KB)']
chart_titles = {
  'TPS': "🚀 TPS (초당 요청 수)",
  'Latency (ms)': "⏱️ 평균 Latency (ms)",
  'CPU (%)': "⚙️ 총 CPU 사용량 (%)",
  'Memory (KB)': "🧠 총 메모리 사용량 (KB)"
}

for scenario in scenarios:
  if scenario not in summary_df.index.get_level_values('scenario'):
    continue
  content_html += f"<div class='scenario-section'><h2>{scenario.upper()} 시나리오</h2>"

  scenario_df = df[df['scenario'] == scenario]
  if scenario_df.empty:
    content_html += "<p>해당 시나리오에 대한 데이터가 없습니다.</p></div>"
    continue

  for metric in metrics:
    chart_id = f"chart_{scenario}_{metric.replace(' ', '').replace('(', '').replace(')', '').replace('%', '')}"
    content_html += f"<h3>{chart_titles[metric]}</h3>"
    content_html += f'<canvas id="{chart_id}"></canvas>'

    # Chart.js 데이터 준비
    labels = sorted(scenario_df['test_case'].unique())
    datasets = []
    for run_label in sorted(scenario_df['run_label'].unique()):
      run_data = scenario_df[scenario_df['run_label'] == run_label]
      data_points = []
      for label in labels:
        value = run_data[run_data['test_case'] == label][metric].values
        data_points.append(float(value[0]) if len(value) > 0 else 0)
      datasets.append({'label': run_label, 'data': data_points})

    # [수정된 부분] 통계 테이블 준비 방식 변경
    metric_summary_df = summary_df.loc[scenario][metric]

    content_html += f"""
        <script>
            new Chart(document.getElementById('{chart_id}'), {{
                type: 'bar',
                data: {{
                    labels: {json.dumps(labels)},
                    datasets: {json.dumps(datasets)}
                }},
                options: {{
                    scales: {{ y: {{ beginAtZero: true }} }},
                    responsive: true,
                    plugins: {{ legend: {{ position: 'top' }} }}
                }}
            }});
        </script>
        {metric_summary_df.to_html(classes='summary-table')}
        """
  content_html += "</div>"

# 최종 HTML 생성 및 저장
final_html = html_template.replace('{content}', content_html)
report_filename = 'final_summary_detailed.html'
with open(report_filename, 'w', encoding='utf-8') as f:
  f.write(final_html)

print(f"\n상세 보고서 생성 완료: {report_filename} 파일을 확인하세요.")